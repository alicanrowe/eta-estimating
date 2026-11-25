#!/usr/bin/env python3
"""ETA helper: measured baselines, ranges, fan-out and transfer maths, and a prediction ledger.

Data lives next to this script:
  ../data/observations.csv   one row per measured duration (minutes unless the category says _h, _sec or _usd)
  ../data/predictions.csv    every ETA given, and what actually happened
  ../references/baselines.md the table between the AUTO markers is rebuilt by `eta.py rebuild`

Commands
  eta.py stats [CATEGORY]                       ranges per category (p10 / p50 / p90, n)
  eta.py add CATEGORY VALUE --source S [--note N] [--start ISO]
  eta.py fanout --n 94 --cat jewelry_piece_cold [--cap 40] [--stagger-sec 3]
  eta.py transfer --frames 2160 [--mb 8] [--rate 2.3]
  eta.py predict "what" --p50 MIN --p90 MIN --source S
  eta.py resolve ID ACTUAL_MIN
  eta.py calibration                            how far off past ETAs were
  eta.py rebuild                                regenerate the baselines table
  eta.py stallcheck LISTING.json [--min 3]      flag fan-out threads that started but never ran
  eta.py project --pieces 9 [--design central|fanout] [--kit] [--page] [--kind new_look]
                                                whole-project ETA: this round, and until accepted
Only the standard library is used.
"""
import argparse, csv, datetime as dt, math, os, re, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OBS = os.path.join(ROOT, "data", "observations.csv")
PRED = os.path.join(ROOT, "data", "predictions.csv")
BASE = os.path.join(ROOT, "references", "baselines.md")
CENSORED = "CENSORED"


def load_obs():
    with open(OBS, newline="") as f:
        return list(csv.DictReader(f))


def q(vals, p):
    """Linear-interpolated quantile, p in [0,1]."""
    s = sorted(vals)
    if len(s) == 1:
        return s[0]
    k = (len(s) - 1) * p
    lo, hi = math.floor(k), math.ceil(k)
    return s[lo] + (s[hi] - s[lo]) * (k - lo)


def summarise(rows):
    out = {}
    for r in rows:
        out.setdefault(r["category"], []).append(r)
    res = []
    for cat, rs in sorted(out.items()):
        vals = [float(r["minutes"]) for r in rs]
        cens = sum(1 for r in rs if CENSORED in (r.get("note") or ""))
        n = len(vals)
        res.append(dict(cat=cat, n=n, cens=cens, lo=min(vals), hi=max(vals),
                        p10=q(vals, .1), p50=q(vals, .5), p90=q(vals, .9),
                        thin=n < 4))
    return res


def unit(cat):
    if cat.endswith("_h"):
        return "h"
    if cat.endswith("_sec"):
        return "s"
    if "usd" in cat:
        return "$"
    if cat.endswith("_pct"):
        return "%"
    return "min"


def fmt(v, u):
    if u == "$":
        return f"${v:.0f}"
    if u == "min" and v >= 90:
        return f"{v/60:.1f} h"
    return f"{v:.1f} {u}" if v < 10 else f"{v:.0f} {u}"


def cmd_stats(a):
    rows = load_obs()
    if a.category:
        rows = [r for r in rows if r["category"] == a.category]
        if not rows:
            sys.exit(f"no observations for {a.category}")
    for s in summarise(rows):
        u = unit(s["cat"])
        flag = " (thin: give min-max, widen)" if s["thin"] else ""
        cens = f" ({s['cens']} still running, true value higher)" if s["cens"] else ""
        print(f"{s['cat']:<32} n={s['n']:<3} p10 {fmt(s['p10'],u):>8}  p50 {fmt(s['p50'],u):>8}  "
              f"p90 {fmt(s['p90'],u):>8}  range {fmt(s['lo'],u)}-{fmt(s['hi'],u)}{flag}{cens}")


def cmd_add(a):
    new = not os.path.exists(OBS)
    with open(OBS, "a", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        if new:
            w.writerow(["category", "minutes", "start_utc", "source", "note"])
        w.writerow([a.category, a.value, a.start or "", a.source, a.note or ""])
    print(f"added {a.category} = {a.value}")


def cmd_fanout(a):
    rows = [r for r in load_obs() if r["category"] == a.cat]
    if not rows:
        sys.exit(f"no observations for {a.cat}")
    vals = [float(r["minutes"]) for r in rows]
    p50, p90, mx = q(vals, .5), q(vals, .9), max(vals)
    waves = math.ceil(a.n / a.cap)
    spawn = a.n * a.stagger_sec / 60.0  # threads are started one after another
    # the wave finishes when its slowest piece finishes, so use p90..max per wave
    lo = spawn + p50 + (waves - 1) * p90
    hi = spawn + waves * max(p90, mx) + a.slack
    print(f"{a.n} pieces, cap {a.cap} at once -> {waves} wave(s); starting threads takes ~{spawn:.0f} min")
    print(f"per piece p50 {p50:.1f} min, p90 {p90:.1f}, worst {mx:.1f}")
    print(f"whole batch: {lo:.0f}-{hi:.0f} min (add a central-fix round if shared code changes)")


def cmd_transfer(a):
    secs = a.frames * a.mb / a.rate
    print(f"{a.frames} frames x {a.mb} MB at {a.rate} MB/s = {secs/3600:.1f} h of pure transfer")
    print("measured reality was ~2x that (farm tail frames, pauses): plan "
          f"{secs/3600:.1f}-{2*secs/3600:.1f} h")


def _read_pred():
    if not os.path.exists(PRED):
        return []
    with open(PRED, newline="") as f:
        return list(csv.DictReader(f))


def _write_pred(rows):
    cols = ["id", "made_utc", "what", "p50_min", "p90_min", "actual_min",
            "ratio_actual_to_p50", "status", "source"]
    with open(PRED, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def cmd_predict(a):
    rows = _read_pred()
    nid = max([int(r["id"]) for r in rows] or [0]) + 1
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    rows.append(dict(id=nid, made_utc=now, what=a.what, p50_min=a.p50, p90_min=a.p90,
                     actual_min="", ratio_actual_to_p50="", status="open", source=a.source))
    _write_pred(rows)
    print(f"logged prediction {nid}")


def cmd_resolve(a):
    rows = _read_pred()
    for r in rows:
        if r["id"] == str(a.id):
            r["actual_min"] = a.actual
            r["ratio_actual_to_p50"] = f"{float(a.actual)/float(r['p50_min']):.2f}"
            r["status"] = "closed"
            _write_pred(rows)
            print(f"closed {a.id}: ratio {r['ratio_actual_to_p50']}")
            return
    sys.exit(f"no prediction {a.id}")


def cmd_calibration(_a):
    rs = [float(r["ratio_actual_to_p50"]) for r in _read_pred() if r["ratio_actual_to_p50"]]
    if not rs:
        print("no closed predictions yet")
        return
    print(f"{len(rs)} closed ETAs: median actual/p50 = {statistics.median(rs):.2f}, "
          f"worst = {max(rs):.2f}, best = {min(rs):.2f}")
    late = sum(1 for x in rs if x > 1.0)
    print(f"{late} of {len(rs)} ran over their p50")


def cmd_rebuild(_a):
    lines = ["| What | n | Typical (p50) | Range (p10 to p90) | Seen |", "|---|---|---|---|---|"]
    for s in summarise(load_obs()):
        u = unit(s["cat"])
        note = " (few samples)" if s["thin"] else ""
        if s["cens"]:
            note += " (one still running)"
        lines.append(f"| `{s['cat']}` | {s['n']} | {fmt(s['p50'],u)} | {fmt(s['p10'],u)} to {fmt(s['p90'],u)} | "
                     f"{fmt(s['lo'],u)} to {fmt(s['hi'],u)}{note} |")
    table = "\n".join(lines)
    with open(BASE) as f:
        txt = f.read()
    txt = re.sub(r"<!-- AUTO:START -->.*<!-- AUTO:END -->",
                 "<!-- AUTO:START -->\n" + table + "\n<!-- AUTO:END -->", txt, flags=re.S)
    with open(BASE, "w") as f:
        f.write(txt)
    print(f"rebuilt {BASE}")


def _parse_ts(t):
    return dt.datetime.fromisoformat(t.replace("Z", "+00:00"))


def cmd_stallcheck(a):
    """Read a saved list_threads result (JSON with a 'sessions' list) and flag stalled threads."""
    import json
    with open(a.listing) as f:
        data = json.load(f)
    sess = data.get("sessions", data if isinstance(data, list) else [])
    now = _parse_ts(a.now) if a.now else dt.datetime.now(dt.timezone.utc)
    stalled, running = [], 0
    for s in sess:
        if s.get("state") != "working":
            continue
        running += 1
        c, l = _parse_ts(s["created_at"]), _parse_ts(s["last_activity_at"])
        idle_since_start = (l - c).total_seconds() < 5
        age = (now - c).total_seconds() / 60
        quiet = (now - l).total_seconds() / 60
        if (idle_since_start and age >= a.min) or quiet >= a.quiet:
            stalled.append((s.get("title", "?"), age, quiet, idle_since_start))
    print(f"{running} threads working; {len(stalled)} look stalled")
    for t, age, quiet, never in stalled:
        why = "never started" if never else f"quiet {quiet:.0f} min"
        print(f"  STALLED  {t}  (started {age:.0f} min ago, {why})")
    if stalled:
        print("Restart these as others finish, and add up to 90 min to the late end of the ETA until they run.")


# ---------------------------------------------------------------- whole-project estimates
PROJ = os.path.join(ROOT, "data", "projects.csv")


def _samples(cat, rows):
    v = [float(r["minutes"]) for r in rows if r["category"] == cat]
    if not v:
        sys.exit(f"no observations for {cat}; add some or pick another --*-cat")
    return v


def _draw(rng, vals):
    """One plausible duration. Thin data (<4) is widened to 0.8 x min .. 1.5 x max, peaked at the median."""
    if len(vals) < 4:
        return rng.triangular(0.8 * min(vals), 1.5 * max(vals), statistics.median(vals))
    return rng.choice(vals) * math.exp(rng.gauss(0, 0.2))


def _p_accept(kind):
    """Chance a delivered round is accepted, from projects.csv (Laplace-smoothed)."""
    acc = rej = 0
    if os.path.exists(PROJ):
        with open(PROJ, newline="") as f:
            for r in csv.DictReader(f):
                if r["kind"] != kind:
                    continue
                acc += r["outcome"] == "accepted"
                rej += r["outcome"] == "rejected"
    return (acc + 1) / (acc + rej + 2), acc, rej


def _gate(rng, at_local_h, mode, rows):
    """Minutes until the user gives a verdict on a delivered round."""
    if mode == "none":
        return 0.0
    if mode == "active":
        return rng.uniform(10, 40)
    h = at_local_h % 24
    if h >= 23 or h < 8:          # delivered at night: answer after waking
        wake = (9 - h) % 24
        return wake * 60 + rng.uniform(0, 60)
    if h >= 16:                    # evening: active or out, measured 24 min to 4.6 h
        return rng.choice([24, 39, 67, 277]) * math.exp(rng.gauss(0, 0.3))
    return _draw(rng, _samples("human_gate_daytime_away", rows))


def cmd_project(a):
    import random
    rows = load_obs()
    rng = random.Random(a.seed)
    S = lambda c: _samples(c, rows)
    kit = S(a.kit_cat) if a.kit else None
    design_c = S(a.design_cat) if a.design == "central" else None
    piece = S(a.piece_cat) if a.design == "fanout" else None
    render = S(a.render_cat) if a.design == "central" and a.render_cat != "none" else None
    fixtail = S("proj_fix_tail")
    page = S(a.page_cat) if a.page else None
    stall = S("platform_concurrency_stall")
    p_acc, n_acc, n_rej = _p_accept(a.kind)
    if a.p_accept is not None:
        p_acc = a.p_accept
    start = _parse_ts(a.start) if a.start else dt.datetime.now(dt.timezone.utc)
    tz = dt.timezone(dt.timedelta(hours=a.tz))

    def one_round(rework):
        parts = {}
        parts["kit"] = _draw(rng, kit) * (0.5 if rework else 1) if kit else 0.0
        threads = 0
        if a.design == "central":
            parts["design"] = _draw(rng, design_c)
            if render:
                threads = math.ceil(a.pieces / a.per_thread)
                waves = math.ceil(threads / a.cap)
                parts["render"] = threads * 3 / 60 + sum(max(_draw(rng, render) for _ in range(min(a.cap, threads)))
                                                         for _ in range(waves))
            else:
                parts["render"] = 0.0
        else:
            threads = a.pieces
            waves = math.ceil(threads / a.cap)
            parts["design"] = threads * 3 / 60 + sum(max(_draw(rng, piece) for _ in range(min(a.cap, threads)))
                                                     for _ in range(waves))
            parts["render"] = 0.0
        fails = sum(rng.random() < a.fail_pct / 100 for _ in range(a.pieces))
        parts["fix"] = _draw(rng, fixtail) * min(1.0, 0.4 + fails / 21) if fails else 0.0
        if threads > a.stall_above and rng.random() < 0.5:
            parts["stall"] = _draw(rng, stall)
        else:
            parts["stall"] = 0.0
        if page:
            pg = _draw(rng, page) * a.page_scale
            # the page is built while machines render, but fix rounds take the same agent's attention; +5 merge/live
            parts["page"] = max(0.0, pg - parts["render"] - parts["stall"]) + 5
        else:
            parts["page"] = 0.0
        # one shared factor per round: when a job is harder than usual, every phase of it is slower
        f = math.exp(rng.gauss(0, a.spread))
        for k in list(parts):
            parts[k] *= f
        parts["total"] = parts["kit"] + parts["design"] + parts["render"] + parts["fix"] + parts["stall"] + parts["page"]
        return parts

    first, full, rounds_used, phase = [], [], [], {}
    for _ in range(a.trials):
        r = one_round(False)
        for k, v in r.items():
            phase.setdefault(k, []).append(v)
        t = r["total"]
        first.append(t)
        n = 1
        while rng.random() > p_acc and n < a.max_rounds:
            when = start + dt.timedelta(minutes=t)
            t += _gate(rng, when.astimezone(tz).hour + when.astimezone(tz).minute / 60, a.gate, rows)
            t += one_round(True)["total"]
            n += 1
        full.append(t)
        rounds_used.append(n)

    def clock(m):
        return (start + dt.timedelta(minutes=m)).astimezone(tz).strftime("%a %-I:%M %p")

    print(f"{a.pieces} pieces, design={a.design}, kind={a.kind}, {a.trials} simulated runs from {clock(0)} (UTC{a.tz:+g})")
    print("phase medians: " + ", ".join(f"{k} {statistics.median(v):.0f}" for k, v in phase.items() if k != "total") + " min")
    p10, p50, p90 = q(first, .1), q(first, .5), q(first, .9)
    print(f"THIS ROUND delivered: p50 {fmt(p50,'min')} (p10 {fmt(p10,'min')}, p90 {fmt(p90,'min')})  ->  {clock(p50)} to {clock(p90)}")
    src = f"{n_acc} accepted / {n_rej} rejected rounds of kind '{a.kind}'" if a.p_accept is None else "given"
    print(f"chance this round is accepted: {p_acc:.0%} ({src})")
    f50, f90 = q(full, .5), q(full, .9)
    print(f"UNTIL ACCEPTED (incl. review waits, rework rounds; median {statistics.median(rounds_used):.0f} rounds, "
          f"p90 {q(rounds_used,.9):.0f}): p50 {fmt(f50,'min')}, p90 {fmt(f90,'min')}  ->  {clock(f50)} to {clock(f90)}")
    print("Quote THIS ROUND as the ETA; give UNTIL ACCEPTED as the full-scope range when the user asks how long the whole thing takes.")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("stats"); s.add_argument("category", nargs="?"); s.set_defaults(f=cmd_stats)
    s = sp.add_parser("add"); s.add_argument("category"); s.add_argument("value", type=float)
    s.add_argument("--source", required=True); s.add_argument("--note"); s.add_argument("--start")
    s.set_defaults(f=cmd_add)
    s = sp.add_parser("fanout"); s.add_argument("--n", type=int, required=True)
    s.add_argument("--cat", required=True); s.add_argument("--cap", type=int, default=40)
    s.add_argument("--stagger-sec", type=float, default=3.0); s.add_argument("--slack", type=float, default=5.0)
    s.set_defaults(f=cmd_fanout)
    s = sp.add_parser("transfer"); s.add_argument("--frames", type=int, required=True)
    s.add_argument("--mb", type=float, default=8.0); s.add_argument("--rate", type=float, default=2.3)
    s.set_defaults(f=cmd_transfer)
    s = sp.add_parser("predict"); s.add_argument("what"); s.add_argument("--p50", type=float, required=True)
    s.add_argument("--p90", type=float, required=True); s.add_argument("--source", required=True)
    s.set_defaults(f=cmd_predict)
    s = sp.add_parser("resolve"); s.add_argument("id", type=int); s.add_argument("actual", type=float)
    s.set_defaults(f=cmd_resolve)
    s = sp.add_parser("calibration"); s.set_defaults(f=cmd_calibration)
    s = sp.add_parser("rebuild"); s.set_defaults(f=cmd_rebuild)
    s = sp.add_parser("stallcheck"); s.add_argument("listing")
    s.add_argument("--min", type=float, default=3.0, help="minutes after start with no activity")
    s.add_argument("--quiet", type=float, default=20.0, help="minutes of silence on a started thread")
    s.add_argument("--now", help="ISO time to measure against (default: now)")
    s.set_defaults(f=cmd_stallcheck)
    s = sp.add_parser("project", help="whole-project ETA: this round, and until accepted")
    s.add_argument("--pieces", type=int, required=True)
    s.add_argument("--design", choices=["central", "fanout"], default="central",
                   help="central: one agent designs all, then frozen-code renders fan out; fanout: one piece per machine")
    s.add_argument("--kind", default="new_look", help="new_look (first time for this kind of thing) or known_kind")
    s.add_argument("--kit", action="store_true", help="a shared kit and briefs come first")
    s.add_argument("--kit-cat", default="proj_kit_and_briefs")
    s.add_argument("--design-cat", default="proj_design_round_central")
    s.add_argument("--piece-cat", default="proj_fanout_piece_design")
    s.add_argument("--render-cat", default="proj_render_batch4_wave", help="'none' if renders are part of design")
    s.add_argument("--per-thread", type=int, default=4)
    s.add_argument("--fail-pct", type=float, default=33.0, help="share of pieces failing checks after wave 1")
    s.add_argument("--page", action="store_true", help="ends with a site page, PR and live check")
    s.add_argument("--page-cat", default="proj_page_build_merge")
    s.add_argument("--page-scale", type=float, default=1.0, help="2 for a big page (history, call-outs, viewers)")
    s.add_argument("--gate", choices=["auto", "active", "none"], default="auto")
    s.add_argument("--p-accept", type=float)
    s.add_argument("--max-rounds", type=int, default=6)
    s.add_argument("--cap", type=int, default=40)
    s.add_argument("--stall-above", type=int, default=30)
    s.add_argument("--start", help="ISO UTC start (default now)")
    s.add_argument("--tz", type=float, default=-5.0, help="user's UTC offset (New York -5)")
    s.add_argument("--spread", type=float, default=0.25, help="shared per-round uncertainty (log sd)")
    s.add_argument("--trials", type=int, default=4000)
    s.add_argument("--seed", type=int, default=7)
    s.set_defaults(f=cmd_project)
    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
