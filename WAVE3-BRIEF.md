# FABLE 25 — Wave 3 brief (sites 51–62)

## Why this wave exists
Jeremy pointed at a rival collection (fable-25.netlify.app, a different/larger project —
105 sites) and said some of theirs are more impressive and smoother than ours. Investigation
found the gap wasn't really about paid assets — it was **process**: they render every site
headless, look at the actual rendered screenshot, and fix what's visually wrong, plus force
one extra complexity upgrade per site so nothing converges to "safe." They also used paid
Higgsfield 3D generation (image→GLB) for their richest 3D pieces, but **Jeremy said not to
spend Higgsfield credits on this wave** — so Wave 3 proves the polish gap can be closed with
process and craft alone: zero binary assets, same as Wing I, but built under a real
render-and-look critique loop instead of code-only review.

**This wave does NOT touch sites 01–50 or their gallery rows.** It adds a new, distinct
"Wave 3" section to the hub with real screenshot-thumbnail cards (not text rows).

## The critique loop — MANDATORY, this is the actual point of this wave
A screenshot harness already exists at `/Users/jeremyxiang/Claude Sites/fable-25/tools/screenshot.js`
(uses puppeteer-core + local Chrome, already installed, zero cost). A local server is running
at `http://localhost:8935/` serving the `sites/` directory (if it's not responding, start one:
`cd "/Users/jeremyxiang/Claude Sites/fable-25/sites" && python3 -m http.server 8935 &`).

For **every** site, after writing `index.html`, run:
```
node "/Users/jeremyxiang/Claude Sites/fable-25/tools/screenshot.js" "http://localhost:8935/XX-name/" "/tmp/wave3-shots/XX-name"
```
This writes `XX-name-desktop.png` and `XX-name-mobile.png` and prints console errors + doc
height as JSON. **Actually open both PNGs with the Read tool and look at them** — you are a
design director reviewing your own screenshot, not just re-reading source. Look specifically
for: cramped/colliding elements, contrast failures, awkward whitespace, type that's too small
or too big relative to the composition, a hero that reads as "empty" or "generic," mobile
layout breaking. Fix what you find, re-run the screenshot, re-look. This is pass 3 of your
3 iteration passes (build pass, code-review pass, THIS real screenshot pass) — do not skip
the actual look.

**After fixes, apply one deliberate complexity upgrade** before calling a site done: one more
layer of texture, a micro-interaction, a small hidden detail — something that pushes the site
past "competent" toward "someone obsessed over this." Note in the guide what it was.

## Non-negotiables (same as Wings I/II, read `sites/25-resonance/` if unfamiliar)
- One self-contained `index.html` (inline CSS/JS) + `guide/index.html` per site, same
  nav/template pattern as `sites/25-resonance/guide/index.html`.
- **Zero binary assets, zero Higgsfield calls of any kind.** Pure procedural: gradients,
  shaders, SVG paths, canvas math, Web Audio synthesis. Three.js via CDN script tag is
  allowed for the 3D pieces (same exception Wing II used) — but the geometry/materials must
  be procedural, not a generated/imported mesh.
  If a 3D piece needs real production value, lean on Three.js post-processing (bloom via
  `UnrealBloomPass`, or a hand-rolled bloom composite) and proper lighting rigs — that's free.
- One display font per site, distinct from the other 61 sites where possible.
- Accessibility floor: semantic headings, keyboard paths, `prefers-reduced-motion` fallback.
- Numbering continues 51–62. Guide kicker text: "Site NN of 62 · how it was made".

## The 12 concepts

### 51 — MERCURY (`51-mercury`)
Raymarched SDF liquid metal, cursor is gravity — a pool of mercury that dents, pools, and
reflects toward wherever the pointer is. Fragment-shader raymarching (sphere-tracing a
metaball/blob SDF), Fresnel-ish fake reflection, physically dark studio backdrop. Technique:
GLSL raymarching in a full-screen shader (via Three.js `ShaderMaterial` on a plane, or raw
WebGL if you prefer — your call). Palette: near-black + liquid chrome.

### 52 — MARIONETTE (`52-marionette`)
A puppet suspended by real verlet-integrated strings the visitor can pull. Hand-rolled physics
(points + constraints, verlet integration, no library) rendered on canvas or SVG. The puppet
itself can be simple procedural geometry (jointed rectangles/circles) — the strings' physical
behavior is the point, not figure realism. Warm stage-lit palette, spotlight vignette.

### 53 — SALVO (`53-salvo`)
GPU-instanced ember/spark bursts — thousands of particles via Three.js `InstancedMesh`,
triggered by click, with real velocity/gravity/fade, warm-to-cool color drift per particle
age. Palette: near-black with ember orange → violet fade. Emphasize instancing performance
(should hold 60fps with thousands of instances) as the craft flex.

### 54 — CENSER (`54-censer`)
Curl-noise smoke that writes calligraphy — a canvas particle system following a curl-noise
flow field, occasionally coalescing into recognizable glyph-like strokes before dispersing.
Minimal, contemplative. Muted incense-smoke palette (warm greys, single amber accent).

### 55 — AUTOMATON (`55-automaton`)
A mechanical songbird driven by real cam-and-crank kinematics — wind a key (click/drag) and
watch actual linkage math (cam profile → follower → linked SVG parts) move a bird's wings and
beak in a physically plausible mechanical cycle, not just a canned CSS animation. Brass/
clockwork palette, engraved-plate serif.

### 56 — GLOAMING (`56-gloaming`)
A draggable dusk sky using a real atmospheric-scattering approximation (Rayleigh/Mie-style
single-scattering integral, simplified for real-time) — dragging the sun position visibly
shifts scattering color across the whole sky dome. Fragment shader, gradient-rich, warm-to-
cool transition. This is the collection's "real atmospheric physics, not a gradient" flex.

### 57 — DRAPE (`57-drape`)
Hand-rolled cloth simulation — a mass-spring-damper grid (not a library) rendered as a
triangulated mesh (canvas or Three.js), cursor acts as wind/force, cloth drapes over an
implied form under gravity. Muted fabric palette, single accent thread color.

### 58 — REVENANT (`58-revenant`)
A humanoid silhouette built from thousands of noise-displaced points that hold formation,
then disperse into drifting particles and re-coalesce on a cycle or on interaction. Canvas or
WebGL point cloud, no mesh — the "ghost" reads through point density and motion, not geometry.
Cold desaturated palette, single warm point-light accent.

### 59 — LATHE (`59-lathe`)
An interactive pottery wheel — drag to "throw" a procedural vessel: a radial profile curve
deforms in response to pointer movement (push in/out/up), rendered as a lathed 3D form
(revolve the 2D profile around an axis, Three.js `LatheGeometry` rebuilt live from the
profile points) with wet-clay-style shading. Earthy palette, warm studio light.

### 60 — DRIFT (`60-drift`)
A self-playing generative ambient "album" — Web Audio synthesizes an evolving generative
ambient piece (no user input required to start, but a play/pause + a couple of macro knobs),
visualized as a WebGL/canvas waveform-terrain that deforms in real time with the audio's
spectral content (FFT-driven displacement). This is Wave 3's answer to a "music that makes
itself" piece — different mechanic from 25-resonance's playable keyboard synth and
32-oscilloscope's patchable scope. Deep space/aurora-adjacent but fully procedural palette.

### 61 — OBSERVATORY (`61-observatory`)
A dense, legible live data dashboard — synthesize a plausible dataset client-side (e.g.
simulated tidal/lunar/solar-position data computed from real astronomical formulas, not
random noise) and present it as a control-room panel: multiple canvas gauges, a scrolling
strip chart, numeric readouts, all updating smoothly. The craft flex is information density
that stays legible — real typographic hierarchy, not clutter. Technical mono type, restrained
dark palette with one signal color.

### 62 — ZENITH (`62-zenith`) — Wave 3 finale
Volumetric god-rays through dust at solar noon — raymarched or layered-shader light shafts,
drifting dust motes (particles), a bloom pass (Three.js `UnrealBloomPass` or hand-rolled
additive-blend bloom) tying together every technique this wave practiced: shader raymarching
(51), particles (53/58), and post-processing. Its guide should close out Wave 3 explicitly:
name the rival collection's process lesson (screenshot-based critique + one deliberate
complexity upgrade per site) and state plainly that this wave was built with it, at zero
additional cost, no generated assets. Stark bright-white/gold palette — the collection's
brightest site, deliberately, after 61 sites that lean dark.

## Thumbnails for the gallery
Once ALL 12 sites are built and passed their screenshot critique, generate gallery thumbnails
for each with:
```
node "/Users/jeremyxiang/Claude Sites/fable-25/tools/screenshot.js" "http://localhost:8935/XX-name/" "/Users/jeremyxiang/Claude Sites/fable-25/sites/assets/thumbs/XX-name" --thumb
```
This writes one `sites/assets/thumbs/XX-name.png` (1280×800, above-the-fold, not full-page).
The hub gallery integration (new Wave 3 card section) is handled separately — don't edit
`sites/index.html` or `sites/guide/index.html` yourselves.
