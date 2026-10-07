---
name: photorealistic-prompt
description: Use whenever an AI-generated image must pass as a real photograph — people, portraits, candids, events, offices, families, food, products in use, interiors, streets, testimonials, ads, social posts, email/landing-page photos. Also use to fix or recreate an image that "looks AI". Triggers on "foto real", "realista", "não parecer IA", "tá muito IA", "parece fake", "pele de plástico", "mão estranha", "dedos errados", "fundo recortado", "photorealistic", "real photo", "looks fake", "AI artifacts", or any request to generate a photo of a person or real-world scene, even if realism isn't mentioned. Works with any image model (Magnific, Nano Banana, Seedream, Flux, Midjourney, GPT, Stable Diffusion). Covers scene planning, the prompt, model settings, defect review, fixes, and a mandatory finishing step.
---

# Photorealistic Prompt

Goal: every image generated with this skill should look like a photo someone actually took, with none of the usual AI failures.

No prompt guarantees that on its own. Realism comes from four steps done every time:
**plan a scene the model can't get wrong → prompt it like a real capture → review for defects and fix → degrade the render finish.**
Skipping any step is how AI images slip through.

## Why AI images look fake

1. **Wrong photographic genre.** Stacking "85mm f/1.4, golden hour, Portra 400, cinematic" pulls the model toward stock/cinema imagery: creamy bokeh, rim light, glossy skin. That polish *is* the AI look. Real photos come from a situation (a phone at dinner, an event photographer in the audience, a colleague snapping a candid).
2. **Impossible physics.** Subject razor-sharp while front and back are equally melted (cutout look); light from no visible source; shadows in different directions; reflections that don't match.
3. **Structural defects.** Hands, teeth, eyes, text, jewelry, background faces, straight lines. The model fails most where detail is small, repeated or interacting.
4. **Render finish.** Over-sharpening, HDR micro-contrast, saturated color, noise-free shadows. Prompts don't remove it reliably; post-processing does.

## Step 1 — Plan a scene that is hard to get wrong

Before writing the prompt, simplify what the model must render. Most "loucuras" come from asking for things models are bad at.

- **Pick the capture situation** from `references/genres.md`. It fixes lens, distance, depth of field, light and typical flaws. If unsure: event/candid → "event", everyday life → "phone snapshot", work → "office candid".
- **Hands:** give them one simple job (holding a cup, resting on a table, in a pocket). Avoid interlaced fingers, hands touching faces, hands gripping complex objects, people holding hands, counting gestures.
- **People count:** 1-3 sharp people. Crowds only far away or out of focus, and partially cut by the frame.
- **Text:** only when required. Short (1-4 words), large, quoted exactly, said to appear once. Otherwise ask for "no readable text" and add the text later in design.
- **Faces:** three-quarter view and mid-action expressions are more forgiving than straight-on symmetrical smiles. Teeth: a slight or closed-mouth smile has fewer errors than a big grin.
- **Objects:** prefer fewer, larger props. Glasses, earrings, jewelry, keyboards, bicycles, musical instruments, chess boards and fences are failure magnets; use only if needed.
- **Light:** must come from sources that exist in the scene. Golden hour indoors on a stage, or studio light in a kitchen, reads as composited.

## Step 2 — Write the prompt

Order:

```
[GENRE SENTENCE] → [SUBJECT + ACTION, caught mid-moment] → [CAMERA: device, position, distance, lens, settings]
→ [FOCAL PLANES: what is sharp / slightly soft / blurred] → [LIGHT: real sources in the scene + their flaws]
→ [ENVIRONMENT with ordinary clutter] → [CAPTURE FLAWS] → [SKIN, HANDS, TEXT — brief and specific]
→ [4-6 short "not" items]
```

Rules:

- **Open with the genre in plain words.** "A phone photo a friend took at a birthday dinner" beats any list of gear.
- **Camera matches the genre.** Phone genres → "shot on a phone". Pro genres → one body + lens + aperture + ISO that make sense together. Don't name gear just to sound real.
- **Describe focal planes explicitly.** Distance and focal length decide blur. E.g. "phone photo, everything from the table to the back wall is in focus" or "she and the bookshelf two meters behind her are both readable, the shelf only slightly soft".
- **Put imperfection in the capture, not only the skin.** Pick 2-4: slight tilt, off-center subject, someone cut by the frame, a highlight slightly blown, mild motion blur on a moving hand, high-ISO noise, mixed white balance, a stray object in the foreground.
- **Ordinary clutter.** One or two mundane objects that nobody would place for a photo: a charger cable, a crumpled napkin, a parked scooter.
- **Skin, briefly and age-appropriate:** "normal skin for a 40-year-old: pores, slight shine on the nose, uneven tone". Not a paragraph.
- **Hands, briefly:** "relaxed hand, five fingers, natural knuckles". Long anatomical lists don't help.
- **Avoid trigger words:** cinematic, dramatic, epic, stunning, gorgeous, perfect, flawless, masterpiece, 8k, ultra-detailed, hyperrealistic, award-winning, studio, rim light, bokeh (as a goal), HDR, octane, unreal engine.
- **Film stock names** only for genres that are actually analog. For digital genres, describe digital traits instead.
- **Negatives:** a few, at the end, phrased as short "not X" items. Long negative lists get ignored or inverted on many models.

Model-specific settings are in `references/models.md` (Midjourney raw style, low stylize, Flux/Nano Banana not supporting negatives, using references for real people, etc.).

**Always generate 2-4 variants.** One seed tells you nothing.

## Step 3 — Review and fix

Download the full-size results. Look at the whole frame, then crop to 100% on faces, hands, text and the background. Go through the checklist in `references/defects.md` (hands, teeth, eyes, ears/jewelry, hair edges, text, background people, straight lines, shadows, reflections, clothing, object logic).

Then:
- **Pick the variant with the fewest structural defects**, not the prettiest one.
- **Local defect** (one hand, a bad ear, an extra object, garbled text) → inpaint/retouch only that region with a short prompt, or crop it out if it's at the edge.
- **Global defect** (cutout background, wrong light, impossible perspective) → rewrite the prompt; inpainting won't fix physics.
- **Everything fails the same way** → simplify the scene (Step 1), don't add more adjectives.

Never deliver an image that fails any checklist item.

## Step 4 — Degrade the finish (mandatory)

Every model's output is too clean. Run:

```bash
python scripts/degrade.py input.png output.jpg --width W --height H --preset PRESET [--strength 1.0]
```

| Preset | Use for |
|---|---|
| `event` | Indoor events, stages, night, any high-ISO situation |
| `phone` | Everyday snapshots, social posts, UGC, testimonials |
| `portrait` | Editorial/professional portraits, office, founder photos |
| `daylight` | Outdoor daytime, street, travel, products in use outside |
| `film` | Genuinely analog looks (named film stock in the prompt) |

The script downsamples and softens, lowers local contrast, desaturates slightly, adds a small white-balance error, lifts blacks, rolls off highlights, adds shadow-weighted luminance noise and a touch of chroma noise, a light vignette, and a JPEG round trip.

After running it, view the output and a face crop. Still too clean → `--strength 1.4`. Muddy → `--strength 0.7`.

**Export at the final size it will be used.** Upscaling an AI image afterwards brings the render look back; if a bigger file is needed, upscale first and degrade last.

If Python isn't available, apply the equivalent manually in Lightroom/Camera Raw: Texture −20, Clarity −15, Dehaze −5, Saturation −10, Vibrance −5, Grain 20-30 (size 25, roughness 50), slight vignette −8, export JPEG quality ~80 at final size.

## Examples

See `references/examples.md` for complete prompts across genres (phone snapshot, office candid, event stage, outdoor portrait, product in use, food at a restaurant), each with its preset.

## Common mistakes

| Mistake | Result | Fix |
|---|---|---|
| Same "camera + film + golden hour" recipe for everything | Stock/cinema look, cutout background | Start from the genre in `references/genres.md` |
| Asking for "shallow depth of field" without distance | Physically impossible blur | Describe distance and focal planes |
| Light that doesn't exist in the location | Looks composited | Name the real light sources in the scene |
| Complex hands, crowds, lots of text | Melted fingers, distorted faces, gibberish | Simplify the scene before prompting |
| Only skin imperfections | Real face inside a perfect render | Add capture flaws |
| Fixing everything with more adjectives | Longer prompt, same defects | Simplify scene, inpaint locally, or change model |
| Judging from thumbnails | Defects slip through | Review at 100% with the checklist |
| Delivering raw model output | HDR/over-sharp finish gives it away | Always run Step 4 |
