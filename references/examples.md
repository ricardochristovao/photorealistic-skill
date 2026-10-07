# Examples

Each example shows the request, the planning decisions (Step 1), the prompt (Step 2) and the finishing preset (Step 4). Prompts are written for natural-language models; for tag-style models, shorten into phrases and move the "not" items to the negative field.

---

## 1. Phone snapshot — family dinner

**Request:** "Foto de uma família jantando em casa, bem natural"

**Planning:** genre phone snapshot; 4 people but only 2 fully in frame, others partly cut; hands on cutlery or glass only; no text.

> A casual phone photo someone took across the table during a weeknight family dinner at home. A woman in her forties laughing at something off-camera while holding a glass of water, a teenage boy next to her looking at his plate, an older man's shoulder and arm cut by the left edge of the frame. Shot on a phone from a seated position about 1.5 meters away, everything from the plates to the kitchen cabinets behind is in focus. Light from a warm ceiling lamp above the table and a cooler window on the right, slightly mixed white balance, the lamp area a bit overexposed. Ordinary table: half-eaten rice and beans, a crumpled napkin, a phone face down, a bottle of hot sauce. Frame slightly tilted, the woman off-center. Normal skin, slight shine on foreheads. Relaxed hands with five fingers. Not posed, not a stock photo, not glossy, not HDR.

**Preset:** `phone`

---

## 2. Office candid

**Request:** "Mulher trabalhando no notebook, foto pra site de empresa"

**Planning:** genre office candid; one person; hands resting on keyboard edge (not typing detail); screen shows nothing readable.

> A candid photo a colleague took in a small, slightly messy office. A woman in her mid-thirties sitting at a desk, mid-sentence on a video call, one hand resting near the laptop, the other holding a pen. Taken from about 3 meters away with a 35mm lens at f/2.8; the bookshelf and window behind her are clearly readable, only slightly soft. Daylight from a window on the left and cool overhead LED panels, faint green cast on the wall. On the desk: a coffee mug with a stain ring, a charger cable, sticky notes, a water bottle. The laptop screen shows a blurry video call, no readable text. She is off-center to the right, her chair partly cut by the bottom edge. Normal skin for her age, a few flyaway hairs. Five fingers, natural knuckles. Not posed, not a stock photo, not cinematic, no rim light.

**Preset:** `portrait`

---

## 3. Event stage

**Request:** "Palestrante no palco de um congresso"

**Planning:** genre event; photographer in the audience with a telephoto; screen with no text (text added later in design); audience heads cut at bottom.

> An ordinary photo from a medical conference, the kind the event photographer uploads to the album. A man in his fifties in a gray suit speaking on stage, one hand gesturing mid-sentence, the other holding a clicker. Shot from the audience about 12 meters away with a 70-200mm zoom at f/2.8, ISO 5000: compressed perspective, the speaker and the projection screen behind him are almost on the same focal plane, the screen only slightly soft. The screen shows a blue slide with a simple chart and no readable text. A hard spot from above, a little too bright on his forehead, cool spill from the screen on his suit. Dark ceiling with lighting truss, some high-ISO noise. Three audience heads and a raised phone at the bottom edge, mildly out of focus. Horizon tilted about 2 degrees. Not glossy, not HDR, no rim light, no lens flare.

**Preset:** `event`

---

## 4. Outdoor portrait at golden hour

**Request:** "Retrato de um homem no campo ao pôr do sol"

**Planning:** genre golden hour outdoor (light actually exists); one person; hands in pockets.

> A photo taken outdoors just before sunset on a farm, a man in his sixties in a worn denim jacket standing by a wooden fence, hands in his pockets, squinting slightly at the sun. Shot with a 50mm lens at f/2.8 from about 3 meters; the field and a distant tree line behind him are soft but clearly recognizable. Low sun from the right and slightly behind, warm light on one side of his face, the other side in open shade; a few stray hairs glowing. Dust in the air, uneven grass, a bucket near the fence post. Weathered skin, sun spots, deep lines around the eyes, gray stubble. Slightly off-center composition. Not cinematic, not oversaturated, not retouched.

**Preset:** `daylight`

---

## 5. Product in real use

**Request:** "Foto de uma garrafa térmica sendo usada, estilo cliente real"

**Planning:** genre product in use; product large in frame; one hand holding it with a simple grip; label text avoided (add brand later) or described minimally.

> A real customer photo of a matte black stainless steel thermos bottle on a kitchen counter in the morning, a hand pouring coffee from it into a chipped ceramic mug. Shot on a phone from about 60 cm, slightly from above, everything in focus. Daylight from a window behind, the window area slightly overexposed. Counter has crumbs, a spoon, a cable from a toaster. The thermos has small scratches and fingerprints, no readable label. Relaxed hand with five fingers, natural nails. Not a studio product shot, not glossy, not CGI.

**Preset:** `phone`

---

## 6. Recreating an existing AI image

**Request:** "Essa foto ficou com cara de IA, recria parecendo real" (image attached)

**Planning:** upload the image, pass it as reference; identify the genre from what the image shows; list what to keep (identity, clothing, main action, required text) and what to change (optics, light, finish).

> [Genre sentence matching the scene]. Same person as the reference (same face, hair, clothing) doing [the same action]. [Camera position, distance, lens, settings from the genre]. [Focal planes]. [Light from real sources in the scene, with flaws]. [Required text, quoted, once]. [Capture flaws]. [Brief skin and hands]. Not glossy, not HDR, not retouched, not over-sharpened, no rim light.

**Then:** review all variants at 100%, discard any with duplicated text or bad hands, run `degrade.py` with the genre's preset at the exact size the original occupied.
