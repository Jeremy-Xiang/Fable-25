#!/usr/bin/env python3
"""Generate Wave 7 guide pages (101-125): simulations, instruments and toys."""
from guidegen import build

G = {}
def g(slug, name, accent, sub, idea, how, typecolor, passes, lift, meta):
    G[slug] = dict(name=name, accent=accent, sub=sub, idea=idea, how=how, typecolor=typecolor, passes=passes, lift=lift, meta=meta)

g('101-petri', 'PETRI', '#7CFFB2', "Conway's Game of Life as a living culture dish you can seed",
 "Four rules, no player, endless behaviour. The page treats Life as a specimen: cells are coloured by how long they have survived, so stable colonies glow differently from the froth around them, and a tray of stamps lets you drop in a glider, a gun or a pulsar.",
 ["The grid is two <code>Uint8Array</code>s swapped each generation; edges wrap, so gliders leave one side and return on the other.",
  "A cell's value is its age, capped — the palette is indexed by age rather than alive/dead.",
  "Stamps are tiny string patterns written into the grid at the pointer.",
  "Play, step, soup and sterilise are the whole interface."],
 ["Monospace labels like a lab notebook; one phosphor green on near-black.", "Age is the only colour variable, so colour always means something."],
 ["The wordmark sat directly on live cells and flickered in and out of legibility; a gradient behind the header fixed it."],
 ["Colour by age is a cheap way to make any simulation readable.", "Wrap-around edges remove the need for boundary cases entirely."],
 'stack — one HTML file · canvas 2D · typed arrays<br>signature — cells that show their age')

g('102-morphogen', 'MORPHOGEN', '#E63946', "Gray–Scott reaction–diffusion: two chemicals that draw coral, mazes and spots",
 "Turing's idea of how a leopard gets its spots, running on the CPU. Two invisible reagents diffuse and react; change two numbers and the same equations produce coral, fingerprints, dividing cells or travelling waves.",
 ["A 220×130 grid of two float fields, updated with a 5-point Laplacian several times per frame.",
  "Recipes are just named <code>(feed, kill)</code> pairs.",
  "Dragging paints reagent B into the field, which seeds new growth.",
  "The field is written to an <code>ImageData</code> and scaled up by CSS, which smooths it for free."],
 ["Paper, navy and one red — a printed scientific plate rather than a neon demo.", "A serif headline with mono parameter readouts."],
 ["First render was an empty sheet because the seed patches were too small to survive; larger initial blobs fixed it."],
 ["Simulating at low resolution and letting CSS upscale is the performance trick behind most of this wave.", "Expose presets, not raw sliders, when a parameter space is mostly dead."],
 'stack — one HTML file · canvas 2D · float32 fields<br>signature — five patterns from one equation')

g('103-chaos', 'CHAOS', '#FFB000', "Sixty double pendulums released a ten-thousandth of a radian apart",
 "Sensitivity to initial conditions, shown rather than explained. All sixty pendulums start as one visible line; for a few seconds they move as one, then the bundle frays and nothing agrees with anything.",
 ["Each pendulum is integrated with the standard double-pendulum equations in small sub-steps.",
  "Trails are drawn on a persistent canvas that fades slowly; arms are redrawn on a second canvas on top.",
  "A readout tracks the angular spread across the set, so you can watch the number explode."],
 ["Hue is assigned by index, so the moment of divergence appears as the first rainbow fringe.", "Condensed sans headline, mono readouts."],
 ["Trails saturated to white after a minute; lowering per-stroke alpha and fading faster kept the colour."],
 ["Two stacked canvases — one that persists, one that clears — is the simplest way to get trails plus crisp foreground.", "Draw many near-identical things to make an invisible property visible."],
 'stack — one HTML file · two canvases · RK-style integration<br>signature — one line becoming sixty')

g('104-tempest', 'TEMPEST', '#B7C9FF', "Click the sky and lightning forks to the ground",
 "A storm you conduct. Each strike is a jittered path from cloud to skyline with branches that fork off and die; the whole scene flashes, and if you allow sound, thunder follows after a delay.",
 ["Bolts are built by midpoint displacement: split a segment, push the midpoint sideways, recurse, and occasionally spawn a thinner branch.",
  "The flash is a full-screen fill whose alpha decays over a few frames.",
  "Thunder is filtered noise from Web Audio with a slow envelope, started only after a click."],
 ["Slate blues with a near-white bolt; the only saturated element is the flash itself.", "Small caps serif titling, like a weather almanac."],
 ["Bolts originally stopped mid-air; they are now aimed at the skyline height under the click."],
 ["Midpoint displacement gives natural-looking lines for lightning, cracks, rivers and coastlines.", "Tie audio to an explicit gesture and it never surprises anyone."],
 'stack — one HTML file · canvas 2D · Web Audio noise<br>signature — the fork')

g('105-vitrail', 'VITRAIL', '#FFCF4A', "A stained-glass window that re-leads itself around your cursor",
 "Voronoi cells are already the shape of leaded glass. Forty seeds drift slowly, each owning a pane of colour; your cursor is one of the seeds, so the window reorganises wherever you point.",
 ["A fragment shader finds the nearest and second-nearest seed for every pixel.",
  "The gap between those two distances draws the dark lead lines.",
  "Pane colour comes from a hash of the seed index, with a soft gradient for a hand-blown look."],
 ["Jewel tones against black lead; a blackletter-adjacent display face.", "Light appears to come through the glass because panes brighten toward their centres."],
 ["Lead lines were uneven widths; switching to the distance-difference formula evened them out."],
 ["Nearest/second-nearest distance is the core of every Voronoi effect.", "Making the pointer one of the data points is an easy way to make generative art interactive."],
 'stack — one HTML file · WebGL fragment shader · 40 seeds<br>signature — the cursor is a pane')

g('106-kaleido', 'KALEIDO', '#FF5DA2', "Draw one line and get a mandala",
 "A kaleidoscope for drawing. Whatever you draw is repeated around the centre and mirrored, so a scribble becomes a rose window. Until you touch it, the page doodles on its own.",
 ["Each stroke segment is redrawn once per mirror by rotating the canvas, plus a flipped copy.",
  "A slider sets 4 to 16 mirrors.", "The auto-doodle is a wandering point driven by summed sines; it stops on first input."],
 ["Dark ground with strokes that cycle through hue as you draw.", "Playful rounded sans."],
 ["The empty canvas gave no reason to click, which is why the auto-doodle exists."],
 ["Never ship an empty canvas — show the result first and let the user take over.", "Rotation plus mirroring turns any input into an ornament."],
 'stack — one HTML file · canvas 2D transforms<br>signature — symmetry does the drawing')

g('107-slingshot', 'SLINGSHOT', '#6FE3FF', "Drag to launch moons around a star and see which ones stay",
 "An orbit sandbox. Pull back from any point to throw a body; a dotted line predicts where it will go before you let go. Most throws crash or escape — the pleasure is finding the ones that don't.",
 ["Bodies feel inverse-square gravity from the central star and are advanced in small fixed steps.",
  "The prediction runs the same integrator ahead a few hundred steps without committing.",
  "Counters track bodies in orbit, crashed and escaped."],
 ["Deep navy with cyan trails and a warm star.", "Mono readouts, a geometric display face."],
 ["Predicted and real paths disagreed until both used the same timestep."],
 ["Showing the outcome before the action commits makes any physics toy learnable.", "Reuse the real simulation for previews so they can never drift."],
 'stack — one HTML file · canvas 2D · fixed-step gravity<br>signature — the predicted path')

g('108-platen', 'PLATEN', '#C8102E', "A typewriter with no backspace",
 "Typing as a physical act. Letters land slightly crooked and unevenly inked, the carriage moves, a bell rings near the margin, and mistakes stay. It types a letter to you until you start typing yourself.",
 ["Each character is a span with a small random rotation, offset and opacity.",
  "The page shifts left as you type and returns on Enter.",
  "The margin bell is a short sine ping from Web Audio.", "Backspace is ignored by design."],
 ["Typewriter face on cream paper with one red ribbon colour.", "The paper has a soft shadow and slight grain so it reads as an object."],
 ["Auto-typing kept going after the user started; it now yields on the first keypress."],
 ["Tiny per-character randomness makes digital text feel made by a machine with parts.", "Removing a feature (undo) can be the concept."],
 'stack — one HTML file · DOM spans · Web Audio ping<br>signature — no backspace')

g('109-clockclock', 'CLOCKCLOCK', '#111111', "Twenty-four small clocks that work together to show one time",
 "After the kinetic wall clocks: a grid of analog clocks whose hands rotate to form the strokes of four large digits. Every minute the whole wall re-choreographs itself.",
 ["Each digit is a 2×3 block of clocks; a lookup table gives the two hand angles each clock needs for each numeral.",
  "Hands ease toward their targets, always rotating clockwise.",
  "A “dance” button sends every hand on a full flourish before settling back."],
 ["Monochrome: white faces, black hands, grey wall.", "Almost no text — the time is the typography."],
 ["Unused clocks pointed at random angles; they now rest at a diagonal so digits read cleanly."],
 ["A lookup table of poses plus easing is all choreography needs.", "Building a display out of smaller displays is a reliably striking idea."],
 'stack — one HTML file · canvas 2D · pose table<br>signature — digits made of clocks')

g('110-hourglass', 'HOURGLASS', '#E9B872', "A falling-sand toy with sand, water and stone",
 "The oldest browser toy, kept small. Pour sand, pour water, draw stone ledges, and watch piles form and water find its level.",
 ["A cellular automaton: each sand grain tries to move down, then diagonally; water also tries sideways.",
  "The grid is scanned bottom-up, alternating direction each frame so nothing drifts to one side.",
  "Standing pours keep the scene alive without input."],
 ["Warm sand, a muted blue and grey stone on dark.", "Pixel-crisp rendering with <code>image-rendering: pixelated</code>."],
 ["Water piled up like sand until sideways movement was added."],
 ["Alternate scan direction in any grid automaton to avoid bias.", "Three materials are enough for emergent behaviour."],
 'stack — one HTML file · canvas 2D · cell automaton<br>signature — water finding its level')

g('111-deepfield', 'DEEP FIELD', '#FFB347', "A Mandelbrot explorer that tours itself until you take over",
 "The famous fractal as a place to fall into. Click to dive toward a point, shift-click to back out; left alone, it visits four well-known regions and returns to the surface.",
 ["Every pixel iterates <code>z = z² + c</code> up to 300 times in a fragment shader.",
  "A smooth iteration count removes colour banding; a cosine palette maps it to amber and teal.",
  "Zoom is interpolated in log space and the centre moves faster than the scale, which makes a dive feel like falling.",
  "Single-precision floats limit depth, so zoom is clamped before the image turns to blocks."],
 ["Bodoni for the title, Fira Code for coordinates.", "Warm palette on a near-black interior."],
 ["The first frame was the whole set, small and plain; the tour now starts immediately so the first impression is the spirals."],
 ["Interpolate zoom logarithmically, always.", "A self-running tour is better than instructions."],
 'stack — one HTML file · WebGL fragment shader<br>signature — the dive')

g('112-pendula', 'PENDULA', '#1B3A6B', "A harmonograph: two decaying pendulums drawing with one pen",
 "A Victorian parlour instrument. The ratio between the two swings is a musical interval, and each interval draws its own family of figures as the motion dies away.",
 ["The pen position is a sum of two damped sine waves per axis.",
  "The interval slider chooses a frequency ratio; a small detune makes the figure precess instead of retracing.",
  "Ink opacity follows the remaining amplitude, so the centre is fainter."],
 ["Cream paper, blue-black ink, a script wordmark and an old-style serif.", "The drawing sits on its own sheet with a shadow."],
 ["No fixes needed beyond confirming the reduced-motion version draws the finished figure at once."],
 ["Sum of damped sines is a tiny formula with a large family of results.", "Label controls in the language of the metaphor (a fifth, an octave), not the maths."],
 'stack — one HTML file · canvas 2D<br>signature — an interval you can see')

g('113-raincheck', 'RAIN CHECK', '#9CC7E8', "A fogged window you can write on while rain runs down it",
 "Night, city lights out of focus, condensation on the glass. Drops gather and run, leaving clear trails; your finger wipes the fog, and it slowly mists back.",
 ["Two canvases: blurred coloured lights underneath, a fog layer on top.",
  "Wiping uses <code>destination-out</code> compositing to erase the fog.",
  "Drops accelerate, stall and wobble, erasing a thin trail as they go.",
  "Every frame a very faint fog fill is added back, so marks fade over a minute."],
 ["A handwriting face for the title, as if written on the glass.", "Grey-blue fog over warm and cool bokeh."],
 ["The fog was too opaque to see the city, and drop trails read as black worms; fog density, trail width and trail strength were all reduced, and the scene now pre-runs so it opens already streaked."],
 ["<code>destination-out</code> is the simplest way to build scratch-off, wipe and reveal effects.", "Pre-run a simulation before first paint so the page never starts blank."],
 'stack — one HTML file · two canvases · compositing<br>signature — fog that comes back')

g('114-trace', 'TRACE', '#E6C15A', "A circuit board that routes its own copper",
 "Generative PCB art. Traces leave chip pads and wander in 45° steps, avoid each other, and end in vias; then small pulses travel along them.",
 ["The board is a grid with an occupancy map; each trace claims cells as it grows.",
  "A trace prefers to continue straight and may turn 45° either way; if blocked, it ends.",
  "Diagonals are refused when they would cross between two occupied cells.",
  "Pulses are interpolated along each finished path."],
 ["Solder-mask green, copper gold, silkscreen white.", "A condensed stencil-like title in a silkscreen box."],
 ["Rendered correctly first time; chip labels were added to give the eye anchors."],
 ["An occupancy grid is the simplest collision avoidance for generative line work.", "Restricting angles to 45° is what makes it read as engineered."],
 'stack — one HTML file · canvas 2D · grid routing<br>signature — pulses on the copper')

g('115-hanabi', 'HANABI', '#FF6B6B', "Fireworks over water, with every spark reflected",
 "A summer festival show. Click the sky to launch a shell; it bursts as a chrysanthemum, willow, ring or rainbow, and the harbour below repeats it dimmer and compressed.",
 ["Sparks are particles with drag and gravity, drawn with additive blending.",
  "The canvas is faded rather than cleared, which leaves glowing trails.",
  "The reflection is each spark redrawn below the horizon, vertically compressed with a small ripple.",
  "An idle timer launches shells so the show never stops."],
 ["Mincho serif set vertically, as on a festival poster.", "Black sky; all colour comes from the shells."],
 ["Sparks were tiny and the reflection fell off-screen; sparks were enlarged, bursts made denser, and the reflection compressed to fit the water."],
 ["Fading instead of clearing is the one-line trail effect.", "Reflections sell a scene and cost one extra draw call per object."],
 'stack — one HTML file · canvas 2D particles<br>signature — the reflection')

g('116-twoslits', 'TWO SLITS', '#5FE0F0', "A ripple tank that shows a wave interfering with itself",
 "The double-slit experiment as water. A plane wave enters from the left, meets a wall with gaps, and the far side fills with bright and dark fringes.",
 ["The 2D wave equation on a 320×200 grid: each cell accelerates toward the average of its neighbours.",
  "A driven column on the left produces the plane wave; wall cells are held at zero.",
  "A damping border absorbs waves so they do not reflect off the screen edge.",
  "Buttons rebuild the wall with one, two, five or no slits."],
 ["Deep teal with white crests.", "Fraunces italics for the title, Plex Mono for labels."],
 ["Rendered correctly first time; 500 steps are pre-run so fringes are already there."],
 ["The wave equation is five lines and looks like physics because it is.", "Absorbing borders matter more than resolution for a clean result."],
 'stack — one HTML file · canvas ImageData · float32 fields<br>signature — the fringes')

g('117-epicycle', 'EPICYCLE', '#FF5D8F', "Draw a line; a chain of spinning circles redraws it",
 "A Fourier series you can watch. Any closed line is a sum of rotations; the page computes them and animates the chain of circles, each riding on the last, with the final tip tracing your drawing.",
 ["The path is resampled to 256 evenly spaced points.",
  "A discrete Fourier transform gives each frequency an amplitude and phase.",
  "Circles are sorted largest first; the slider limits how many are used, so you can see detail arrive.",
  "A heart, a star and a squiggle are provided as starting shapes."],
 ["Near-black, cream construction lines, one pink trace.", "Instrument Serif title."],
 ["The trail started empty; it is now pre-warmed so most of the shape is visible on load."],
 ["Sorting components by size and adding them one at a time explains Fourier better than any formula.", "Resample user input before doing maths on it."],
 'stack — one HTML file · canvas 2D · naive DFT<br>signature — circles on circles')

g('118-telegraph', 'TELEGRAPH', '#F2C14E', "Type a message; a lamp sends it in Morse",
 "A signal station. Your text becomes dots and dashes: a brass lamp flashes, a tone sounds if you enable it, and a paper tape scrolls past with each mark inked.",
 ["Text is expanded into a queue of on/off steps using standard Morse timing (dash = three dots).",
  "One frame loop drives the lamp, the tone gain and the tape together, so they cannot drift.",
  "It sends famous messages on its own until you send yours."],
 ["Oxblood and brass with small-caps serif titling.", "The tape is cream with dark marks and a red pen line."],
 ["Rendered correctly first time."],
 ["Drive several outputs from one queue to keep them in sync.", "Showing the current letter beside its code teaches the code."],
 'stack — one HTML file · canvas tape · Web Audio oscillator<br>signature — the tape')

g('119-labyrinth', 'LABYRINTH', '#E23B2E', "A maze that builds itself, then solves itself",
 "Three algorithms in sequence: a backtracker carves the maze, a breadth-first search floods it with colour by distance, and a red thread is laid from entrance to exit.",
 ["Each cell stores its four walls as a bitmask.",
  "Carving uses a stack: move to a random unvisited neighbour, or back up when stuck.",
  "The search records each cell's distance; the solution is found by walking downhill from the exit.",
  "After a pause, a new maze begins."],
 ["Black, cream and one red — Ariadne's thread.", "Cinzel capitals."],
 ["Rendered correctly first time; the grid size now adapts to the window."],
 ["Storing distance during a search gives you both the solution and a heat-map.", "Showing an algorithm's phases in order is a ready-made narrative."],
 'stack — one HTML file · canvas 2D · DFS + BFS<br>signature — the thread')

g('120-islet', 'ISLET', '#FF7A59', "An isometric island you raise and lower with clicks",
 "A tiny world-builder. Click to raise land, shift-click or use dig mode to lower it; sand, grass, forest, rock and snow follow the height you give.",
 ["A 22×22 height map from value noise with a radial falloff.",
  "Tiles are drawn back to front as a top diamond plus two shaded side faces.",
  "Picking checks tiles front to back for the first top face containing the pointer.",
  "Heights ease toward their targets, so edits rise smoothly."],
 ["Sky blue and coral with a rounded display face.", "Three fixed brightness levels per block give the 3D read."],
 ["A helper named <code>top</code> clashed with the browser's built-in <code>window.top</code> and stopped the script; renamed."],
 ["Isometric 3D on a 2D canvas needs only draw order and three shades.", "Avoid global names that the browser already owns."],
 'stack — one HTML file · canvas 2D · value noise<br>signature — the landscape follows your clicks')

g('121-pluck', 'PLUCK', '#F5C26B', "A harp across the screen with physically modelled strings",
 "Fourteen strings tuned to a pentatonic scale, so anything you play sounds fine. Drag across them to play; each string visibly rings and settles.",
 ["Sound is Karplus–Strong synthesis: a burst of noise in a delay line, averaged on each pass.",
  "A string is plucked when the pointer's path crosses it; speed sets loudness, height sets where it bends.",
  "The visible vibration is a triangle wave peaking at the pluck point, decaying over time.",
  "It strums silently as a demonstration until your first touch, when audio starts."],
 ["Aubergine and gold, italic Cormorant.", "Lower strings are drawn thicker."],
 ["Rendered correctly first time."],
 ["Karplus–Strong is the best sound-per-line-of-code in audio.", "A pentatonic scale removes wrong notes from any toy instrument."],
 'stack — one HTML file · canvas 2D · Web Audio buffers<br>signature — strings you can hear and see')

g('122-sixfold', 'SIX-FOLD', '#9FD6FF', "A snowflake grown from one random arm",
 "Every click designs one arm at random — a spine, branches, sometimes a plate — and symmetry repeats it twelve times into a flake that has not existed before.",
 ["An arm is a short list of line segments in unit space.",
  "It is drawn six times at 60° intervals, each with a mirrored copy.",
  "Segments appear in order so the flake seems to crystallise outward.",
  "Background snow falls slowly behind it."],
 ["Night blue with a cold white glow.", "Italiana capitals; specimens are numbered."],
 ["Rendered correctly first time."],
 ["Design one unit, let symmetry do the rest.", "Numbering generated results makes them feel collectable."],
 'stack — one HTML file · canvas 2D transforms<br>signature — one arm, twelve copies')

g('123-thinfilm', 'THIN FILM', '#E0489E', "Soap bubbles coloured by a thin-film interference shader",
 "Bubble colour comes from the thickness of the soap film. The shader models a film that is thicker at the bottom and stirred by noise, and converts thickness to colour the way interference does.",
 ["Each bubble is a circle with a computed sphere height per pixel.",
  "Thickness combines the rim, a gravity gradient and animated noise.",
  "Colour is a cosine per channel at slightly different rates — each wavelength cancels at a different thickness.",
  "Click a bubble and it swells briefly, vanishes and is replaced from below."],
 ["Pale lilac-grey so the iridescence is the only saturated thing.", "Gloock serif with one pink italic."],
 ["Rendered correctly first time."],
 ["Three phase-shifted cosines are a compact iridescence model.", "A quiet background lets a colourful effect read as delicate."],
 'stack — one HTML file · WebGL fragment shader · 10 bubbles<br>signature — colour from thickness')

g('124-tremor', 'TREMOR', '#C62828', "A seismograph that records your mouse, scroll and keys",
 "A station log of your own restlessness. Movement, scrolling and typing add energy; a spring-loaded needle turns it into a trace on scrolling paper, with a magnitude reading.",
 ["The needle is a damped spring kicked by noise scaled to recent activity.",
  "Energy decays every frame, so the trace settles when you stop.",
  "Magnitude is a logarithm of energy, like the real scale.",
  "With no visitor, occasional tremors happen by themselves."],
 ["Paper, black and seismograph red.", "Heavy condensed capitals with typewriter labels."],
 ["Rendered correctly first time; the trace is pre-filled so the paper is not blank on load."],
 ["A damped spring turns any noisy input into a believable instrument reading.", "Ambient input is a low-effort way to make a page feel alive."],
 'stack — one HTML file · canvas 2D · spring model<br>signature — the page records you')

g('125-encore', 'ENCORE', '#FFE9A8', "A slot reel that lands on one of the other 124 sites",
 "The wave's closer is a way back into the collection. Pull the lever, the reel spins down, and a button opens whichever site it lands on.",
 ["The site list was generated from the real folder names, so every link resolves.",
  "The reel is the list repeated three times, moved with a CSS transform.",
  "A quartic ease-out gives the fast start and long settle of a real reel.",
  "Space bar also spins."],
 ["Theatre red and gold with a marquee display face.", "Cream reel window with red index lines."],
 ["Rendered correctly first time."],
 ["A random-pick page makes a large collection browsable.", "Generate link lists from the file system, never from memory."],
 'stack — one HTML file · DOM + transform · 124 live links<br>signature — the lever')

if __name__ == '__main__':
    assert len(G) == 25, len(G)
    build(7, G)
