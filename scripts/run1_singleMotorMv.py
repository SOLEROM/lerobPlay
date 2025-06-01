#!/usr/bin/env python3
"""
move_motor.py  –  minimal STS3215 tester (single-turn)

Usage examples
  # raw-ticks mode (default)
  python move_motor.py  3  1024        # +1024 counts  (≈ 90°)
  python move_motor.py  3 -1024        # -1024 counts  (≈ -90°)

  # degree mode
  python move_motor.py  3  90  deg     # +90°
  python move_motor.py  3 -90  deg     # -90°
--------------------------------------------------------------------------
Prerequisites:
  pip install scservo-sdk
  sudo usermod -aG dialout $USER && newgrp dialout      # serial access
"""

import sys, time
import scservo_sdk as scs

# ─────────────── CLI ───────────────
if len(sys.argv) < 3:
    sys.exit("Usage: python move_motor.py <ID> <pos> [deg]\n"
             "  <pos> :  -4095…4095  (raw-ticks mode)\n"
             "         | -360 …360   (degree mode, add 'deg')")

SID      = int(sys.argv[1])
POS_IN   = float(sys.argv[2])
DEG_MODE = len(sys.argv) >= 4 and sys.argv[3].lower().startswith("deg")

# ───────────── constants ────────────
RAW_MAX      = 4095                 # 12-bit encoder
SERIAL_PORT  = "/dev/ttyACM0"
BAUDRATE     = 1_000_000
TORQUE_EN    = 40                   # 0x28
GOAL_L, PRES_L = 42, 56             # Goal & Present Position

# ─────────── conversions ────────────
def to_raw(val_deg_or_raw, degree_mode=False):
    """Returns a wrapped 0-4095 raw value from ±360° or ±4095 ticks."""
    ticks = (val_deg_or_raw * RAW_MAX / 360) if degree_mode else val_deg_or_raw
    return int(ticks) % (RAW_MAX + 1)

def raw_to_deg(raw):
    return raw * 360 / RAW_MAX

GOAL_RAW = to_raw(POS_IN, DEG_MODE)

# ─────────── helpers ────────────────
def w1(port, addr, data): packet.write1ByteTxRx(port, SID, addr, data)
def w2(port, addr, data): packet.write2ByteTxRx(port, SID, addr, data)
def r2(port, addr):
    v, res, _ = packet.read2ByteTxRx(port, SID, addr)
    return v if res == scs.COMM_SUCCESS else None

# ─────────── main flow ──────────────
port, packet = scs.PortHandler(SERIAL_PORT), scs.PacketHandler(0)

if not (port.openPort() and port.setBaudRate(BAUDRATE)):
    sys.exit(f"❌  Cannot open {SERIAL_PORT} @ {BAUDRATE} baud")

try:

    SOFT_START = 0x34
    w1(port, SOFT_START, 1)          # 1 = smooth-start enabled

    w1(port, TORQUE_EN, 1)              # enable
    w2(port, GOAL_L, GOAL_RAW)          # command
    print(f"➡️  Sent {GOAL_RAW} raw ({POS_IN}{'°' if DEG_MODE else ' ticks'})")

    time.sleep(0.5)
    now = r2(port, PRES_L)
    if now is not None:
        print(f"✅  Present: {now} raw  ≈ {raw_to_deg(now):.1f}°")
    else:
        print("⚠️  No reply when reading position")

finally:
    w1(port, TORQUE_EN, 0)              # relax
    port.closePort()

