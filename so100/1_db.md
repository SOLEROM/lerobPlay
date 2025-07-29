# Visualize datasets

* [see db format](https://github.com/huggingface/lerobot?tab=readme-ov-file#the-lerobotdataset-format)

> python  examples/1_load_lerobot_dataset.py


```

 'weblucas/eval_act_sponge_ball_2_yellow_tray_lerobot_small',
 'sylbae/grab-cube1',
 'abhifoo/new_embodiment_v2_2corrected',
 'modanqing/shelf_pick_and_place_easy_test',
 'satvikahuja/eval_TEST_1_normal_f',
 'nik658/xarm_smolvla',
 'zeta0707/test1',
 'GinoGinetti34/test-250719-1218',
 'nik658/xarm_task_19jul',
 'masato-ka/SO100_evaluate_generalize_pick_pos',
 'Anteid11/hil3',
 'DanqingZ/test-merged-final-format',
 'tmeynier/test_pusht_record_13',
 'tmeynier/test_pusht_record_14',
 'tanxxxx/il_gym0',
 'prahalad123/pick_blue_cube',
 'ankithreddy/test_uno',
 'silverlife/move_pikachu',
 'YutaMoriwaki/record-test',
 'YutaMoriwaki/record-test2',
 'jmarangola/distracted_ballplay',
 'tmeynier/test_pusht_record_16',


 ```

....
.......

```

Number of episodes selected: 85
Number of frames selected: 127500
LeRobotDatasetMetadata({
    Repository ID: 'lerobot/aloha_mobile_cabinet',
    Total episodes: '85',
    Total frames: '127500',
    Features: '['observation.images.cam_high', 'observation.images.cam_left_wrist', 'observation.images.cam_right_wrist', 'observation.state', 'observation.effort', 'action', 'episode_index', 'frame_index', 'timestamp', 'next.done', 'index', 'task_index']',
})',

Dataset({
    features: ['observation.state', 'observation.effort', 'action', 'episode_index', 'frame_index', 'timestamp', 'next.done', 'index', 'task_index'],
    num_rows: 127500
})





<class 'torch.Tensor'>
torch.Size([3, 480, 640])
{'dtype': 'video',
 'names': ['height', 'width', 'channel'],
 'shape': (480, 640, 3),
 'video_info': {'has_audio': False,
                'video.codec': 'av1',
                'video.fps': 50.0,
                'video.is_depth_map': False,
                'video.pix_fmt': 'yuv420p'}}
(480, 640, 3)
Resolving data files: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 85/85 [00:00<00:00, 64075.46it/s]

dataset[0][camera_key].shape=torch.Size([4, 3, 480, 640])
dataset[0]['observation.state'].shape=torch.Size([6, 14])
dataset[0]['action'].shape=torch.Size([64, 14])

batch[camera_key].shape=torch.Size([32, 4, 3, 480, 640])
batch['observation.state'].shape=torch.Size([32, 6, 14])
batch['action'].shape=torch.Size([32, 64, 14])



```

from that demo:

```
# Let's take this one for this example
repo_id = "lerobot/aloha_mobile_cabinet"
```


