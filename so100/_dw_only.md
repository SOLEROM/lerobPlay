# 2_dw_only


lerobot/2_dw_only.py

```
from lerobot.common.policies.diffusion.modeling_diffusion import DiffusionPolicy

# Choose the Hugging Face repo ID or local path
pretrained_policy_path = "../../diffusion_pusht/"

# Download and cache locally
policy = DiffusionPolicy.from_pretrained(pretrained_policy_path)

# Print confirmation and where it’s stored
print("✅ Policy downloaded and initialized:")

```

