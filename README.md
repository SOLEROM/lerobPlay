

ref git clone https://github.com/huggingface/lerobot.git 


conda create -y -n lerobot python=3.10
conda activate lerobot

conda install ffmpeg -c conda-forge
pip install -e ".[feetech]"
pip install -e .
pip install -e ".[aloha, pusht]"



# configs

lerobot/common/robot_devices/robots/configs.py
prot = ???


## engine id set

python lerobot/scripts/configure_motor.py  --port /dev/ttyACM0   --brand feetech  --model sts3215  --baudrate 1000000  --ID 6


## visual

python lerobot/scripts/visualize_dataset.py \
    --repo-id lerobot/pusht \
    --episode-index 0

