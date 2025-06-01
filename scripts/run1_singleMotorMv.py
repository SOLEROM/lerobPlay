#!/usr/bin/env python3
"""
move_motor.py  –  STS3215 tester with optional staged motion

Usage
  # direct jump (default)
  python move_motor.py 3 2048            # +180° raw
  python move_motor.py 3  90 deg         # +90°  degrees

  # smooth ramp (10 equal slices)
  python move_motor.py 3 180 deg --stage
-----------------------------------------------------------------
Prerequisites:
  pip install scservo-sdk
  sudo usermod -aG dialout $USER && newgrp dialout
"""

import sys, time, math
import scservo_sdk as scs

# ──────────────── CLI ─────────────────
if len(sys.argv) < 3:
    sys.exit("Usage: python move_motor.py <ID> <pos> [deg] [--stage]")

SID       = int(sys.argv[1])
POS_IN    = float(sys.argv[2])
DEG_MODE  = 'deg' in [a.lower() for a in sys.argv[3:]]
STAGED    = '--stage' in sys.argv[3:]

# ───────────── constants ──────────────
RAW_MAX        = 4095                     # 12-bit encoder
SERIAL_PORT    = "/dev/ttyACM0"
BAUDRATE       = 1_000_000
TORQUE_EN      = 0x28                     # 40
GOAL_L         = 0x2A                     # 42/43
PRESENT_L      = 0x38                     # 56/57
SOFT_START     = 0x34                     # enable smooth start/stop

# ─────────── conversions ──────────────
def to_raw(val, deg_mode):
    ticks = val * RAW_MAX / 360 if deg_mode else val
    return int(ticks) % (RAW_MAX + 1)

def raw_to_deg(raw): return raw * 360 / RAW_MAX

GOAL_RAW = to_raw(POS_IN, DEG_MODE)

# ─────────── helpers / wrappers ───────
def w1(port, addr, data): packet.write1ByteTxRx(port, SID, addr, data)
def w2(port, addr, data): packet.write2ByteTxRx(port, SID, addr, data)

def r2(port, addr):
    v, res, _ = packet.read2ByteTxRx(port, SID, addr)
    return v if res == scs.COMM_SUCCESS else None

def ramp_move(port, start_raw, target_raw, steps=10, dwell=0.05):
    """Linear interpolation from start_raw to target_raw in <steps> hops."""
    for i in range(1, steps + 1):
        p = (start_raw + (target_raw - start_raw) * i / steps) % (RAW_MAX + 1)
        w2(port, GOAL_L, int(p))
        time.sleep(dwell)

# ───────────── main flow ──────────────
port, packet = scs.PortHandler(SERIAL_PORT), scs.PacketHandler(0)
if not (port.openPort() and port.setBaudRate(BAUDRATE)):
    sys.exit(f"❌  Cannot open {SERIAL_PORT} @ {BAUDRATE} baud")

try:
    w1(port, SOFT_START, 1)          # smooth-start on (sticky until power-cycle)
    w1(port, TORQUE_EN, 1)           # torque enable

    if STAGED:
        now = r2(port, PRESENT_L) or 0
        ramp_move(port, now, GOAL_RAW)
    else:
        w2(port, GOAL_L, GOAL_RAW)

    fmt_in  = f"{POS_IN}{'°' if DEG_MODE else ' ticks'}"
    print(f"➡️  Sent {fmt_in}  →  raw {GOAL_RAW}")

    time.sleep(0.4)
    pos = r2(port, PRESENT_L)
    if pos is not None:
        print(f"✅  Present: {pos} raw  ≈ {raw_to_deg(pos):.1f}°")
    else:
        print("⚠️  No reply when reading position")

finally:
    w1(port, TORQUE_EN, 0)
    port.closePort()

