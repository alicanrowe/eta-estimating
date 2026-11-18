# ETA estimating skill

A Claude skill for giving honest time estimates on creative production work: renders, render-and-check loops, splitting a batch across many cloud machines, farm animations, CAD, site work, and the waits on a person (sign-ins, OKs, unlocking a computer).

It answers with a range in the user's time zone, names what could make it late, logs every estimate, and compares it with what actually happened. The baselines update as new measurements come in.

## What's in it
- **`SKILL.md`**: the method Claude follows: split the job into steps, look each up, add loop rounds, fan-out waves, transfers and waits, then say it as a clock-time range.
- **`references/baselines.md`**: the measured table and what each row means (jewelry renders one per machine, furniture variants with render-check loops, farm animation upload, render, download and encode, web features, research, and how long people take to answer).
- **`data/observations.csv`**: every measured duration behind the table.
- **`data/predictions.csv`**: past ETAs and how far off they were.
- **`scripts/eta.py`**: ranges per category, fan-out and transfer maths, the prediction ledger and calibration. Standard library only.

## Install
- **Claude.ai / Claude app:** zip this folder and upload it under Settings > Capabilities > Skills.
- **Claude Code:** copy the folder to `~/.claude/skills/eta-estimating/`.

## Quick start
```
python3 scripts/eta.py stats                                   # all ranges
python3 scripts/eta.py fanout --n 94 --cat jewelry_piece_cold --cap 40
python3 scripts/eta.py transfer --frames 2160 --mb 8 --rate 2.3
python3 scripts/eta.py predict "farm download" --p50 120 --p90 240 --source "my thread"
python3 scripts/eta.py resolve 6 253
python3 scripts/eta.py add farm_download_2160f_h 4.2 --source "my thread"
python3 scripts/eta.py rebuild                                 # refresh the table
python3 scripts/eta.py calibration
```

## Where the numbers come from
About 140 measurements from two days of real studio work in November 2026: thread start and finish times, Blender render logs and GarageFarm jobs. Your own work will differ, so log your ETAs and add your own measurements; the table rebuilds from them.
