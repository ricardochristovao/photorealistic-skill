# Defect checklist

Review every variant at 100% zoom. An image passes only if no item below fails. For each defect: how to prevent it in the prompt, and how to fix it after generation.

## People

| Check | What fails | Prevent | Fix |
|---|---|---|---|
| Hands | Extra/missing/fused fingers, bent the wrong way, two left hands, fingers merging into objects | One simple hand task; "relaxed hand, five fingers"; avoid interlaced fingers and hand-on-face | Inpaint the hand region with "natural relaxed hand, five fingers"; or crop/hide the hand |
| Teeth | Too many, one uniform white bar, misaligned midline | Closed-mouth or slight smile; "natural teeth, slightly uneven" | Inpaint mouth; or pick another variant |
| Eyes | Different iris shapes or sizes, pupils pointing different ways, catchlights that don't match the light | Three-quarter view; name the light source | Inpaint eyes with "matching eyes looking at [target]" |
| Ears & jewelry | Different ear shapes, mismatched earrings, glasses arms melting into hair | Avoid jewelry and glasses unless needed | Inpaint one side to match the other |
| Hair edges | Hair dissolving into background, halo outline, painted look | Avoid busy backgrounds behind hair; no rim light | Inpaint edge region; degrade step softens halos |
| Skin | Plastic, waxy, embossed wrinkles, crunchy pores (HDR) | Age-appropriate brief skin description; avoid "detailed skin" overload | Degrade step; lower `--strength` if pores turn to noise |
| Body proportions | Long necks, tiny heads, arms of different lengths, impossible posture | Simple poses; "weight on one leg" style natural posture | Regenerate; crop |
| Clothing | Buttons on both sides, collars that don't connect, logos as gibberish, seams that vanish | Plain clothing; "no logos" | Inpaint the area |
| Background people | Melted faces, duplicated people, limbs without owners | Keep crowds far, out of focus, cut by frame | Inpaint or blur the region; crop |
| Expression | Same frozen stock smile across variants | Mid-action expression ("mid-sentence", "half laughing") | Regenerate |

## Scene

| Check | What fails | Prevent | Fix |
|---|---|---|---|
| Text | Gibberish, misspelling, duplicated words, wrong font weights | Avoid text; if needed, short, quoted, "appears once" | Inpaint, or remove and add text in design software |
| Straight lines | Door frames, windows, tables, shelves bending or not meeting | Simple architecture; don't ask for ultra-wide | Inpaint; crop |
| Perspective / focal planes | Subject sharp, front and back equally blurred (cutout) | Describe distance and focal planes | Rewrite prompt |
| Light consistency | Light with no source, shadows in different directions, face lit from one side and body from another | Name the real light sources | Rewrite prompt |
| Reflections | Mirrors, windows, glasses, glossy objects reflecting the wrong thing or nothing | Avoid mirrors; matte objects | Inpaint; crop |
| Object logic | Chairs with 3 legs, cups without handles merging into hands, floating objects, repeated identical objects | Fewer, larger props | Inpaint or erase |
| Repetition | Same face, plant, or object copy-pasted across the frame | Vary descriptions; fewer elements | Inpaint one copy |
| Scale | Objects too big or small relative to people | Mention size when it matters | Regenerate |
| Too perfect | Perfect symmetry, centered subject, spotless surfaces | Capture flaws + ordinary clutter | Regenerate or crop off-center |

## Finish

| Check | What fails | Fix |
|---|---|---|
| Sharpness | Everything crisp to the pixel, edges with halos | `degrade.py` |
| Contrast | HDR look, glowing midtones | `degrade.py` |
| Color | Oversaturated, teal-orange grade | `degrade.py`; prompt for mixed, slightly wrong white balance |
| Noise | Perfectly clean shadows at night/indoors | `degrade.py --preset event` |
| Resolution | Upscaled after degrading, render look returns | Upscale first, degrade last, export at final size |
