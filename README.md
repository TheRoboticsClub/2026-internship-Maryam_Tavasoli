# JdeRobot Internship 2026 — Maryam Tavasoli

Research internship at [JdeRobot](https://jderobot.github.io/) / RoboticsLab URJC, supervised by Prof. José María Cañas and Dr. Luis Bote-Curiel.

**Topic:** deep reinforcement learning for robot pick-and-place in MuJoCo, and explainability of the learned policy (machine learning + XAI).

**Blog (weekly progress):** https://theroboticsclub.github.io/2026-internship-Maryam_Tavasoli/

## Layout

- `docs/` — the blog (Jekyll, served by GitHub Pages from this folder)
- `scripts/` — small utilities (`check_mujoco.py`: physics + rendering benchmark for any MJCF scene)
- `src/` — the internship code (environments, training, explainability), added as the work progresses

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/check_mujoco.py path/to/scene.xml
```

MuJoCo is pinned to 3.11.0 to match the lab's mjlab-based projects.

On macOS: run `python -m mujoco.viewer` with plain `python`, and scripts that use `mujoco.viewer.launch_passive` with `mjpython`.
