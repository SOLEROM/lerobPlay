# Policy

A policy is an algorithm or logic that uses one or more models to decide actions for the robot.

It wraps the model, preprocessing, postprocessing, and decision rules (e.g., ACT, DiffusionPolicy, etc.).

In lerobot, policy classes are implemented like ACTPolicy, DiffusionPolicy, etc

* compare 
```
model	Trained neural network weights	model.safetensors, config.json	Inside a p
policy	Full logic to produce actions	Uses one or more models	For inference or training
```


## examples

Diffusion Policy (policy)
A policy architecture that uses a diffusion-based model trained on the Push-T dataset.
It generates smooth, temporally coherent actions for pushing objects.

VQ-BeT (policy)
A policy that leverages a Vector Quantized Behavior Transformer model trained on Push-T.
It serves the same task as Diffusion Policy but with a different model architecture for comparison.

ACT (policy)
A policy designed for high-precision manipulation (e.g., inserting or grasping small items).
It uses a transformer-based model trained to handle fine motor control in robot arms.



# repos

pingev/lerobot-so100-1
