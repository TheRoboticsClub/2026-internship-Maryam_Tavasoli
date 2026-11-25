"""Quick MuJoCo sanity check: load a model, time the physics, time off-screen rendering.

Usage:
    python scripts/check_mujoco.py path/to/scene.xml [frame.ppm]

Works with any MJCF scene, e.g. the UR5e from MuJoCo Menagerie.
"""
import sys
import time

import mujoco
import numpy as np


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    path = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else None

    m = mujoco.MjModel.from_xml_path(path)
    d = mujoco.MjData(m)
    print(f"mujoco {mujoco.__version__}: {path}")
    print(f"  {m.nbody} bodies, {m.njnt} joints, {m.nu} actuators, {m.ngeom} geoms")

    n = 20000
    t = time.perf_counter()
    for i in range(n):
        if m.nu:
            d.ctrl[:] = 0.3 * np.sin(i * 0.002 * np.arange(1, m.nu + 1))
        mujoco.mj_step(m, d)
    dt = time.perf_counter() - t
    print(f"physics: {n / dt:,.0f} steps/s ({n * m.opt.timestep / dt:,.0f}x real time, dt={m.opt.timestep})")

    renderer = mujoco.Renderer(m, 480, 640)
    cam = mujoco.MjvCamera()
    mujoco.mjv_defaultFreeCamera(m, cam)
    cam.distance, cam.elevation = 2.0, -25
    k = 60
    t = time.perf_counter()
    img = None
    for _ in range(k):
        for _ in range(10):
            mujoco.mj_step(m, d)
        renderer.update_scene(d, cam)
        img = renderer.render()
    print(f"offscreen render 640x480: {k / (time.perf_counter() - t):.0f} fps")
    if out and img is not None:
        with open(out, "wb") as f:
            f.write(b"P6\n640 480\n255\n")
            f.write(np.ascontiguousarray(img).astype(np.uint8).tobytes())
        print(f"saved {out}")
    renderer.close()


if __name__ == "__main__":
    main()
