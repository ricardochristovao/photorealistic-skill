<div align="center">

# 📸 Photorealistic Skill

### Make AI-generated images indistinguishable from real photographs

**A systematic framework + post-processing toolkit that eliminates the "AI look" — works with Midjourney, Flux, DALL-E, Stable Diffusion, Seedream, and any image model.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](scripts/degrade.py)
[![GitHub Stars](https://img.shields.io/github/stars/ricardochristovao/photorealistic-skill?style=social)](https://github.com/ricardochristovao/photorealistic-skill/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/ricardochristovao/photorealistic-skill?style=social)](https://github.com/ricardochristovao/photorealistic-skill/network/members)

[🌐 Website](https://bychr.com.br/ia/skills/photorealistic/) · [👤 About the Author](https://bychr.com.br/eu/) · [💼 LinkedIn](https://www.linkedin.com/in/ricardochristovao/) · [🐙 GitHub](https://github.com/ricardochristovao/)

**English** | [Português](#português)

</div>

---

## Why AI images look fake (and how to fix it)

Most people try to fix AI images by adding more adjectives: *"85mm f/1.4, golden hour, Portra 400, cinematic, hyperrealistic."* This makes it **worse**. That polished, creamy-bokeh, rim-lit aesthetic *is* the AI look. Real photos come from situations, not gear lists.

Photorealistic Skill replaces guesswork with a **repeatable 4-step system**:

```
Plan a scene the model can't get wrong
        ↓
Prompt it like a real capture (not a render)
        ↓
Review for structural defects & fix locally
        ↓
Degrade the render finish (mandatory post-processing)
```

Skip any step and the image slips through. Do all four and it passes as a real photo.

## What's inside

| File | Purpose |
|------|---------|
| [`SKILL.md`](SKILL.md) | Complete 4-step methodology — the core of the system |
| [`references/genres.md`](references/genres.md) | 12 capture genres with camera settings, DOF, lighting & presets |
| [`references/examples.md`](references/examples.md) | Full prompt examples across genres (phone, office, event, portrait, product, food) |
| [`references/defects.md`](references/defects.md) | Defect checklist: hands, teeth, eyes, text, shadows, reflections + prevention & fixes |
| [`references/models.md`](references/models.md) | Model-specific notes: Midjourney, Flux, DALL-E, SD, Magnific, Nano Banana |
| [`scripts/degrade.py`](scripts/degrade.py) | Python script that removes the AI render finish in one command |

## Quick start

### As a Claude Desktop skill (native integration)

Photorealistic Skill was **designed to work natively inside Claude Desktop**. Copy the `photorealistic-skill/` folder into your Claude Desktop skills directory or install via plugin. Once installed, Claude automatically follows the full 4-step methodology whenever you ask for a realistic photo — no manual prompting needed.

The skill auto-triggers on requests like *"foto real"*, *"realista"*, *"não parecer IA"*, *"looks fake"*, *"AI artifacts"*, *"photorealistic"*, or any request for a photo of a person or real-world scene. Claude will plan the scene, write the prompt following the genre system, review against the defect checklist, and remind you to run `degrade.py` as the mandatory finishing step.

Works with Claude's built-in image generation tools (Magnific, Nano Banana, Seedream) and can guide prompts for external models too.

### Standalone (any AI image tool)

Follow the 4 steps in [`SKILL.md`](SKILL.md) manually, then run the finishing script:

```bash
pip install Pillow numpy

python scripts/degrade.py input.png output.jpg \
  --width 1200 --height 675 \
  --preset phone \
  --strength 1.0
```

### Presets

| Preset | Best for |
|--------|----------|
| `event` | Indoor events, stages, night, high-ISO situations |
| `phone` | Everyday snapshots, social posts, UGC, testimonials |
| `portrait` | Editorial/professional portraits, office, founder photos |
| `daylight` | Outdoor daytime, street, travel, products in use |
| `film` | Genuine analog looks (named film stock in prompt) |

Adjust `--strength`: **1.4** if still too clean, **0.7** if muddy.

### Without Python

Apply equivalent adjustments in Lightroom / Camera Raw: Texture −20, Clarity −15, Dehaze −5, Saturation −10, Vibrance −5, Grain 20–30 (size 25, roughness 50), light vignette −8, export JPEG quality ~80 at final size.

## How it works (the short version)

**Step 1 — Plan.** Pick a capture genre from [`genres.md`](references/genres.md). Simplify what the model must render: give hands one simple job, limit people to 1–3 sharp subjects, avoid complex text, choose light sources that actually exist in the scene.

**Step 2 — Prompt.** Open with the genre in plain words (*"A casual phone photo a friend took at a birthday dinner"*), not a gear list. Describe focal planes explicitly. Add 2–4 capture flaws (slight tilt, off-center, blown highlight, mixed WB). End with 4–6 short "not" items. See [`examples.md`](references/examples.md) for complete prompts.

**Step 3 — Review.** Download full-size. Zoom to 100% on faces, hands, text, background. Run the [`defects.md`](references/defects.md) checklist. Pick the variant with fewest *structural* defects. Inpaint local issues; rewrite the prompt for global ones.

**Step 4 — Degrade.** Every model's output is too clean. Run `degrade.py` at the **final output size**. This applies softening, anti-clarity, desaturation, WB shift, black lift, highlight roll-off, luminance noise, chroma noise, vignette, and a JPEG round-trip. Upscale *before* degrading, never after.

## Common mistakes

| Mistake | Result | Fix |
|---------|--------|-----|
| Same "camera + film + golden hour" recipe for everything | Stock/cinema look, cutout background | Start from the genre in `genres.md` |
| Asking for "shallow DOF" without distance | Physically impossible blur | Describe distance and focal planes |
| Light that doesn't exist in the location | Looks composited | Name real light sources in the scene |
| Complex hands, crowds, lots of text | Melted fingers, distorted faces, gibberish | Simplify the scene *before* prompting |
| Only skin imperfections | Real face inside a perfect render | Add capture flaws to the prompt |
| Fixing everything with more adjectives | Longer prompt, same defects | Simplify scene, inpaint locally, or change model |
| Judging from thumbnails | Defects slip through | Always review at 100% zoom |
| Delivering raw model output | HDR/over-sharp finish gives it away | **Always** run Step 4 |

## Compatible models

Photorealistic Skill is model-agnostic. Specific notes for each:

- **Midjourney** — `--style raw`, low `--stylize` (0–100), `--no` for exclusions
- **Flux** — No negative prompt; phrase everything positively; lower guidance
- **DALL-E / GPT Image** — Strong at text/layout; lean harder on genre + degrade step
- **Stable Diffusion** — Use negative field; moderate CFG; inpaint with photo checkpoint
- **Magnific / Nano Banana / Seedream** — See [`models.md`](references/models.md) for MCP workflow

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. Ideas: new genre entries, model-specific tips, additional example prompts, translations, improvements to `degrade.py`.

## License

MIT — see [LICENSE](LICENSE).

## Author

**Ricardo Christovão da Silva (ByCHR)**
[Website](https://bychr.com.br/eu/) · [LinkedIn](https://www.linkedin.com/in/ricardochristovao/) · [GitHub](https://github.com/ricardochristovao/)

If this project helped you generate better images, consider giving it a ⭐ — it helps others find it too.

---

<div align="center">

<a name="português"></a>

## 🇧🇷 Português

### Faça imagens geradas por IA serem indistinguíveis de fotografias reais

**Um framework sistemático + toolkit de pós-processamento que elimina a "cara de IA" — funciona com Midjourney, Flux, DALL-E, Stable Diffusion, Seedream e qualquer modelo de imagem.**

### Por que imagens de IA parecem falsas

A maioria das pessoas tenta corrigir adicionando mais adjetivos: *"85mm f/1.4, golden hour, Portra 400, cinematic, hiper-realista."* Isso **piora**. Essa estética polida, com bokeh cremoso e rim light *é* a cara de IA. Fotos reais vêm de situações, não de listas de equipamento.

Photorealistic Skill substitui tentativa e erro por um **sistema repetível de 4 passos**: planejar cena → promptar como captura real → revisar defeitos → degradar acabamento.

### Como usar

Siga os 4 passos do [`SKILL.md`](SKILL.md) e rode o script de finalização:

```bash
pip install Pillow numpy
python scripts/degrade.py entrada.png saida.jpg --width 1200 --height 675 --preset phone
```

Consulte [`references/genres.md`](references/genres.md) para gêneros, [`references/examples.md`](references/examples.md) para prompts prontos e [`references/defects.md`](references/defects.md) para o checklist de revisão.

### Autor

**Ricardo Christovão da Silva (ByCHR)**
[Site](https://bychr.com.br/eu/) · [LinkedIn](https://www.linkedin.com/in/ricardochristovao/) · [GitHub](https://github.com/ricardochristovao/)

Se este projeto te ajudou a gerar imagens melhores, considere dar uma ⭐ — ajuda outros a encontrarem também.

</div>
