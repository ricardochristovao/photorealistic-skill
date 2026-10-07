# Releases

## v1.0.0 — Initial Release (2026-10-07)

### What's included

- **Complete 4-step methodology** (`SKILL.md`): scene planning → capture-style prompting → defect review → render finish degradation
- **12 capture genres** (`references/genres.md`): phone snapshot, selfie, event/stage, office candid, editorial portrait, outdoor daylight, golden hour, food/restaurant, product in use, interior/real estate, analog film, night/low light — each with camera settings, DOF, lighting, typical flaws, and matching degrade preset
- **Full prompt examples** (`references/examples.md`): family dinner, office candid, conference stage, golden hour portrait, product in real use, recreating an existing AI image
- **Defect checklist** (`references/defects.md`): hands, teeth, eyes, ears/jewelry, hair edges, skin, body proportions, clothing, background people, expression, text, straight lines, perspective, light consistency, reflections, object logic, repetition, scale, finish — with prevention and fix for each
- **Model-specific notes** (`references/models.md`): Midjourney, Flux, DALL-E/GPT Image, Stable Diffusion, Magnific/Nano Banana/Seedream
- **`degrade.py` script**: one-command post-processing that removes the AI render finish with 5 presets (`event`, `phone`, `portrait`, `daylight`, `film`) and adjustable strength
- **Bilingual README** (English + Português)
- **MIT License**

### Why this exists

AI image models produce output that is too clean, too polished, and structurally inconsistent with real photography. Adding more adjectives to the prompt makes it worse. This project provides a systematic, repeatable process that works across any model to produce images that pass as real photographs.

### Compatibility

Works with any AI image generation model: Midjourney, Flux, DALL-E, GPT Image, Stable Diffusion, Seedream, Nano Banana, Magnific, and others.