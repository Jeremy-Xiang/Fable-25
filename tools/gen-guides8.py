#!/usr/bin/env python3
"""Generate Wave 8 guide pages (126-150): graphs and data visualisation."""
from guidegen import build

G = {}
def g(slug, name, accent, sub, idea, how, typecolor, passes, lift, meta):
    G[slug] = dict(name=name, accent=accent, sub=sub, idea=idea, how=how, typecolor=typecolor, passes=passes, lift=lift, meta=meta)

g('126-quirk', 'QUIRK', '#FF5A36', "Turn any link into a styled QR code, with an encoder written from scratch",
 "A friend mentioned a site that turns URLs into pretty QR codes; this is that idea rebuilt in one file. Paste a link, pick a shape and a palette, save a PNG. Nothing leaves the browser.",
 ["The encoder handles byte mode at error-correction level M for versions 1–10 (up to about 200 characters).",
  "Reed–Solomon codewords are computed over GF(256) with log/antilog tables; blocks are interleaved as the standard requires.",
  "All eight mask patterns are tried and the one with the lowest penalty score is kept.",
  "Drawing is separate from encoding: the same matrix is rendered as dots, connected “liquid” blobs, diamonds, bars or squares, and the three corner eyes are drawn as whole shapes."],
 ["Unbounded for the headline, with a two-colour gradient that matches the default palette.", "Every palette keeps dark modules on a light ground, because inverted codes do not scan everywhere."],
 ["Thirty-five generated codes (seven lengths × five shapes) were decoded back with OpenCV to prove the encoder. The first styled versions failed: the corner eyes were too round to be detected. Eye corners were tightened and an inverted palette was replaced; after that every code decoded to its original text."],
 ["Separate the data matrix from how it is drawn, and restyling becomes free.", "If you generate something a machine has to read, test it with a machine — looking right is not enough.", "Keep the finder eyes close to square and leave the four-module quiet margin."],
 'stack — one HTML file · hand-written QR encoder · canvas 2D<br>signature — codes verified by decoding them')

g('127-tether', 'TETHER', '#FF7AB6', "A force-directed network you can drag and extend",
 "The default way to draw a network: let it draw itself. Nodes repel, links pull, and communities appear as clumps without being told to.",
 ["Every pair of nodes repels with an inverse-square force; each link is a spring with a rest length.",
  "A weak pull toward the centre stops the graph drifting away.",
  "Node size follows its number of links; hovering dims everything except a node's neighbours.",
  "Clicking empty space adds a node joined to its two nearest neighbours."],
 ["Five community colours on deep indigo.", "Space Grotesk and Space Mono."],
 ["Rendered correctly first time; 260 steps are pre-run so it opens already settled."],
 ["Pre-run physics before first paint so a layout never opens as a knot.", "Dimming non-neighbours on hover is the most useful single interaction for any network."],
 'stack — one HTML file · canvas 2D · n² repulsion<br>signature — structure from two forces')

g('128-roots', 'ROOTS', '#2F6B3F', "Paste URLs and they grow into a radial tree",
 "This began as a misheard message — “a site that turns URLs into pretty trees” — and was too good not to build anyway. A list of URLs is a tree already; this just draws it.",
 ["Each URL is split on slashes and inserted into a nested map, one level per path segment.",
  "Every node gets a slice of the circle proportional to its number of leaves, and sits at the middle of its slice.",
  "Branches are Bézier curves that leave along the parent's radius and arrive along the child's.",
  "Editing the text re-parses and regrows the tree."],
 ["Paper and leaf green, Young Serif for the title.", "Hovering turns the path back to the root rust-red."],
 ["Rendered correctly first time."],
 ["Any slash-separated data (file paths, routes, categories) can be drawn with this exact code.", "Sizing slices by leaf count keeps labels from colliding."],
 'stack — one HTML file · canvas 2D · radial tidy tree<br>signature — a list becomes a plant')

g('129-chord', 'CHORD', '#FF8552', "A chord diagram of who messages whom",
 "Chord diagrams show flows within one group. Here it is a week of messages between eight invented friends: who talks most, who talks to whom, and who mostly listens.",
 ["Each person's arc length is proportional to the messages they sent.",
  "The arc is subdivided per recipient; a ribbon joins the two matching sub-arcs.",
  "Ribbons are two arcs joined by quadratic curves through the centre.",
  "Hovering a name isolates their ribbons and writes a one-line summary."],
 ["Eight distinct hues on charcoal; wide Syne headline.", "Ribbons take the colour of whoever sent more."],
 ["Rendered correctly first time."],
 ["Use a chord diagram only for flows inside one set; for two different sets use a Sankey.", "A sentence that changes on hover does more than a tooltip full of numbers."],
 'stack — one HTML file · canvas 2D<br>signature — ribbons through the centre')

g('130-sankey', 'SANKEY', '#E4572E', "A flow diagram of where twenty-four hours go",
 "A Sankey diagram keeps quantity visible as it splits. One band of 24 hours divides into four parts, then into the things that actually fill a day.",
 ["Nodes are stacked in three columns with heights proportional to hours.",
  "Each link is a band between two nodes, drawn as a pair of Bézier curves.",
  "Running offsets on each node keep bands from overlapping where they attach.",
  "Hovering a band or a label lights its whole path."],
 ["Cream with four category colours; DM Serif Display.", "Hours are printed beside every label."],
 ["Rendered correctly first time."],
 ["Sankeys work when totals are conserved from left to right.", "Give categories personality in the labels; the chart does the arithmetic."],
 'stack — one HTML file · canvas 2D · 3 columns<br>signature — one river dividing')

g('131-wayfinder', 'WAYFINDER', '#FFE14D', "Three shortest-path searches you can watch and compare",
 "The same grid, three strategies. Dijkstra expands evenly in all directions; A* leans toward the goal; greedy search rushes and sometimes pays for it.",
 ["All three share one loop and differ only in the priority used to pick the next cell.",
  "Visited cells are tinted by distance from the start, so the frontier's shape is visible.",
  "Walls are drawn by dragging; the two endpoints can be dragged too.",
  "The count of visited cells is the comparison that matters."],
 ["Dark slate, a yellow path, green start and pink goal.", "Archivo Black titling, Martian Mono labels."],
 ["Rendered correctly first time."],
 ["Showing the work of an algorithm explains it better than its result.", "One code path with a swappable scoring function makes comparisons honest."],
 'stack — one HTML file · canvas 2D · A*, Dijkstra, greedy<br>signature — the frontier')

g('132-metro', 'METRO', '#E3262E', "A transit map for an invented city, with a route planner",
 "Transit maps are graphs with good manners: only 45° angles, even spacing, interchange circles. This one also answers the question maps exist for.",
 ["Six lines are lists of grid coordinates; stations at the same coordinate merge into an interchange.",
  "A breadth-first search finds the route with the fewest stops.",
  "The route is rewritten to stay on the current line where two lines serve the same hop.",
  "The answer is written as a sentence with coloured line badges."],
 ["White ground, six saturated line colours, a pale river for orientation.", "Hanken Grotesk, with station names set at an angle."],
 ["Rendered correctly first time."],
 ["Restricting angles to 0, 45 and 90 degrees is most of what makes a diagram read as a transit map.", "Present a computed route in words as well as on the picture."],
 'stack — one HTML file · canvas 2D · BFS routing<br>signature — the map answers back')

g('133-smallworld', 'SMALL WORLD', '#5B3FD6', "The Watts–Strogatz experiment with a slider",
 "Why is everyone a few handshakes from everyone? Start with a ring of neighbours and rewire a few links at random: distances collapse long before the neighbourhoods break up.",
 ["Sixty nodes, each linked to its four nearest neighbours.",
  "Each link has a fixed random number; the slider decides which ones are rewired, so sliding back and forth is stable.",
  "Average path length comes from a breadth-first search from every node; clustering counts triangles.",
  "Hovering a node labels everyone by their distance from it."],
 ["Lavender ground, violet ring links, red shortcuts.", "Newsreader italic headline."],
 ["Rendered correctly first time."],
 ["Tie randomness to fixed seeds so a control feels continuous.", "Two bars that move at different rates can be the whole argument."],
 'stack — one HTML file · canvas 2D · all-pairs BFS<br>signature — two bars that diverge')

g('134-treemap', 'TREEMAP', '#FF6B4A', "A squarified, zoomable treemap of an imaginary disk",
 "The chart behind every disk-usage tool. Area is size; nesting is folders; the eye finds the largest thing immediately.",
 ["The squarify algorithm fills rows along the shorter side, adding items while the worst aspect ratio improves.",
  "Folders reserve a header strip and lay out their children inside.",
  "Clicking a folder makes it the new root; the path above steps back.",
  "File names carry the humour: three copies of the same installer."],
 ["Black with one hue per top-level folder.", "Familjen Grotesk and Commit Mono."],
 ["Rendered correctly first time."],
 ["Squarified layout keeps rectangles readable; plain slice-and-dice does not.", "Believable invented data makes a demo memorable."],
 'stack — one HTML file · canvas 2D · squarify<br>signature — zoom by clicking')

g('135-spanning', 'SPANNING', '#FFCF5C', "Prim's algorithm laying cable between islands",
 "The minimum spanning tree: connect everything with the least total length and no loops. Shown as cable being laid across a dark sea.",
 ["Prim's algorithm keeps, for each unconnected island, its nearest connected neighbour.",
  "Each step adds the closest island; the faint dashed lines are what each remaining island is currently considering.",
  "The saving is measured against simply chaining nearest islands.",
  "Clicking the sea adds an island and starts again."],
 ["Deep navy, white islands, gold cable with a glow.", "Marcellus capitals."],
 ["Rendered correctly first time."],
 ["Showing the candidates an algorithm rejects makes the choice legible.", "A comparison number gives a result meaning."],
 'stack — one HTML file · canvas 2D · Prim<br>signature — candidate lines')

g('136-stream', 'STREAM', '#EF476F', "A streamgraph of a year of listening",
 "A stacked area chart with a wandering baseline, so the whole reads as one river. Good for showing how a mix changes over time.",
 ["Seven series are generated as a baseline plus a few Gaussian bumps.",
  "Layers are stacked and every column is shifted so the stack is centred.",
  "Curves are Catmull–Rom splines through the weekly points.",
  "Each layer is labelled at its thickest point."],
 ["Warm cream with seven strong colours; Bricolage Grotesque.", "Labels switch between light and dark by layer."],
 ["An exponent written after a unary minus was a syntax error. After that, the curves showed stair-steps from horizontal tangents; switching to Catmull–Rom removed them."],
 ["Centring the stack is the only difference between a stacked area and a streamgraph.", "Label inside the shape, at its widest point."],
 'stack — one HTML file · canvas 2D · spline areas<br>signature — one river')

g('137-arcs', 'ARCS', '#9C2F2F', "An arc diagram of an invented play",
 "Put every character on one line and draw an arc between any two who share a scene. Order by household and three families appear; order by name and they vanish.",
 ["Links are generated from a seeded random number generator, denser within households.",
  "Arcs are half-ellipses; height grows more slowly than width so long arcs do not leave the page.",
  "Reordering animates each character to a new position.",
  "Hovering a name shows only their arcs."],
 ["Paper and oxblood, Cormorant with Courier labels — a theatre programme.", "Same-household arcs take the household colour; others are black."],
 ["Rendered correctly first time."],
 ["In a one-dimensional layout, order is the whole design.", "Animate reordering so the reader can follow which item went where."],
 'stack — one HTML file · canvas 2D<br>signature — order reveals plot')

g('138-matrix', 'MATRIX', '#FF4D6D', "An adjacency matrix that only makes sense once sorted",
 "The same network as a grid of squares. Alphabetical order looks like static; sorted by community it becomes four bright blocks.",
 ["Thirty-six people in four communities, assigned out of alphabetical order on purpose.",
  "Each ordering is a permutation; rows and columns animate to it together.",
  "Within-community squares take the community colour; bridges are grey.",
  "Hovering a square names the pair and their relationship."],
 ["Near-black with four neon community colours.", "Anton headline."],
 ["Rendered correctly first time."],
 ["Matrices scale to dense networks where node-link drawings fail.", "A good default ordering is the most important decision."],
 'stack — one HTML file · canvas 2D · animated permutation<br>signature — blocks from noise')

g('139-sunburst', 'SUNBURST', '#E0A030', "A zoomable sunburst of an orchestra's seating",
 "Hierarchy drawn as rings: sections, families, instruments. Click an arc and it opens to fill the circle.",
 ["Each node stores a start and end fraction of the circle.",
  "Zooming animates a view window; every arc is mapped through it.",
  "Ring depth is rescaled so the remaining levels fill the radius.",
  "The centre shows the current total and acts as the back button."],
 ["Concert-hall dark with four section hues.", "Playfair Display italics."],
 ["The first rings used a square-root radius, which made the inner ring too thick; a linear radius fixed it."],
 ["Animate the view, not the data — zoom is a change of mapping.", "Make the centre of a radial chart do something."],
 'stack — one HTML file · canvas 2D · radial partition<br>signature — click to open')

g('140-bundle', 'BUNDLE', '#58A6FF', "Hierarchical edge bundling of a codebase's imports",
 "Hundreds of straight lines are a hairball. Pull each line toward the centre of its package and they gather into cables you can read.",
 ["Forty-eight files sit on a circle, grouped by package.",
  "Each import is routed through its package's hub and the other package's hub.",
  "A tension slider blends that route with a straight line.",
  "Hovering a file colours what it imports blue and what imports it orange."],
 ["GitHub-dark with one colour per package.", "Geist and Geist Mono."],
 ["Rendered correctly first time."],
 ["Bundling trades exact paths for readable structure.", "Two colours for outgoing and incoming is a convention worth keeping."],
 'stack — one HTML file · canvas 2D · bundled curves<br>signature — the tension slider')

g('141-contagion', 'CONTAGION', '#E5383B', "An epidemic model on a contact network",
 "Spread depends on the shape of the network. Click someone to start an outbreak; raise the immune share and the same spark fails.",
 ["Two hundred people are linked to their three nearest neighbours, plus a few long-distance ties.",
  "Each day an ill person may infect each well neighbour; after eight days they recover.",
  "A small chart tracks well, ill and recovered over time.",
  "It is labelled as a toy model, not a forecast."],
 ["Newsprint grey with red, slate and teal.", "Libre Franklin heavy, with one Baskerville italic."],
 ["With the first settings the outbreak usually died after two people, so the opening looked empty; the default transmission chance was raised."],
 ["Pick defaults so the first thing a visitor sees is the interesting case.", "Say what a model is not."],
 'stack — one HTML file · canvas 2D · SIR on a graph<br>signature — the immune slider')

g('142-percept', 'PERCEPT', '#00D1B2', "A small neural network learning in front of you",
 "Twenty-odd neurons learn to separate two colours of dots. One panel shows the wiring changing; the other shows the boundary it is drawing.",
 ["A 2-8-6-1 network with tanh units, trained by plain gradient descent, all written by hand.",
  "Link thickness is weight size; colour is sign.",
  "The right panel evaluates the network on a 44×44 grid every frame.",
  "Hovering the map sends that point through the network and lights the neurons."],
 ["Teal and orange for the two classes and for positive and negative weights.", "Sora and JetBrains Mono."],
 ["Rendered correctly first time."],
 ["Show a model's output over its whole input space, not only on the data.", "Small enough to draw is small enough to understand."],
 'stack — one HTML file · two canvases · hand-written backprop<br>signature — the boundary bending')

g('143-lineage', 'LINEAGE', '#3FB950', "A commit graph you grow with three buttons",
 "Version history drawn as railway track. Commit, branch, switch and merge; left alone, an invented team keeps working.",
 ["Commits store a column, a lane and their parents.",
  "Branching takes the first free lane; merging adds a commit on main with two parents and frees the lane.",
  "Edges between lanes are Bézier curves; the view scrolls to follow the newest commit.",
  "Commit messages are drawn from a list of familiar ones."],
 ["GitHub-dark with one colour per branch.", "Mona Sans and Fira Code."],
 ["Rendered correctly first time."],
 ["A directed graph with time on one axis needs only lanes and curves.", "Self-running demos should stop the moment a person takes over."],
 'stack — one HTML file · canvas 2D<br>signature — track laying itself')

g('144-markov', 'MARKOV', '#E63946', "A Markov chain drawn as a graph, writing sentences",
 "The simplest text generator there is. Each word is a node; each arrow means “was followed by”. A token walks the arrows and writes.",
 ["The text is split into words and full stops; each pair of neighbours adds to an arrow's count.",
  "The next word is chosen in proportion to those counts.",
  "Recently used arrows stay red and fade.",
  "Editing the text rebuilds the graph."],
 ["Paper and ink with one red.", "Literata, with word size following frequency."],
 ["Rendered correctly first time."],
 ["Seeing the graph explains both why the output sounds plausible and why it means nothing.", "Let visitors replace the sample data."],
 'stack — one HTML file · canvas 2D · word-level chain<br>signature — the hopping token')

g('145-orbs', 'ORBS', '#FFB454', "A packed bubble chart of the solar system's round bodies",
 "Planets, large moons and dwarf planets as circles sized by their real radii. True scale shows how lopsided the system is; a compressed scale lets the small ones be read.",
 ["Circles are pushed apart by repeated collision passes and pulled gently to the centre.",
  "The readable scale raises radius to a power below one.",
  "Sorting by kind moves each group to its own column.",
  "Bubbles can be dragged; the rest make room."],
 ["Black with one colour per kind and a simple highlight for volume.", "Chakra Petch capitals."],
 ["The cluster was small and off-centre; radii were scaled up and the centre moved."],
 ["Offer a true scale and a readable one, and say which is which.", "Collision relaxation is enough for bubble charts; no packing algorithm is needed."],
 'stack — one HTML file · canvas 2D · collision packing<br>signature — true scale toggle')

g('146-parallel', 'PARALLEL', '#B5532A', "Parallel coordinates with brushing",
 "Six measurements per item, six vertical axes, one line per item. Drag along an axis to filter and patterns between the others appear.",
 ["180 invented coffees in three families, with built-in relationships (price follows altitude; roast lowers acidity).",
  "Each row is a smooth line across the axes.",
  "A brush is a range on one axis; a line is kept only if it passes every brush.",
  "The page opens with expensive coffees selected, to show the idea."],
 ["Cream with three earthy family colours.", "Fraunces and Inconsolata."],
 ["A variable named <code>top</code> clashed with the browser's <code>window.top</code> — the same mistake as site 120 — and was renamed."],
 ["Open with a filter already applied; an unfiltered parallel plot looks like a tangle.", "Build real correlations into invented data, or there is nothing to find."],
 'stack — one HTML file · canvas 2D · brushing<br>signature — drag to filter')

g('147-ridgeline', 'RIDGELINE', '#D64933', "A ridgeline plot of monthly temperatures in four climates",
 "Twelve overlapping curves, one per month. The outline of the stack is the seasonal cycle; each curve's width is how variable that month was.",
 ["Each month is a normal curve, sometimes with a smaller second bump.",
  "Curves are drawn back to front with a light outline so overlaps read.",
  "Switching climate morphs every curve to its new shape.",
  "Height is normalised so the tallest ridge spans a fixed number of rows."],
 ["Cool grey with a blue-to-red temperature gradient.", "Source Serif and Archivo Narrow."],
 ["Ridges were several times too tall and ran off the top; height is now normalised to the tallest curve."],
 ["Overlap is the point of a ridgeline — about two to three rows.", "Colour by the x-axis value so the chart needs no legend."],
 'stack — one HTML file · canvas 2D<br>signature — the stack is the season')

g('148-daylight', 'DAYLIGHT', '#FFCC4D', "A radial chart of sunrise and sunset for any latitude",
 "One trip round the circle is a year; the gold band is daylight. At the equator it is a ring. Near the poles it swallows the chart in summer and disappears in winter.",
 ["Day length comes from the sun's declination and the standard sunrise equation.",
  "Radius is time of day; the band runs from sunrise to sunset.",
  "Polar day and night are handled by clamping the equation.",
  "A white spoke marks today, using the visitor's clock."],
 ["Midnight blue with a glowing gold band.", "Fraunces light and Geist Mono."],
 ["Rendered correctly first time."],
 ["Cyclical data belongs on a circle.", "Computing from a formula means the chart is correct for every input."],
 'stack — one HTML file · canvas 2D · sunrise equation<br>signature — the ring warps')

g('149-rank', 'RANK', '#2F6FED', "PageRank shown as random surfers",
 "A page is important if important pages link to it. The original description was a random surfer; here are three hundred of them.",
 ["Each surfer follows a random link, or sometimes jumps to a random page.",
  "The exact ranking is computed by power iteration; circle size follows it.",
  "Clicking two pages adds or removes a link, and the ranking updates.",
  "The slider changes how often surfers jump."],
 ["White with four primary colours.", "Public Sans and Plex Mono."],
 ["Rendered correctly first time."],
 ["Show the process and the exact answer together; each explains the other.", "Let visitors edit the graph to test their intuition."],
 'stack — one HTML file · canvas 2D · power iteration<br>signature — the wandering crowd')

g('150-atlas', 'ATLAS', '#FFD76A', "All 150 sites as one graph",
 "The collection's own map. One node per site, pulled into eight clusters by wave. Hover for a name, type to search, click to go.",
 ["The site list was generated from the real folder names, so every node links somewhere.",
  "Each node is drawn toward its wave's hub and pushed away from its neighbours.",
  "The legend isolates a wave; the search box highlights matches and Enter opens a single match.",
  "This page appears in its own graph, marked."],
 ["Night sky with one colour per wave.", "Fraunces light and JetBrains Mono."],
 ["Clusters were too tight to pick out single dots; repulsion was increased and the pull to the hub reduced."],
 ["A collection's index can be a visualisation of the collection.", "Search plus hover is enough navigation for a hundred-odd items."],
 'stack — one HTML file · canvas 2D · force clusters · 149 live links<br>signature — you are here')

if __name__ == '__main__':
    assert len(G) == 25, len(G)
    build(8, G)
