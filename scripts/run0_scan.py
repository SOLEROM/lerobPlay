from lerobot.common.robot_devices.motors.configs import FeetechMotorsBusConfig
from lerobot.common.robot_devices.motors.feetech import FeetechMotorsBus

# ❶  Tell the bus where it is attached
SERIAL_PORT = "/dev/ttyACM0"          # adjust to your system
BAUDRATE    = 1_000_000               # default for Feetech SCS/STS-series

# ❷  Create a “dummy” motor entry only so the bus knows the **model**
#     (its index is ignored while scanning)
config = FeetechMotorsBusConfig(
    port   = SERIAL_PORT,
    motors = {"probe": (0, "sts3215")},  # or "scs_series" for the SCS servos
)

bus = FeetechMotorsBus(config)
bus.connect()                 # open the USB-serial link
bus.set_bus_baudrate(BAUDRATE)

ids = bus.find_motor_indices()   # scans the whole 0-252 range
print(f"Motors that replied: {ids}")

bus.disconnect()

