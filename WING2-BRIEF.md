# FABLE 25 — Wing II brief (sites 26–50)

Wing I (sites 01–25, already live) was a deliberate zero-binary-asset flex — everything
procedural. Wing II is the counterpart: it embraces the generated-imagery pipeline the
master guide explicitly called out as the alternative path — Higgsfield-generated stills
(nano_banana_pro, ~2cr/1k image) as key hero assets, Higgsfield-animated motion where it
earns its cost, and real WebGL/Three.js 3D. This is the "go nuts, show the range" half.

**Non-negotiables, inherited from Wing I and the owner's brief:**
- Every site is one self-contained `index.html` (inline CSS/JS) + `guide/index.html`,
  same template/nav pattern as `sites/25-resonance/` — copy that structure.
- One display font per site, distinct from all other 49 sites where possible.
- One signature technique executed deeply, not five gimmicks.
- Real accessibility floor: semantic headings, keyboard paths, `prefers-reduced-motion`
  fallback, contrast checked against actual rendered backgrounds.
- `prefers-reduced-motion` must also gracefully degrade any generated video/hero motion.
- Generated assets live in `sites/XX-name/assets/` and are referenced by relative path —
  no base64 bloat.
- Nav crumbs in guide pages: back to site, all sites (`../../`), master guide (`../../guide/`).
- **3 documented iteration passes per site** before sign-off (build pass, code-review pass,
  live-browser pass) — same discipline as Wing I, write what was found/fixed in the guide.
- Image generation model: `nano_banana_pro` unless a site's brief says otherwise. Always
  pass `get_cost:true` first if generating more than the one planned hero image.
- If a planned video/animation generation fails, is too expensive, or times out: fall back
  gracefully to the still image + CSS/canvas motion. Never block a site's completion on it.

Numbering continues 26–50. Accent hex per site should be visually distinct from the 25
already used in `sites/index.html` (see ACCENTS array there).

---

## 26 — AURORA (`26-aurora`)
Polar sky / atmospheric optics. **Asset:** one generated image, aurora borealis over dark
mountains, painterly/cinematic, teal-violet-green. **Technique:** image as fixed backdrop,
layered under a canvas/WebGL perlin-noise flow-field that paints *additional* moving aurora
ribbons in front of it — the generated image gives it richness a pure shader can't, the
shader gives it motion a photo can't. Dark palette, cold.

## 27 — TERRAZZO (`27-terrazzo`)
Playful stone-confetti material study. **Asset:** one generated macro terrazzo texture
(tileable-ish, bright chips in cream cement). **Technique:** the image tiles as a background;
foreground is a canvas generative terrazzo-chip scatter that responds to scroll/cursor,
chip colors sampled from the image. Bright, candy palette, big rounded geometric type.

## 28 — KINTSUGI (`28-kintsugi`)
Gold-repaired ceramics. **Asset:** one generated image of a cracked ceramic bowl/vessel,
moody studio lighting. **Technique:** SVG crack-line paths hand-placed over the image,
animated gold-gradient "repair" draws itself in on scroll/load. Deep indigo/charcoal bg,
gold accent, one serif display face evoking a museum placard.

## 29 — CREVASSE (`29-glacier`)
Glacial ice. **Asset:** one generated image, blue glacier ice crevasse, crystalline.
**Technique:** WebGL fragment shader refraction/caustics effect composited over the image
(image as texture sampled by the shader). Cold blue-white palette, thin geometric sans.

## 30 — MYCELIUM (`30-mycelium`)
Fungal network. **Asset:** one generated macro image, bioluminescent fungus/mycelium threads
in dark forest soil, glowing cyan-green. **Technique:** canvas recursive branching (L-system)
growth animation drawn *from* points sampled off the image's bright areas, so the generative
growth looks like it's emerging from the photo. Near-black bg, bioluminescent accent.

## 31 — RISO CLUB (`31-riso`)
Risograph zine. **Asset:** one generated illustration in a flat riso-print style (2-3 tone,
grainy, offset-registration look) — subject: your choice (a plant, a face, an object; pick
something that reads well duotone). **Technique:** CSS blend-mode layered duotone/tritone
recoloring of the image, halftone overlay, slight registration-wobble animation on hover.
Two-three flat riso inks (e.g. fluorescent pink + navy + cream), a grotesque display face.

## 32 — MODULAR (`32-oscilloscope`)
Synth/oscilloscope lab. **Asset:** try ONE short (4-6s) Higgsfield video loop of modular
synth patch cables / oscilloscope traces (get_cost first; if too expensive or it fails,
fall back to a single generated still of a eurorack synth close-up). **Technique:** the
video/image is the hero backdrop; foreground is a live canvas oscilloscope readout driven
by a small Web Audio synth the visitor can trigger (reuse/extend the polysynth idea from
25-resonance but make the *visual* different — Lissajous/XY scope curves, not rings). CRT
green/amber on black, monospace type.

## 33 — TESSERA (`33-tessera`)
Byzantine mosaic. **Asset:** one generated image, close-up gold/jewel-tone mosaic tessellation.
**Technique:** SVG/canvas Truchet-tile generative overlay that extends the mosaic pattern
algorithmically beyond the image's edges, so photo and generative pattern blend seamlessly.
Gold, lapis, garnet palette, an old-style serif.

## 34 — CARTOGRAPH (`34-cartograph`)
Antique cartography. **Asset:** one generated image, hand-drawn-style antique map/atlas page,
sepia. **Technique:** SVG animated route lines and a compass rose draw themselves over the
map on scroll; hover reveals annotations. Sepia/blueprint palette, a serif with old-style
figures or a hand-lettered-feeling display face.

## 35 — ORRERY (`35-orrery`)
Clockwork solar system. **No generated asset — pure Three.js/WebGL 3D**, this is one of the
collection's real-3D showcase pieces. Brass/gear-textured (procedural materials, not images)
spheres orbiting on tilted rings, draggable camera. Warm brass/candlelit palette, engraved-
plate serif type.

## 36 — ABYSSA (`36-coral`)
Bioluminescent reef. **Asset:** one generated image, deep-sea coral reef, bioluminescent blues
and magentas. **Technique:** Three.js 3D — the image as an environment/background plane behind
a real 3D particle field of drifting "plankton" and a few procedural 3D coral shapes; genuine
depth via camera parallax. Deep sea palette.

## 37 — MURMURATION (`37-murmuration`)
Starling flock at dusk. **Asset:** one generated image, dusk sky gradient with a flock
silhouette for texture reference (or skip if the canvas boids read better against a pure
gradient — owner's brief allows either; if generating, keep it abstract/atmospheric, not the
whole hero). **Technique:** canvas boids algorithm, thousands of birds, interactive (cursor
as a predator/attractor). Dusk gradient palette, elegant italic display serif.

## 38 — FACET (`38-facet`)
Gemstone. **No generated asset — pure Three.js 3D**, second real-3D showcase piece. Low-poly
faceted gem mesh with refraction/env-map shader, rotates and responds to pointer, dramatic
spotlight sweep. Jewel-tone spot palette on black, sharp geometric display type.

## 39 — ILLUMINATED (`39-manuscript`)
Illuminated manuscript. **Asset:** one generated image, illuminated manuscript page detail,
gold leaf and ornate initial capital. **Technique:** CSS gold-leaf shimmer animation (moving
gradient) over generated ornamental border elements; a large drop-cap animates in. Parchment/
gold/deep red palette, a calligraphic or blackletter-adjacent display face used sparingly.

## 40 — THUNDERHEAD (`40-thunderhead`)
Storm. **Asset:** one generated image, dramatic storm cell / thunderhead sky. **Technique:**
canvas procedural lightning-bolt generator (recursive branching, mid-point displacement)
flashes over the image at intervals + on click, brief screen-flash + rumble-timed (visual
only) delay effect. Near-black/violet-grey palette, condensed bold display type.

## 41 — LOOM (`41-loom`)
Textile weave. **Asset:** one generated macro image, woven textile/embroidery close-up, warm
fiber tones. **Technique:** CSS/SVG generative weave-grid pattern that "unravels"/reweaves on
scroll, sampling colors from the image. Warm fiber-art palette (rust, cream, indigo thread),
a warm humanist serif.

## 42 — SUMI (`42-inkwash`)
Ink-wash calligraphy. **Try ONE short Higgsfield video** of ink dropped in water / sumi-e
ink diffusion (get_cost first; fallback to a single generated still of an ink-wash brush
stroke if video is impractical). **Technique:** video/image as hero, canvas fluid-ish ink
diffusion simulation responds to cursor/click on top. Minimal monochrome + one red seal
accent, brush-feel display type if available, otherwise clean sans for restraint.

## 43 — HOLOTYPE (`43-holotype`)
Holographic foil / trading card. **Asset:** one generated image, holographic foil texture,
iridescent rainbow sheen on dark. **Technique:** CSS conic-gradient holo-foil shader blended
with the image via blend-modes, tilts interactively with cursor/gyroscope (parallax card
tilt), like a physical foil card. Black base, full-spectrum iridescent accent, bold condensed
display type.

## 44 — MAGNETO (`44-magneto`)
Magnetic field lines. **Asset:** one generated image, iron filings tracing a magnetic field
around a bar magnet, macro, dramatic lighting. **Technique:** canvas vector-field visualization
of two or more draggable "poles" whose field lines redraw live, image used as a textured
backdrop/reference. Electric palette (black, cyan, magenta), technical mono type.

## 45 — DUNES (`45-dunes`)
Desert. **Asset:** one generated image, warm desert sand dunes, long shadows, wind ripples.
**Technique:** WebGL heightmap-parallax shader (multiple scroll-linked layers derived from
the image) plus a light procedural sand-particle drift. Warm gradient palette (ochre, rose,
violet dusk), an elegant thin display serif.

## 46 — CATHEDRAL (`46-cathedral`)
Stained glass. **Asset:** one generated image, cathedral stained-glass window, jewel tones,
light behind it. **Technique:** SVG tessellated "lead came" line overlay on the image (looks
hand-leaded) + CSS animated light-ray sweep across it. Jewel palette on stone-grey, a gothic-
adjacent but readable display face used sparingly, clean serif for body.

## 47 — CASSETTE-90 (`47-cassette`)
Cassette-futurism / retro hardware. **Asset:** one generated image, product-style shot of a
cassette deck / retro synth hardware, studio lit. **Technique:** CSS 3D transforms build an
interactive tape-deck UI (buttons that actually depress, a spinning reel) around/using the
image. Amber CRT + brushed-metal palette, a squarish retro-tech display face.

## 48 — MURANO (`48-murano`)
Molten glass. **No generated asset primarily — pure Three.js 3D metaball/blob shader**, third
real-3D showcase piece (liquid-glass material, refraction, slow morph). May optionally use
one generated glass-texture image as an environment map only if it clearly improves the
render; do not let it become the hero. Vivid Murano-glass palette on black.

## 49 — TRANSIT (`49-transit`)
Subway/transit diagram. **Asset:** one generated image, vintage transit-map paper texture
(aged paper grain) used only as a subtle background texture, not the hero. **Technique:**
SVG animated transit-map generator draws flat-color lines and stations, Vignelli-style,
purely algorithmic — the generated asset just adds paper grain underneath. Flat primary
color line palette on off-white/aged paper, a clean grotesque.

## 50 — ECLIPSE (`50-eclipse`) — finale
Solar eclipse / corona. **Asset:** one generated image, solar corona during totality,
dramatic. **Try ONE short Higgsfield video** of the corona shimmering if budget allows
(get_cost first) — this is the collection's closing piece, worth spending on. **Technique:**
Three.js 3D sphere (the moon) occults a light source in front of the generated/animated
corona backdrop — genuine 3D + generated imagery + motion, all three Wing II techniques
combined as a closer. Stark black/white/gold palette, confident display serif.

---

## Asset generation batching
- **Batch A (task #2):** 26–37 — aurora, terrazzo, kintsugi, glacier, mycelium, riso,
  oscilloscope, tessera, cartograph, orrery(none), coral, murmuration.
- **Batch B (task #3):** 38–50 — facet(none), manuscript, thunderhead, loom, inkwash,
  holotype, magneto, dunes, cathedral, cassette, murano(optional), transit, eclipse.

Each generated image: save as `sites/XX-name/assets/hero.jpg` (or `.png`). Any video:
`sites/XX-name/assets/hero.mp4` (download and re-host locally — do not link to Higgsfield's
CDN directly, it may not be a stable long-term URL).
