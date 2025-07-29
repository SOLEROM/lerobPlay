# SO100

https://github.com/huggingface/lerobot
cache will be at : ~/.cache/huggingface/lerobot



https://github.com/TheRobotStudio/SO-ARM100

* major pr changes: https://github.com/huggingface/lerobot/pull/777
* ref git clone https://github.com/huggingface/lerobot.git 

```
conda create -y -n lerobot python=3.10
conda activate lerobot

conda install ffmpeg -c conda-forge
pip install -e ".[feetech]"
pip install -e .
pip install -e ".[aloha, pusht]"
```



## manuals

* https://github.com/TheRobotStudio/SO-ARM100/blob/main/SO100.md
* https://huggingface.co/docs/lerobot/so100
* run inner docs https://github.com/huggingface/lerobot/tree/main/docs  => http://localhost:5173/so100
