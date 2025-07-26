# ReachTarget


lerobot/diffusion_pusht
clone to ../policies/diffusion_pusht/

python lerobot/scripts/control_robot.py \
  --robot.type=so100 \
  --control.type=pretrained \
  --control.policy.name=reach_target \
  --control.policy.path=../policies/diffusion_pusht \
  --robot.cameras='{}'
