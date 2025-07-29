# Evaluate a pretrained policy


## 

python examples/2_evaluate_pretrained_policy.py 






## run2
pretrained model hosted on lerobot/diffusion_pusht:


```
python -m lerobot.scripts.eval \
    --policy.path=../diffusion_pusht \
    --env.type=pusht \
    --eval.batch_size=10 \
    --eval.n_episodes=10 \
    --policy.use_amp=false \
    --policy.device=cuda


    Stepping through eval batches: 100%|█| 1/1 [41:07<00:00, 2467.12s/it, running_success_rate=70.
{'avg_sum_reward': 110.80743191158619, 'avg_max_reward': 0.9658180733000201, 'pc_success': 70.0, 'eval_s': 2471.8305881023407, 'eval_ep_s': 247.1830590724945}
INFO 2025-07-26 23:12:35 pts/eval.py:501 End of eval

```