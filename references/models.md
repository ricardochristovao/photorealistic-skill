# Model notes

Model names, versions and parameters change often. Check the current docs of the tool when something below doesn't match.

## General

- Natural-language models (Nano Banana / Gemini image, GPT image, Seedream, Flux) respond best to full descriptive sentences. Write the prompt as a paragraph, not a tag list.
- Tag-style models (Stable Diffusion family) need shorter phrases and a separate negative prompt field.
- When the request involves a **specific existing person or an image to recreate**, always pass that image as a reference and say "same person as the reference (same face, hair, …)". Text alone won't keep identity.
- When the request is **text-to-image with no reference**, pick a model known for photographic output and avoid design/typography-oriented models.
- Generate 2-4 variants per call. Change the prompt, not just the seed, if all variants share the same defect.

## Per tool

**Magnific (MCP)**
- With a reference image: `imagen-nano-banana-2` (Nano Banana Pro) or `seedream-5-pro`, reference `type: image`, `count: 2-4`, resolution 2k.
- Without reference: `seedream-5-pro` or `recraft-v4-1`.
- Avoid the GPT design family for photos (`agentRecommendation` lists it as non-photorealistic design).
- Local fixes: `images_retouch` with a mask (white = change). Edge cleanup: `images_crop`. Don't use `images_upscale` after degrading; upscale first if needed.
- Upload local files with `creations_request_upload` → PUT bytes → `creations_finalize_upload`. Download results via `creations_wait` URLs, then run `degrade.py`.

**Midjourney**
- Use `--style raw` and a low `--stylize` (roughly 0-100) to reduce the model's own aesthetic.
- Use `--no` for 3-5 exclusions instead of writing them in the prompt.
- Aspect ratio via `--ar`. Use character/omni reference features for a specific person.

**Flux**
- No negative prompt support in most setups; phrase everything positively ("matte skin with normal shine on the nose" instead of "no plastic skin").
- Lower guidance values tend to look less "rendered".

**Nano Banana / Gemini image**
- Very good at following edit instructions on a reference ("keep everything, change only X").
- Negatives must be written inside the prompt as short "not X" phrases at the end.
- Tends to render text well, but still check for duplicated words.

**GPT image**
- Strong at text and layout, tends to a polished commercial finish. Lean harder on genre, capture flaws and the degrade step.

**Stable Diffusion family**
- Use the negative field for: plastic skin, airbrushed, extra fingers, deformed hands, oversaturated, HDR, cartoon, 3d render.
- Moderate CFG; very high CFG increases the over-processed look.
- Use inpainting with a photo-trained checkpoint for hand/face fixes.
