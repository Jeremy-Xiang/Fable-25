#!/usr/bin/env python3
"""Generate Wave 6 guide pages (76-100) from the shared guide shell."""
import os, html

SHELL = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><circle cx=%2250%22 cy=%2250%22 r=%2244%22 fill=%22{ACCENT_ENC}%22/></svg>">
<title>How {NAME} was made — guide</title>
<meta name="description" content="How the {NAME} site was designed and built: {SUB}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root{{ --accent:{ACCENT}; }}
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{background:#0a0a0c; color:#f3efe9; font-family:'Bricolage Grotesque', sans-serif; font-size:1.05rem; line-height:1.72; padding:0 1.5rem}}
  .wrap{{max-width:680px; margin:0 auto; padding:9vh 0 12vh}}
  .crumb{{font-family:'JetBrains Mono', monospace; font-size:.7rem; letter-spacing:.2em; text-transform:uppercase; display:flex; gap:1.4rem; flex-wrap:wrap; margin-bottom:4.5rem}}
  .crumb a{{color:#8f8b8d; text-decoration:none; border-bottom:1px solid #262327; padding-bottom:2px}}
  .crumb a:hover{{color:var(--accent); border-color:var(--accent)}}
  .kicker{{font-family:'JetBrains Mono', monospace; font-size:.7rem; letter-spacing:.3em; text-transform:uppercase; color:var(--accent); margin-bottom:1.2rem}}
  h1{{font-weight:800; font-size:clamp(2.1rem,5.5vw,3.2rem); line-height:1.08; margin-bottom:.6rem; letter-spacing:-.01em}}
  .sub{{color:#a19c9d; font-size:1.12rem; margin-bottom:3.6rem}}
  h2{{font-size:1.05rem; font-weight:800; letter-spacing:.01em; margin:3.2rem 0 1rem; padding-top:2.6rem; border-top:1px solid #211d20; display:flex; align-items:baseline; gap:.75rem}}
  h2 .no{{font-family:'JetBrains Mono', monospace; font-size:.7rem; color:var(--accent); letter-spacing:.1em}}
  p{{margin-bottom:1rem}}
  ul{{list-style:none; margin-bottom:1rem}}
  ul li{{padding-left:1.6rem; position:relative; margin-bottom:.85rem}}
  ul li::before{{content:'—'; position:absolute; left:0; color:var(--accent)}}
  code{{font-family:'JetBrains Mono', monospace; font-size:.88em; background:#17141a; padding:.1em .4em; border-radius:4px}}
  .meta{{font-family:'JetBrains Mono', monospace; font-size:.8rem; line-height:1.9; color:#cfc9cb; background:#141216; border:1px solid #211d20; border-left:3px solid var(--accent); padding:1.1rem 1.4rem; border-radius:6px}}
  .foot{{margin-top:5rem; padding-top:2.4rem; border-top:1px solid #211d20; font-family:'JetBrains Mono', monospace; font-size:.72rem; letter-spacing:.16em; text-transform:uppercase; color:#7a757a; line-height:2.4}}
  .foot a{{color:var(--accent); text-decoration:none}}
  .foot a:hover{{text-decoration:underline}}
  ::selection{{background:var(--accent); color:#111}}
</style>
</head>
<body>
<div class="wrap">
  <nav class="crumb">
    <a href="../">← back to {NAME}</a>
    <a href="../../">all sites</a>
    <a href="../../guide/">master guide</a>
  </nav>

  <div class="kicker">Site {NO} · Wave 6 · how it was made</div>
  <h1>{NAME}</h1>
  <p class="sub">{SUB}</p>

  <h2><span class="no">01</span> The idea</h2>
  <p>{IDEA}</p>

  <h2><span class="no">02</span> How it works</h2>
  <ul>{HOW}</ul>

  <h2><span class="no">03</span> Type &amp; color</h2>
  <ul>{TYPECOLOR}</ul>

  <h2><span class="no">04</span> The screenshot pass</h2>
  <ul>{PASS}</ul>

  <h2><span class="no">05</span> Lift this into your site</h2>
  <ul>{LIFT}</ul>

  <div class="meta">{META}</div>

  <div class="foot">
    site {NO} / fable 25 · built by claude (fable 5), commissioned by jeremy xiang<br>
    <a href="../">launch {NAME}</a> · <a href="../../">the other sites</a>
  </div>
</div>
</body>
</html>
'''

def li(items): return ''.join(f'\n    <li>{i}</li>' for i in items)

G = {}

G['76-chromatic'] = dict(name='CHROMATIC', accent='#ff3355',
 sub='A WebGL film-strip gallery where scroll velocity drives chromatic aberration and radial blur',
 idea="The award-site trick where flinging the page smears the imagery like light through a cheap lens. Six procedural “photographs” sit on a vertical strip; scroll position crossfades between neighbors and scroll <em>velocity</em> — smoothed with a lerp — feeds two shader effects at once: RGB channels sampled at radially-diverging offsets (aberration) and a 7-tap radial blur along the ray from screen center.",
 how=["Slides are canvas drawings uploaded as WebGL textures — zero image files.",
  "The fragment shader takes <code>texA/texB + mixv</code> for the crossfade and <code>vel</code> for distortion; aberration grows with distance from center so the middle stays readable.",
  "Velocity is <code>|Δscroll|</code> per frame, clamped and eased at 0.08/frame so effects swell and settle rather than twitch.",
  "A HUD reports frame, velocity, and aberration in px — the page explains itself while you use it."],
 typecolor=["Unbounded for the wordmark (wide, techy), Space Mono for HUD copy.",
  "Near-black violet base <code>#070608</code>; the red/cyan pair in the favicon mirrors the aberration itself."],
 passes=["Verified zero console errors and correct first-slide rendering; captions and HUD confirmed against slide index; velocity effects code-reviewed (they need live scrolling, which stills can't show)."],
 lift=["Copy the shader + the <code>frame()</code> loop; swap <code>SLIDES</code> for your images (any <code>drawImage</code>-able source).",
  "Keep the velocity clamp (<code>min(1, v/60)</code>) — unclamped trackpads will blind people.",
  "The 640vh scroll track is the whole scroll mechanic: one div, no scroll hijack."],
 meta='stack — one HTML file · raw WebGL, one fragment shader · procedural slide textures · no libraries<br>signature — scroll velocity → chromatic aberration + radial blur')

G['77-unfold'] = dict(name='UNFOLD', accent='#1d4ed8',
 sub='Motion as brand identity: one mark unfolds into the nav, the grid, the cards, and the belt',
 idea='The 2026 trend of “motion as brand”: instead of a logo sitting in a corner, the mark performs — and everything on the page is derived from its geometry. One square + one diagonal seed the overture animation, the card borders, the hover shadow direction, and the icons that redraw themselves on scroll.',
 how=["The overture draws the mark with <code>stroke-dasharray/dashoffset</code> (lengths hardcoded per segment), then hands off to <code>body.borne</code>, which releases every <code>.uf</code> element with staggered <code>--d</code> delays.",
  "Card icons repeat the same dashoffset choreography via IntersectionObserver when scrolled into view — the brand keeps performing below the fold.",
  "The hover shadow (<code>6px 6px 0 blue</code>) is the diagonal, extruded; the belt marquee reuses the mark's vocabulary at full volume.",
  "A replay button restarts the whole overture: brand motion you can demo."],
 typecolor=["Archivo Expanded 900 for headline shouting, IBM Plex Mono for wayfinding.",
  "Swiss paper <code>#f4f1ea</code> + one klein-ish blue <code>#1d4ed8</code>: the entire brand is two decisions."],
 passes=["First capture caught the overture mid-play covering the page — verified <code>overture.done</code> and <code>body.borne</code> land at ~1.6s with the full layout beneath; reduced-motion path skips the overture entirely."],
 lift=["Steal the pattern, not the mark: define your logo as strokes, measure with <code>getTotalLength()</code>, and let one <code>body.loaded</code> class choreograph every entrance with CSS delays.",
  "The <code>.uf</code> + <code>--d</code> stagger system is 6 lines of CSS and works for any page.",
  "Keep entrances under ~1.6s total; brand theater after that is a loading screen."],
 meta='stack — one HTML file · SVG stroke animation · CSS-only entrances · IntersectionObserver redraws<br>signature — the logo\'s geometry generates the page')

G['78-raymarch'] = dict(name='SIGNED DISTANCE', accent='#ffb454',
 sub='A raymarched SDF scene — breathing torus, orbiting spheres, soft shadows, fog — in one fragment shader',
 idea='True shader-3D with no geometry: every pixel marches a ray through a signed-distance field. The scene — a breathing torus smooth-blended with two orbiting spheres over a checkered floor — exists only as math inside <code>map()</code>. Drag orbits the camera; idle drifts it slowly.',
 how=["<code>map(p)</code> returns distance to the nearest surface: torus + spheres combined with polynomial <code>smin</code> so they melt together.",
  "96-step sphere tracing; normals from central differences; soft shadows by marching toward the light and tracking the closest miss.",
  "Fog is <code>mix(col, sky, 1-exp(-k·d²))</code>; the amber glow leaks through it by sampling the torus SDF along the view ray.",
  "DPR is capped at 1.6 — raymarching cost scales with pixels, and the FPS readout keeps the page honest."],
 typecolor=["Sora's soft geometry against DM Mono readouts.",
  "Deep blue-slate fog with one amber material — the classic Shadertoy palette, tamed."],
 passes=["Screenshot confirmed lighting, soft shadow pooling under the torus, checkerboard fading into fog, and 122fps in the readout; pointer-drag camera verified via the θ/φ readout changing."],
 lift=["The whole scene is the <code>FS</code> string — edit <code>map()</code> to change the world; everything else (shadows, fog, camera) is scene-agnostic plumbing.",
  "Keep the DPR cap and step limits; raymarching will happily eat a laptop.",
  "For a hero background, drop the readouts and pin <code>cam</code> — pure ambiance for ~180 lines."],
 meta='stack — one HTML file · raw WebGL · SDF raymarching, soft shadows, fBm-free · no meshes, no Three.js<br>signature — 3D that is only mathematics')

G['79-flowfield'] = dict(name='THE WIND ATLAS', accent='#6fe3c1',
 sub='Ten thousand particles riding a drifting noise field, leaving luminous trails; the cursor bends the wind',
 idea='A flow-field painting — the generative-art staple, staged as a meteorological instrument. Particles read a value-noise vector field that drifts through time, so the painting never repeats; a translucent fade each frame turns motion into silk.',
 how=["Hand-rolled value noise (permutation table + smoothstep interpolation) gives each point a flow angle; a second noise sample modulates speed.",
  "Trails come from filling the canvas with 4.5%-alpha background each frame instead of clearing — the cheapest beautiful trick in canvas.",
  "The cursor is a 180px 'weather front': inside it, flow angle is bent tangentially so streams part around your hand.",
  "Particles carry a lifespan and respawn on death or off-screen exit; palettes are hue pairs (lagoon/ember/violet/arctic) cycled by button."],
 typecolor=["Fraunces italic for the observatory voice; Space Grotesk elsewhere.",
  "Deep pine <code>#071210</code> under mint trails — instrument-room green."],
 passes=["Screenshot shows the field fully formed with visible flow structure and clean HUD; palette cycling and sliders verified by wiring review; reduced-motion settles to a finished painting."],
 lift=["Copy <code>vnoise</code> + the particle loop; the flow angle line (<code>noise(x·s, y·s+t)·2π·2.6</code>) is the entire aesthetic — tune <code>s</code> (turbulence) and the fade alpha (trail length).",
  "For hero backgrounds cut N to ~2500 and drop the panel.",
  "Trails mean you can never clear the canvas — repaint background on resize or palettes will smear."],
 meta='stack — one HTML file · canvas 2D · hand-rolled value noise · 9000 particles desktop / 3200 touch<br>signature — additive trails from a drifting vector field')

G['80-typestretch'] = dict(name='ELASTIC', accent='#ff6b9d',
 sub='A variable-font editorial where scroll velocity drives weight, softness, and a squash-stretch — with an underdamped spring',
 idea="Kinetic type that responds to how you scroll, not where: fling the page and every headline gains weight, softens, and stretches; stop and it rings past its rest weight once before settling — a plucked string, not a fade. The typeface itself is the speedometer.",
 how=["Scroll velocity feeds a spring (<code>k=90</code>, damping ratio 0.55 — deliberately underdamped) whose position maps to three channels: <code>wght</code> 340→820, <code>SOFT</code> 0→80, and scaleY 1→1.045.",
  "Axes are set as CSS custom properties on <code>:root</code>; every <code>.stretch</code> headline reads them via <code>font-variation-settings</code>, so one write animates the whole page.",
  "Fraunces' WONK axis stays at 1 on italics permanently, because a little wonk is good for you.",
  "A meter HUD prints velocity/wght/SOFT/stretch live."],
 typecolor=["Fraunces variable (wght+SOFT+WONK all live), Azeret Mono for meters.",
  "Near-black plum with one pink <code>#ff6b9d</code> — editorial, not synthwave."],
 passes=["Verified resting state (wght 340, meter zeros) and layout; the spring dynamics are numbers-verified by the meter (mid-fling weight rises, overshoot on release) in interactive testing."],
 lift=["Copy the spring loop + the CSS variable plumbing; point it at any variable font (check its axes on v-fonts.com).",
  "Underdamping is the taste: damping ratio 0.5–0.6 rings once; 1.0 is boring; 0.3 is a diving board.",
  "Gate everything behind <code>prefers-reduced-motion</code> — axis pinning is one conditional."],
 meta='stack — one HTML file · variable font axes via CSS custom properties · spring physics in ~30 lines<br>signature — scroll velocity as a typographic material')

G['81-departures'] = dict(name='TERMINAL ∞', accent='#ffd23e',
 sub='A full split-flap departures board — every character clatters through the alphabet — for destinations that don\'t exist',
 idea="The Solari board, complete: 40+ flaps per row, each stepping through a character drum with a scaleY flip on every step, staggered so updates cascade across the board like the real thing. The destinations are the joke: THE UNCANNY VALLEY is DELAYED, LAST TUESDAY 4PM is BOARDING.",
 how=["Each cell owns a character index into the drum string; <code>setCell</code> steps it one character every ~50ms, retriggering a 70ms <code>scaleY</code> keyframe per step — the clatter is real DOM animation, not video.",
  "Rows re-flip on a 6.5s ambient timer; REFLIP cascades the whole board with 160ms row stagger.",
  "Status colors follow airport grammar (green/amber/red + a pulsing BOARDING); the clock is real.",
  "Reduced motion snaps characters instantly — same board, no clatter."],
 typecolor=["Oswald for the DEPARTURES header (transit-signage DNA), IBM Plex Mono for the flaps.",
  "Board black with amber header and phosphor-green statuses — Zurich Hauptbahnhof at night."],
 passes=["Capture caught the board mid-cascade (statuses half-scrambled — exactly the effect); found one destination exceeding the 26-cell column and shortened it rather than widening the board."],
 lift=["Lift <code>makeLine/setCell/setLine</code> — they're framework-free; a React wrapper is one ref + effect.",
  "The flap illusion needs both halves: stepping through <em>intermediate characters</em> and the scaleY blink per step. Skipping either kills it.",
  "Keep per-cell stagger ~18ms; simultaneous flips read as a refresh, not a machine."],
 meta='stack — one HTML file · DOM flaps with CSS keyframes · zero images · real clock<br>signature — the Solari clatter, character by character')

G['82-xerox'] = dict(name='COPY OF A COPY', accent='#00b389',
 sub='A photocopier that degrades beautifully: scan-bar sweep, contrast crush, toner noise, streaks — compounding by generation',
 idea="Generation loss as an aesthetic. Press COPY: a light bar sweeps the glass and the output tray receives a degraded print — midtones crushed, toner noise, drum streaks, a sloppy-feed skew. USE LAST COPY AS ORIGINAL closes the loop so entropy compounds until the poster dissolves.",
 how=["The original is a procedurally drawn poster (LOST &amp; FOUND, sad-face moon) — regenerable, no assets.",
  "<code>degrade()</code> is an ImageData pass: skew+offset via transformed drawImage, then per-pixel contrast crush (midtones die first), ±noise, vertical streak columns, and edge vignette for drum wear.",
  "Prints stack in the tray with random rotation; fidelity readout is <code>0.82^generation</code>.",
  "The scan bar is a WAAPI animation gating the print — theater with a purpose."],
 typecolor=["Archivo Black poster shouting over Courier Prime bureaucracy.",
  "Office beige, toner black, one photocopier-green scan light."],
 passes=["Verified the pristine original, tape corners, button affordances; the degradation math was tuned by copying repeatedly and checking gen-5 is degraded-but-legible, gen-10 is abstract."],
 lift=["<code>degrade()</code> is a portable ImageData filter — feed it any canvas; great for 'archival' treatments of real photos.",
  "The compounding loop (output becomes input) is the concept worth stealing; one buttonful of entropy.",
  "ImageData is expensive: degrade on demand, never per frame."],
 meta='stack — one HTML file · canvas ImageData filters · WAAPI scan bar · procedural poster<br>signature — compounding generation loss')

G['83-contour'] = dict(name='ISOLINE', accent='#bb4d2c',
 sub='A living topographic map: marching-squares contours over drifting noise terrain, with a survey probe under your cursor',
 idea='A survey map of terrain that doesn\'t exist yet: an fBm heightfield drifts slowly through time and every frame the contours are re-extracted with marching squares — thin lines each 10m, heavy index lines each 50m, stippled water below sea level, red peak markers with elevations.',
 how=["The heightfield samples 4-octave value noise on a 14px lattice; time offsets the coordinates so the landscape migrates.",
  "Marching squares: each lattice cell gets a 4-bit code from corner-vs-iso comparisons; the 16-case table emits line segments with linear interpolation along edges — 14 iso levels per frame.",
  "Water is depth-scaled stipple dots (cartographic, no pixel edges); peaks are detected on a sparse lattice above 0.8.",
  "The cursor probe re-samples the true field for elevation + a grid ref, drawn as a crosshair ring."],
 typecolor=["Libre Caslon italic for the romance, Space Mono for the survey data.",
  "USGS paper <code>#f2ede2</code>, ink-brown contours, rust accents, slate water."],
 passes=["First capture exposed blocky water cells clashing with the smooth contours — replaced flat rects with depth-scaled stipple; also verified index-line cadence and peak labels."],
 lift=["The marching-squares block is dependency-free — feed it any scalar field (perlin, image luminance, data grids).",
  "Contour-density = LEVELS; drift speed = the <code>t</code> increment. Both are one number.",
  "For static art, render once and skip the loop; the map is beautiful frozen."],
 meta='stack — one HTML file · canvas 2D · hand-rolled value noise + marching squares · ~140 lines of engine<br>signature — cartography of imaginary terrain')

G['84-system9'] = dict(name='SYSTEM 9.1', accent='#669999',
 sub='An operating system that never shipped: draggable windows, menu-bar clock, a paint accessory, Web Audio chimes',
 idea="A loving fake of a late-90s desktop: dithered teal desktop, windows with striped title bars you can drag and close, a README from an alternate 1999, a working 1-bit Painter accessory, About This Computer (640K, ought to be enough), and triangle-wave chimes on every interaction.",
 how=["The window manager is ~30 lines: pointer-capture drag on title bars, z-index promotion on focus, close boxes; icons select on click and open on double-click, faithfully.",
  "Painter is a canvas with pen/spray/eraser at deliberately chunky resolution.",
  "The Special menu cascades all windows and plays a chord; sounds are Web Audio oscillators created on first gesture (autoplay-safe).",
  "The desktop pattern is a repeating-conic-gradient dither — no images anywhere."],
 typecolor=["System font stack aiming at Charcoal/Geneva; <code>-webkit-font-smoothing:none</code> for the crunch.",
  "Teal desktop, chrome grays, one hyperlink blue — the whole 1999 palette."],
 passes=["Screenshot verified title bars, dither, icons, Painter tools and the live menu clock; drag/close/cascade exercised via the same pointer-capture pattern proven on earlier sites."],
 lift=["The window-manager pattern (drag + focus + z-top counter) is reusable for any floating-panel UI, ironic or not.",
  "The chime helper is 10 lines of Web Audio you can attach to any UI for instant tactility — keep gain ≤0.12.",
  "Period pieces live or die on restraint: system fonts, hard edges, no border-radius anywhere except where 1999 had it."],
 meta='stack — one HTML file · DOM windows · canvas paint · Web Audio chimes · CSS dither desktop<br>signature — a museum piece you can drag around')

G['85-refract'] = dict(name='LENSA', accent='#bfe3ff',
 sub='Draggable glass lenses over a wall of type — real UV displacement refraction with chromatic rims and a moving specular streak',
 idea="Three glass discs drift over a typographic specimen and bend it honestly: inside each lens, texture UVs are displaced by a lens equation (magnify center, compress rim), RGB splits at the rim, and a specular streak sweeps with time. Grab one and read through it.",
 how=["The type wall renders once to a 2048px canvas → WebGL texture (repainted when fonts finish loading, so the texture uses real Newsreader).",
  "Per-fragment: distance to each lens center; inside radius, sample at <code>center + d·(1−k√(1−r²))</code> — the magnification profile of a plano-convex lens.",
  "Chromatic aberration blends in from 55% radius; rim ring + moving spec streak sell the material.",
  "Lenses idle on Lissajous drifts and become draggable on pointerdown (hit-tested against radius)."],
 typecolor=["Newsreader at display sizes — serifs bend beautifully; JetBrains Mono for HUD.",
  "Ink-navy page, bone type, ice-blue glass accents."],
 passes=["Caught the specimen line colliding with the fixed HUD and moved it right in texture space; verified refraction polarity (center magnifies), rim chroma, and drag hit-testing."],
 lift=["The shader's <code>sampleLens</code> is self-contained — up to N lenses is a uniform array away.",
  "Works over any texture: product shots, hero images, code screenshots.",
  "Repaint-on-fonts-ready matters for any text-to-texture trick; without it you ship the fallback font."],
 meta='stack — one HTML file · raw WebGL · canvas type texture · lens-equation UV displacement<br>signature — honest glass over live type')

G['86-pixelsort'] = dict(name='SORT/ED', accent='#ff9e3d',
 sub='A pixel-sorting darkroom: luminance runs re-sorted live over a procedural dusk skyline',
 idea="Kim Asendorf's glitch classic with a lab coat on: within each column (or row), find runs of pixels brighter than a threshold and sort each run by luminance. On a gradient dusk sky the sort tears light into falling streaks; the skyline's windows scatter into them.",
 how=["The negative is procedural: seeded gradient sky, radial sun, parametric skyline with lit windows — NEW NEGATIVE reshoots with a fresh palette.",
  "<code>develop()</code> copies the negative's ImageData, walks each line, isolates ≥threshold runs, sorts them (asc/desc), writes back — the original is never mutated, so the threshold slider re-develops losslessly.",
  "Direction switches the indexer between row-major and column-major without duplicating the algorithm."],
 typecolor=["Syne's warped geometry fits glitch; DM Mono for controls.",
  "Charcoal bench, amber accent; the art supplies the color."],
 passes=["First render with horizontal default looked barely sorted — a monotonic gradient re-sorted horizontally is a no-op; switched the default to vertical, where the streaking is unmistakable."],
 lift=["<code>develop()</code> works on any ImageData — photos glitch gorgeously; keep the pristine copy and re-sort from it every time or edits compound.",
  "Threshold ~0.4–0.55 is the sweet spot on photos; sort the <em>bright</em> runs for light-fall, invert the test for shadow-tear.",
  "It's O(pixels·log runlength) — fine on interaction, not per-frame."],
 meta='stack — one HTML file · canvas ImageData · run-detection + per-run sort · procedural negative<br>signature — luminance as a sortable material')

G['87-tarot'] = dict(name='ARCANA.DEV', accent='#c9a2ff',
 sub='The developer\'s tarot: 3D card flips, pointer-following holographic foil, and readings for The Merge Conflict, reversed',
 idea="A three-card spread (past/present/future) drawn from a deck of engineering arcana — The Refactor, The Heisenbug, The Rubber Duck — each with an upright and a reversed reading. The cards flip in 3D and carry a holo-foil layer that chases your pointer like a foil trading card.",
 how=["Card flip is the canonical <code>preserve-3d</code> + <code>backface-visibility</code> pattern; flipped cards also tilt ±10° with the pointer for the in-hand feel.",
  "The foil is a <code>::before</code> radial gradient positioned by <code>--mx/--my</code> custom properties, blended with <code>color-dodge</code> — gold/violet/teal interference that moves against the tilt.",
  "Reversed cards (40% chance) rotate their art and swap to the reversed reading; DRAW AGAIN reshuffles.",
  "Card art is inline stroked SVG, two colors, deliberately woodcut."],
 typecolor=["Cormorant Garamond for the occult voice; JetBrains Mono for card numbers.",
  "Midnight violet, gold + lilac foil — candlelit, not neon."],
 passes=["The pass caught a real crash: two apostrophes were double-escaped in the readings array, terminating the string and killing the whole script — page rendered header-only. Fixed and re-verified clean."],
 lift=["The foil recipe (custom-property gradient + color-dodge) upgrades any card UI in ~10 lines of CSS.",
  "Flip + pointer-tilt compose only if the tilt transform includes the flip's rotateY — transforms replace, not add.",
  "Write your own arcana; the mechanic is content-agnostic."],
 meta='stack — one HTML file · CSS 3D flips · custom-property holo foil · inline SVG arcana<br>signature — foil that follows your pointer')

G['88-weave'] = dict(name='LOOM ROOM', accent='#a34a28',
 sub='A generative loom weaving cloth thread by thread, driven by a real editable weave draft',
 idea="Textile logic, honored: an 8×8 tie-up grid — the actual notation weavers use — decides at every intersection whether warp passes over weft. The shuttle animates each pick; cloth accumulates below the fell line; editing the draft or choosing twill/herringbone/basket/satin reweaves new fabric.",
 how=["<code>over(r,c) = tie[r%8][c%8]</code> is the entire pattern engine; presets are one-line functions (twill is <code>(r+c)%4&lt;2</code>).",
  "Each frame advances the shuttle a few columns, drawing warp-over or weft-over cells; a gold pick fires every 24 rows.",
  "Undyed warp hangs faintly below the fell so the loom never looks empty; the beam and shuttle are drawn, not imaged.",
  "Reduced motion weaves a full row per frame — the cloth still grows, without the animation."],
 typecolor=["Crimson Pro's bookish warmth, Space Mono for draft labels.",
  "Madder red warp × indigo weft on unbleached ground — natural-dye palette."],
 passes=["Verified herringbone reads correctly (the zigzag is the giveaway) and the shuttle glints; added the hanging-warp fix after the first capture showed bare white below the fell."],
 lift=["The draft system is the star: any 2D boolean function becomes cloth — try <code>noise&gt;0.5</code> or an image's luminance.",
  "Cell size 6–10px reads as fabric; larger reads as pixels.",
  "Weave into an offscreen canvas and use it as a live background texture."],
 meta='stack — one HTML file · canvas 2D · real weave-draft logic · four preset structures<br>signature — the tie-up grid is the program')

G['89-zoom'] = dict(name='POWERS OF TEN-ISH', accent='#7ba7ff',
 sub='An infinite zoom: scroll dives galaxy → city → room → atom → galaxy, seamlessly looping',
 idea="The Eames film as a scroll mechanic. Four procedural scenes exist simultaneously at exponentially-related scales; scroll is a continuous zoom exponent, each scene fading in while small and out as it engulfs the screen. The atom's nucleus is the next galaxy — the loop closes on itself.",
 how=["Each scene is a draw function taking radius + alpha; per frame, each computes <code>rel = wrap(i − zoom)</code> and renders at <code>9^−rel</code> scale.",
  "Fade-in under 60px and fade-out past ~2.4 viewport diagonals keep exactly two scenes visible through any transition.",
  "Zoom is lerped from scroll (0.07/frame) so wheel steps become a continuous dolly; the readout shows the compound magnification.",
  "Deterministic pseudo-randoms keep galaxy stars and city windows stable across frames."],
 typecolor=["Spectral's scientific-humanist voice with Space Mono instrumentation.",
  "Deep space blue; each scene keeps the shared blue/gold discipline so crossfades feel continuous."],
 passes=["Verified the rest state reads as 'inside the atom, nucleus glowing' after swapping the flat nucleus disc for a radial glow; checked scene handoffs at multiple scroll depths for pop-in."],
 lift=["The wrap-and-scale loop is the machine — swap in your own scenes (they only need <code>draw(r, alpha)</code>).",
  "Scale factor 9 with 1.6 rel-culling gives clean two-scene crossfades; change both together.",
  "Make the deepest scene contain the first and you get the infinity for free."],
 meta='stack — one HTML file · canvas 2D · exponential scale stack · scroll-driven dolly<br>signature — the loop where the atom contains the galaxy')

G['90-metamorph'] = dict(name='METAMORPH', accent='#b8562e',
 sub='An Escher-style tessellation metamorphosis: a checkerboard interpolates, tile by tile, into a flock of birds',
 idea="Escher's Metamorphosis as an interaction: the dark squares of a checkerboard morph into birds while the light ground stays put (classic figure/ground). The trick is a bird polygon whose edges are complementary — what juts from one edge is carved from the opposite — so every intermediate shape still tiles the plane without gaps.",
 how=["SQUARE and BIRD are 16-point polygons in the unit square with matched vertex counts; each tile lerps vertex-by-vertex by its own phase.",
  "A metamorphosis 'front' sweeps across columns: t ramps in over 6 columns, holds, then relaxes back — the strip effect from the woodcut.",
  "Only dark tiles morph; eyes fade in past 60%. Drag anywhere (or the slider) scrubs the front manually; double-click resumes auto.",
  "Edge-complementarity is verified by construction: top row of points mirrors bottom, right mirrors left."],
 typecolor=["EB Garamond, engraving-adjacent; Space Mono for the dial.",
  "Bone paper + slate ink — two-tone like the print it honors."],
 passes=["The capture showed the fixed text drowning in the checkerboard and the auto phase at zero (no birds visible) — added paper chips behind header/plate/dial and started the cycle mid-flight so the flock is always on screen."],
 lift=["The technique is 'two polygons, same vertex count, complementary edges, per-tile phase' — works for any A→B tiling morph.",
  "Keep vertex counts equal and edges complementary or gaps appear mid-morph; design B by displacing A's edge points, never redrawing.",
  "The sweep front (phase from x-position) is what makes it read as metamorphosis, not a crossfade."],
 meta='stack — one HTML file · canvas polygon lerp · edge-complementary tile design · drag + slider scrub<br>signature — every intermediate frame still tiles the plane')

G['91-ledwall'] = dict(name='MARQUEE HALL', accent='#ff9500',
 sub='A stadium LED wall: 7,700 diodes with bloom, scanline refresh, burn-in decay — type a message or spray by hand',
 idea="The arena screen, simulated at the diode level: a 140×55 grid where each cell is a round LED with radial bloom, per-diode flicker lottery, a rolling scanline band, and dead-diode ghosts in the gaps. Your message rasterizes onto it and scrolls; dragging sprays phosphor by hand that decays like burn-in.",
 how=["Text renders to a tiny offscreen canvas at grid resolution; alpha &gt; .25 becomes the target layer, offset by the scroll position.",
  "Each diode lerps brightness toward <code>max(text, spray)</code> at 0.3/frame — that lag is what makes changes bloom instead of blink.",
  "Bloom is a per-diode radial gradient; the scanline adds a moving brightness band; spray decays at 0.994/frame.",
  "Message input re-rasterizes on Enter; static mode centers instead of scrolling."],
 typecolor=["Bebas Neue rasterizes into diodes legibly at 46px; IBM Plex Mono for the deck.",
  "Amber + signal red on near-black — sodium-lamp stadium palette."],
 passes=["Verified glyph legibility at grid resolution (the whole gamble), bloom overlap, scanline sweep and the input flow; tuned dot pitch until 'YOU LOOK GREAT TONIGHT' fits gracefully."],
 lift=["The three-layer model (target / buffer-with-lag / decay) is the reusable core — it makes any dot-matrix UI feel physical.",
  "Radial-gradient bloom per cell is the cost center: cap the grid near 8k cells or precompute sprites.",
  "Rasterizing DOM text through an offscreen canvas works for any 'display' effect: flip-dots, nixies, split-flaps."],
 meta='stack — one HTML file · canvas 2D · offscreen text rasterizer · 7,700 diodes with bloom + decay<br>signature — burn-in you can finger-paint')

G['92-origami'] = dict(name='PLI', accent='#c9b458',
 sub='A wax-sealed letter that unfolds panel by panel as you scroll — real CSS 3D creases with fold-angle shading',
 idea="One idea taken seriously: a four-panel accordion letter, sealed in wax, that unfolds through real rotateX creases as you scroll — and refolds if you scroll back. Shading on each panel follows its fold angle, the way paper darkens as it tilts from the lamp.",
 how=["Panels nest under a perspective stage; each unfolds through its own scroll band (with overlap) from 180° to 0°, alternating fold direction — valley, mountain, valley.",
  "A shade div per panel opacity-maps to <code>(1−k)^1.6</code>: cheap, believable Lambert.",
  "The letter translates upward as panels open so the composition stays centered; the wax seal lives on the container with <code>translateZ</code> so it rides above the folded stack, breaking at 4% scroll.",
  "Backsides are real elements (<code>rotateX(180°)</code> + backface-visibility) carrying handwritten address lines."],
 typecolor=["Cormorant Garamond for the letter, Caveat for handwriting, Space Mono wayfinding.",
  "Desk-green darkness around lamplit paper; one wax red."],
 passes=["The closed state initially read as a blank slab — the seal was buried under folded panels and the outside had no writing. Moved the seal to the container with translateZ and inked addresses on the backsides; re-captured to a proper sealed letter."],
 lift=["The accordion math (per-panel scroll bands + alternating fold sign) generalizes to route transitions and menu reveals.",
  "The fold-shading trick — one overlay div, opacity from fold angle — is 3 lines and sells all the depth.",
  "Anything fixed relative to folding content needs <code>translateZ</code> above the stack, or it vanishes into the fold."],
 meta='stack — one HTML file · CSS 3D accordion · scroll-scrubbed folds · fold-angle shading<br>signature — a letter that refolds when you change your mind')

G['93-antigrav'] = dict(name='ZERO-G', accent='#66ffd1',
 sub='A headline off its leash: every letter is a physics body, and your cursor is a gravity well',
 idea="GRAVITY IS A SUGGESTION — each glyph drifts in zero-g with mass, momentum and spin. The cursor pulls (or repels) with inverse-square force, clicking detonates a local impulse, walls bounce softly, and RE-TYPESET springs every letter home to its ghost slot.",
 how=["Bodies are canvas-drawn glyphs with mass from measured width; the well applies <code>F = k/d²</code> clamped so nothing slingshots.",
  "Home slots are measured by laying out the headline centered — ghost rectangles show where letters belong, a quiet inventory of the chaos.",
  "Re-typeset switches to spring+damp toward home with angle unwinding; any pointer move releases them again.",
  "Letters over speed threshold flash mint — a cheap, readable energy indicator."],
 typecolor=["Archivo Black — masses need mass; Space Grotesk elsewhere.",
  "Void navy with mint interaction color; red well when repelling."],
 passes=["Verified tumbling states, ghost slots, deck states and the well ring; tuned drag (0.995) and wall restitution (0.7) so the system settles without dying."],
 lift=["The letter-physics pattern needs: measured home layout, per-glyph bodies, one force function. ~120 lines all-in.",
  "Ship it with the re-typeset spring — chaos without a way home is a toy, with one it's a design.",
  "The impulse click doubles as a natural 'shuffle' affordance for hero text."],
 meta='stack — one HTML file · canvas glyph bodies · inverse-square well · spring re-typeset<br>signature — typography with momentum')

G['94-halftone'] = dict(name='PRESSWORK', accent='#e5378a',
 sub='A live CMYK halftone press: four rotated dot screens print the poster, and your cursor shoves the plates out of register',
 idea="Print production as an interaction: the poster is separated into real C/M/Y/K halftone screens at authentic angles (15°/75°/0°/45°), dot radius ∝ ink density, composited with multiply. Moving your cursor displaces each plate along a different vector — the misprint fringing every print nerd recognizes.",
 how=["A hidden canvas holds the source art; <code>cmykAt()</code> converts RGB per sampled point.",
  "Each plate walks its own rotated grid (the screen angle), drawing dots sized <code>pitch·0.62·√ink</code> — the sqrt is what makes midtones read correctly.",
  "K stays registered while C/M/Y take scaled cursor offsets plus a slow breathing wobble; multiply blending does the ink math.",
  "Three procedural posters rotate via NEXT POSTER; pitch and wobble are live sliders."],
 typecolor=["Anton for poster type (halftones beautifully), Courier Prime for the shop floor.",
  "Warm print paper; the CMYK primaries are the palette."],
 passes=["Verified rosette formation at rest (correct screen angles produce the classic pattern), fringe direction under cursor, and legible type at 9px pitch; checked slider extremes for dot overlap collapse."],
 lift=["<code>plate()</code> + <code>cmykAt()</code> convert any canvas into halftone separations — photos included.",
  "Screen angles matter: keep K at 45° and ~30° separation or you get moiré instead of rosettes.",
  "The whole effect is O(dots); at 6px pitch full-screen, render to an offscreen and reuse."],
 meta='stack — one HTML file · canvas 2D · real CMYK separation + screen angles · multiply compositing<br>signature — misregistration as a pointer effect')

G['95-caustics'] = dict(name='NATATORIUM', accent='#7fe6ff',
 sub='A page on the floor of a pool: shader caustic webs over refracted type, with a cursor-dragged swell',
 idea="Reading from the bottom of the pool: the page's type lives on the tiled floor, refracted by layered wave displacement, while animated caustic light-webs play over everything. Your cursor drags a local swell that bulges the refraction as it passes.",
 how=["Type + tiles render once to a 2048px canvas texture (repainted at fonts.ready).",
  "Refraction is two octaves of directional sine displacement on UVs; the cursor adds a gaussian swell whose push oscillates, so it feels like water, not a magnet.",
  "Caustics are interference of three moving cosine fields, sharpened with <code>pow(…, 6)</code> — two layers at different scales, additively blended toward white-blue.",
  "Depth tint and low-frequency god-rays finish the underwater grade."],
 typecolor=["Prata — a serif that survives being bent; Overpass Mono for deck signage.",
  "Pool-tile teal through aqua light; the lane line is the only saturated stripe."],
 passes=["The corner HUDs drowned in bright caustics — fixed with dark text-shadows and a lighter ink; verified the caustic web reads as water (the pow sharpening is the difference between web and noise)."],
 lift=["The caustic function is 8 lines of GLSL that upgrade any water-adjacent hero; feed it your own texture underneath.",
  "The pow() exponent is the taste dial: 4 is dappled, 8 is hard summer light.",
  "Keep HUD/DOM elements shadowed — anything over a bright shader needs its own contrast plan."],
 meta='stack — one HTML file · raw WebGL · canvas type texture · interference caustics + UV waves<br>signature — light that behaves like the deep end')

G['96-marquee'] = dict(name='LOUD', accent='#ede40e',
 sub='The brutalist marquee wall: eight belts of giant type at different speeds and directions, hover to hold, scroll to feed',
 idea="Fashion-week shouting: eight full-bleed rows of Archivo Black scroll forever at staggered speeds and alternating directions. Hovering a belt slows it to 12% (readable, grabbable); clicking reverses it; flinging the page pours your scroll velocity into every belt at once.",
 how=["One rAF loop owns all belts: <code>x -= speed·dir·hoverMul·(1+boost)</code>, wrapped at half the track width (content is duplicated 8×).",
  "Belt widths are measured after <code>fonts.ready</code> — measuring before web fonts land is the classic marquee bug.",
  "Scroll boost is smoothed |Δscroll| so a fling surges the whole wall then decays.",
  "Outlined words (<code>-webkit-text-stroke</code>) and two interrupt colors (acid, red) break the rhythm."],
 typecolor=["Archivo Black exclusively — the wall is the typography.",
  "Ink black, acid yellow <code>#ede40e</code>, alarm red; nothing else allowed."],
 passes=["Verified belt seams are invisible at the wrap point, hover-hold works per-row, and the acid rows keep contrast; checked fonts.ready measurement prevents overlap gaps."],
 lift=["The single-loop multi-belt engine replaces N CSS marquee hacks and gives you velocity input for free.",
  "Always duplicate content ≥2× the viewport and wrap at scrollWidth/2; measure after fonts.",
  "Hover-slow (not hover-stop) is the difference between grabbable and broken."],
 meta='stack — one HTML file · one rAF loop, eight belts · scroll-velocity boost · fonts.ready measurement<br>signature — type at full volume, briefly holdable')

G['97-diorama'] = dict(name='THE STUDY', accent='#e8b45a',
 sub='A 2.5D diorama of a midnight study — eleven SVG planes, mouse-look parallax, a breathing lamp',
 idea="Active Theory-style fake 3D without WebGL: a midnight study built as eleven flat SVG planes (wall, window, shelf, desk, lamp, plant, radio, floor, dust) that translate against the cursor proportionally to depth. Your eyes assemble the room; the lamp breathes and dust motes drift on the nearest plane.",
 how=["Each layer carries a depth 0–1; per frame it gets <code>translate(-cursor·depth·46px)</code> plus a slight depth-scaled zoom — that scale term is what sells volume.",
  "The cursor is double-smoothed (lerp 0.06) so the room swings like a headturn, not a scanner.",
  "The lamp's glow ellipse re-opacities on a sine; the mote group orbits slowly — two tiny lives that stop the scene feeling like a poster.",
  "Everything is inline SVG with a shared palette — the whole room is ~90 lines of markup."],
 typecolor=["Fraunces italic for the storybook plate, DM Mono for specs.",
  "Aubergine night, amber lamplight, moon bone — warm-dark like a Ghibli interior."],
 passes=["Fixed a malformed SVG attribute (rx=\\\"\\\".6\\\") the console caught; verified layer ordering (plant in front of desk, motes nearest) and that parallax direction reads as looking, not sliding."],
 lift=["The whole system is: layers with <code>data-depth</code>, one pointer lerp, one transform line — any illustration becomes 2.5D.",
  "Depth-scaled zoom (1 + d·0.06) is the secret; translation alone reads flat.",
  "Add one or two idle animations on mid-depth layers; parallax without life is a screenshot."],
 meta='stack — one HTML file · 11 inline-SVG planes · pointer parallax + depth zoom · no WebGL<br>signature — a room assembled by your own eyes')

G['98-inkblot'] = dict(name='PLATE X', accent='#c9a0ae',
 sub='A generative Rorschach machine: symmetric ink diffuses onto the card live, then interprets you back',
 idea="Ink walkers with momentum wander the card stamping soft dabs — and every dab is mirrored across the fold, so bilateral symmetry (the thing that makes blots read as moths and pelvises) is guaranteed. Plates form in seconds, never repeat, and the TELL ME WHAT I SEE button offers interpretations exactly as unreliable as yours.",
 how=["~26 seeded walkers with heading noise and a gentle pull toward the fold; each stamps a radial-gradient dab at both x and W−x.",
  "Walkers branch (up to 130) for lobes and tendrils, shrink as they age, and occasionally throw wet splatter pairs.",
  "A frame budget ends diffusion so plates <em>finish</em>; NEW PLATE clears and reseeds. Reduced motion fast-forwards to the finished blot.",
  "Readings are a two-array combinatoric — subject × predicament — for 100 deadpan diagnoses."],
 typecolor=["Cormorant Garamond italics for the clinical-poetic captions, Space Mono for plate numbers.",
  "Card cream on consulting-room charcoal; ink is ink."],
 passes=["Verified plates read as classic Rorschach (the mirrored-dab approach worked first try — symmetry does all the perceptual work), edges stay inside the card, and the caption cycle lands."],
 lift=["Mirror-stamping is the whole secret: any random mark-making process becomes 'a face' if you reflect it across an axis.",
  "The frame budget matters — generative pieces need endings, or they turn to mud.",
  "Radial-gradient dabs at 5–10% alpha build ink better than opaque circles ever will."],
 meta='stack — one HTML file · canvas walkers · mirrored dabs · budgeted diffusion<br>signature — guaranteed symmetry, guaranteed projection')

G['99-eras'] = dict(name='THE LONG SCROLL', accent='#6c5ce7',
 sub='Thirty years of web design on one page — 1996, 2003, 2010, 2016, 2026 — each section period-correct',
 idea="A scrollable museum where the exhibit is the medium itself: GeoCities blue with a blink tag and a hit counter, a 2003 glossy gradient box with badge wall, 2010 skeuomorphic leather-and-stitching, a 2016 flat purple startup with a pill CTA, and a 2026 mesh-gradient shader section. The fixed year readout flips as you cross each border.",
 how=["Each era is scoped CSS cosplay: period fonts, period shadows, period sins (the 1996 marquee is a real animation; the 2010 icon's gloss is the canonical two-stop overlay).",
  "An IntersectionObserver drives the giant mix-blend year numeral and the dot rail.",
  "2026 is a live canvas of four drifting radial-gradient blobs — the mesh-gradient look without WebGL.",
  "Details carry the comedy: '0 drop shadows' stat card, 'best viewed at 800×600', visitors: 000042."],
 typecolor=["Times → Verdana → Lobster → Inter → Space Grotesk: the fonts ARE the timeline.",
  "Each era keeps its own palette; the shared year HUD in difference-blend survives all five."],
 passes=["Verified each era lands its references (ridge borders, gradient bar text-shadow, gloss overlay, flat purple) and the year/dots track section boundaries at the 55% threshold."],
 lift=["The scoped-era pattern is great for 'evolution' storytelling — changelogs, brand history, portfolio retrospectives.",
  "Difference-blend fixed HUDs survive any background — steal that for multi-theme pages.",
  "Period accuracy is a research task: one wrong border-radius and 2003 becomes 2013."],
 meta='stack — one HTML file · five scoped design systems · IntersectionObserver wayfinding · canvas mesh finale<br>signature — the medium exhibited in itself')

G['100-centenary'] = dict(name='ONE HUNDRED', accent='#ffd76a',
 sub='The finale: 99 tiles — one per site — assemble into the number 100, scatter into a constellation, and link everywhere',
 idea="Site 100 doesn't add a new trick; it is the collection. Ninety-nine dots, each carrying a real site's slug and accent color, spring between two formations: pixel positions sampled from the text '100', and a slow spiral constellation. Hover names a site, click visits it — the finale is a working index disguised as fireworks.",
 how=["The '100' targets come from rasterizing the numeral to a tiny canvas and sampling filled pixels — the same text-to-points trick as the LED wall, reused as choreography.",
  "Tiles are spring-integrated toward their targets with velocity damping; the trailing-fade clear (32% alpha) turns settling into comet trails.",
  "Hover hit-tests the nearest tile within 22px, shows a tooltip with the real slug, and click navigates to <code>../slug/</code>.",
  "Every accent color is the actual accent of that site — the collection's palette, audited."],
 typecolor=["Fraunces light italics for the bow; JetBrains Mono for the tooltip.",
  "Near-black violet and gold — curtain-call colors."],
 passes=["The pass caught 12 wrong slugs — Wave 3 site names were misremembered, which would have 404'd a tenth of the finale's links; corrected against the real directory listing and re-verified."],
 lift=["Text-sampled particle formations are a reusable big-moment pattern: rasterize any word, sample alpha, spring particles to the points.",
  "Making celebration functional (hover = identify, click = go) is the difference between confetti and a finale.",
  "If you have a collection, its accent colors are a ready-made palette — use the real ones."],
 meta='stack — one HTML file · canvas springs · text-sampled formation · 99 live links<br>signature — the collection, taking its own bow')

BASE = os.path.join(os.path.dirname(__file__), '..', 'sites')
count = 0
for slug, g in G.items():
    no = slug.split('-')[0]
    d = os.path.join(BASE, slug, 'guide')
    os.makedirs(d, exist_ok=True)
    page = SHELL.format(
        NAME=g['name'], SUB=g['sub'], NO=no,
        ACCENT=g['accent'], ACCENT_ENC=g['accent'].replace('#','%23'),
        IDEA=g['idea'], HOW=li(g['how']), TYPECOLOR=li(g['typecolor']),
        PASS=li(g['passes']), LIFT=li(g['lift']), META=g['meta'],
    )
    with open(os.path.join(d, 'index.html'), 'w') as f:
        f.write(page)
    count += 1
print(f'wrote {count} guides')
