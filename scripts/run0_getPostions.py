#!/usr/bin/env python3
"""
read_pos.py ― read present position of Feetech IDs 1‒6

Usage
  python read_pos.py                # default /dev/ttyACM0 @1 Mbps
  python read_pos.py /dev/ttyUSB0   # custom serial port
-----------------------------------------------------------------
Requires:  pip install scservo-sdk
Make sure your user can open the port:
  sudo usermod -aG dialout $USER && newgrp dialout
"""

import sys, time
import scservo_sdk as scs

PORT      = sys.argv[1] if len(sys.argv) > 1 else "/dev/ttyACM0"
BAUDRATE  = 1_000_000                 # adjust if you changed it
IDS       = range(1, 7)               # 1 2 3 4 5 6
RAW_MAX   = 4095                      # 12-bit, STS3215
ADDR_POS  = 56                        # Present_Position low byte
BYTES     = 2

def raw_to_deg(raw): return raw * 360 / RAW_MAX

port   = scs.PortHandler(PORT)
packet = scs.PacketHandler(0)         # Feetech protocol-0

if not (port.openPort() and port.setBaudRate(BAUDRATE)):
    sys.exit(f"Cannot open {PORT} @ {BAUDRATE} baud")

try:
    reader = scs.GroupSyncRead(port, packet, ADDR_POS, BYTES)
    for sid in IDS:
        reader.addParam(sid)

    # single broadcast read
    if reader.txRxPacket() != scs.COMM_SUCCESS:
        sys.exit("⚠️  Read failed (bus or baud-rate mismatch?)")

    print(f"ID : Raw   →  Degrees")
    print("-" * 28)
    for sid in IDS:
        val = reader.getData(sid, ADDR_POS, BYTES)
        if val == 0:   # heuristic: probably no servo, raw 0 = hard limit
            print(f"{sid:2d} : ----  (no reply)")
            continue
        print(f"{sid:2d} : {val:4d} → {raw_to_deg(val):7.2f}°")
        time.sleep(1)

finally:
    port.closePort()

