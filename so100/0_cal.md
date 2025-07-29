# cal


## engine id set

```
python -m lerobot.setup_motors \
    --robot.type=so100_follower \
    --robot.port=/dev/ttyACM0
Connect the controller board to the 'gripper' motor only and press enter.
'gripper' motor id set to 6
Connect the controller board to the 'wrist_roll' motor only and press enter.
'wrist_roll' motor id set to 5
Connect the controller board to the 'wrist_flex' motor only and press enter.
'wrist_flex' motor id set to 4
Connect the controller board to the 'elbow_flex' motor only and press enter.
'elbow_flex' motor id set to 3
Connect the controller board to the 'shoulder_lift' motor only and press enter.
'shoulder_lift' motor id set to 2
Connect the controller board to the 'shoulder_pan' motor only and press enter.
'shoulder_pan' motor id set to 1

```

## cal 


```
python -m lerobot.calibrate \
    --robot.type=so100_follower \
    --robot.port=/dev/ttyACM0 \
     --robot.id=myArm


Move myArm SO100Follower to the middle of its range of motion and press ENTER....
Move all joints except 'wrist_roll' sequentially through their entire ranges of motion.
Recording positions. Press ENTER to stop...

-------------------------------------------
-------------------------------------------
NAME            |    MIN |    POS |    MAX
shoulder_pan    |   1168 |   1972 |   3298
shoulder_lift   |   1921 |   1948 |   4028
elbow_flex      |      0 |   2048 |   4095
wrist_flex      |    394 |   2125 |   2696
gripper         |   2046 |   2163 |   3767
Calibration saved to /home/vlad/.cache/huggingface/lerobot/calibration/robots/so100_follower/myArm.json
```