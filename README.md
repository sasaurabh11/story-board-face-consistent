# Same face with diffrent scenario

![Face Consistent Sample](/public/demo.jpeg)


## Features

- Character-aware `FluxPipeline` wrapper (`CharaConsistPipeline`) with prompt encoding, latent prep, and denoising orchestration.
- Drop-in attention processors that save/reuse foreground/background attention banks, cross-image similarity maps, and adaptive interpolation.
- Utilities for resetting attention state, resizing feature maps, cleaning masks, and running pre-pass “ID” stages.
- Example notebook (`main.ipynb`) for ad‑hoc experiments.

## Repository Layout

- `models/pipeline_characonsist.py` – main pipeline entry point with inference loop modifiers (spatial kwargs, interpolation schedules, etc.).
- `models/atteention_processor.py` – custom attention processors, mask utilities, and helper functions for the pipeline.
- `main.ipynb` – scratch notebook (rename or duplicate for your own experiments).

## Getting Started

1. **Create environment**
   ```bash
   conda create -n face-consistent python=3.10
   conda activate face-consistent
   ```
2. **Install dependencies**
   ```bash
   pip install torch diffusers transformers accelerate einops numpy opencv-python tqdm
   ```
   Adjust the PyTorch build (CUDA vs CPU) per your hardware.

## Usage

```python
from diffusers import AutoencoderKL, FluxPipeline
from models.pipeline_characonsist import CharaConsistPipeline
from models.atteention_processor import reset_attn_processor, set_text_len, reset_size

pipe = CharaConsistPipeline.from_pretrained(
    "black-forest-labs/FLUX.1-dev",
    torch_dtype=torch.bfloat16,
).to("cuda")

reset_attn_processor(pipe, size=(64, 64))

images = pipe(
    prompt="portrait of a smiling traveler, cinematic lighting",
    spatial_kwargs={"id_fg_mask": None, "curr_fg_mask": None},
    share_bg=True,
    use_interpolate=True,
)[0]
images[0].save("traveler.png")
```

- Run an **ID pass** (`is_id=True`) to capture foreground/background masks, then reuse them in subsequent calls (`is_pre_run` / default).
- Tune `attn_start_step`, `attn_end_step`, and interpolation parameters for the desired level of identity strictness vs. diversity.
- Use `reset_id_bank`, `reset_size`, and `set_text_len` when switching prompts, aspect ratios, or batching strategy.

## Image Preview

  ```markdown
  ![Face Consistent Sample](/public/demo2.png)
  ```



