# Contributing to Photorealistic Skill

Thanks for your interest in contributing! This project thrives on community knowledge about what makes AI images look real (or fake).

## How to contribute

### New genre entries

Found a capture situation not covered in `references/genres.md`? Open a PR adding a row to the table with: genre sentence, camera/position, DOF, light, typical flaws, and matching degrade preset. Include at least one example prompt in `references/examples.md`.

### Model-specific tips

If you've discovered a setting, workflow, or gotcha for a specific image model that isn't in `references/models.md`, add it under the appropriate section. Cite the model version and date — these change fast.

### Example prompts

Add complete examples to `references/examples.md` following the existing format: request → planning decisions → full prompt → preset. Real-world requests are more valuable than synthetic ones.

### Defect checklist additions

Found a failure mode not in `references/defects.md`? Add it to the appropriate table with prevention and fix columns filled in.

### `degrade.py` improvements

New presets, better default parameters, performance improvements, or support for additional image formats are all welcome. Keep the script dependency-light (Pillow + NumPy only).

### Translations

The README is bilingual (English/Portuguese). If you want to add another language or improve an existing translation, go ahead.

## Guidelines

- Keep prose concise and practical. No filler.
- Test prompts against at least two different models before submitting.
- For `degrade.py` changes, include before/after sample images in the PR description.
- One concern per PR when possible.
- MIT license applies to all contributions.

## Questions?

Open an issue or reach out via [LinkedIn](https://www.linkedin.com/in/ricardochristovao/).