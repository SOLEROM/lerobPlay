# refactors

# fix for cpu

/examples/2_evaluate_pretrained_policy.py

-device = "cuda"
+device = "cuda" if torch.cuda.is_available() else "cpu"
+print(f"Using device: {device}")
