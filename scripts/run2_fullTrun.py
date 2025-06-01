#!/usr/bin/env python3
"""
full_turn.py – STS3215 sanity-check
Moves the chosen servo one clockwise revolution (0 → 360 deg → 0),
prints the live position, then relaxes torque.
"""

import sys, time
import scservo_sdk as scs

PORT      = "/dev/ttyACM0"
BAUDRATE  = 1_000_000         # default factory value
ID        = int(sys.argv[1])  # 1st CLI argument

# ---- registers (same as other FEETECH serial servos) --------------
TORQUE_EN        = 40               # 0x28
GOAL_POS_L       = 42               # 0x2A/0x2B
PRESENT_POS_L    = 56               # 0x38/0x39

# ---- helpers -------------------------------------------------------
def set_torque(p, on): packet.write1ByteTxRx(p, ID, TORQUE_EN, 1 if on else 0)
def write_pos(p, val): packet.write2ByteTxRx(p, ID, GOAL_POS_L, val & 0x0FFF)
def read_pos(p):       v, res, _ = packet.read2ByteTxRx(p, ID, PRESENT_POS_L); return v

# -------------------------------------------------------------------
port   = scs.PortHandler(PORT)
packet = scs.PacketHandler(0)

assert port.openPort() and port.setBaudRate(BAUDRATE), "Cannot open port"

try:
    set_torque(port, True)

    # a) jump to raw 0   (define “zero”)
    write_pos(port, 0)
    time.sleep(2)

    # b) go all the way to 4095  (= ≈360 °)
    write_pos(port, 4095)
    time.sleep(2)                # adjust for speed / load

    # c) wrap back to 0 so you see a clean full turn
    write_pos(port, 0)
    time.sleep(2)

    pos = read_pos(port)
    deg = pos * 360 / 4095
    print(f"Position now {pos} raw  ≈ {deg:.1f} °")

finally:
    set_torque(port, False)
    port.closePort()

