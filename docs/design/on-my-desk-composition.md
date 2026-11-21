# On my desk — composition and implementation brief

Documented: 21 November 2026. Based on the approved desk concept and the portfolio's subsequently chosen visual identity.

## Visual reference

[On my desk: studio experiments.png — approved desk mockup](https://chatgpt.com/library?file_id=libfile_8298276a589481918ad15cae9cbd2c67&account_id=personal).

Use this image for the top-view desk composition, mixed media, and atmosphere. The mockup predates the final typography and navigation decisions: replace its “Studio” navigation label with “On my desk” and use the current five-section navigation. Its illustrated experiments are visual proposals, not a verified inventory of experiments to publish.

## Core idea

A handdrawn top view of Mari's own desk, scattered with bits and pieces of experiments: material tests, sketches, mechanisms, electronics, paper folds, and unfinished ideas. The drawing style draws on Mari's Atelier illustration.

The page feels like an invitation to look at what Mari is exploring. It makes room for curiosity and work in progress without requiring every experiment to become a full portfolio case study.

## Page structure

1. Small handwritten name/signature at the upper left.
2. Navigation at the upper right: Work, On my desk, Illustration, About me, Contact. Mark On my desk with the small magenta handdrawn active underline.
3. Prominent page title: **ON MY DESK**. The reference places its title centrally above the desk.
4. Small typewriter subtitle immediately below: “experiments, fragments, things in progress”. This is the mockup's draft copy.
5. A large top-view drawing of a desk beneath the title, containing photographic experiment fragments, drawings, short annotations, and a few familiar desk tools.

## Desk composition

- Draw the desk perimeter by hand, with imperfect rounded corners and a textured black crayon/pencil stroke.
- Keep the desktop the same warm ivory as the surrounding page. It is a light drawn boundary, rather than a solid furniture illustration.
- Use a top-down view throughout, including drawn tools such as scissors, pencils, a thread spool, a cup, and a sketchbook.
- Let some tools sit at the edges or slightly cross the desk outline. They frame the experiments without overwhelming them.
- Scatter experiment objects at different scales and angles; avoid a thumbnail grid, shelves, or boxed cards.
- Leave open space between experiments so their shapes and annotations can be read.
- Place short handwritten notes beside the relevant object, with small arrows ending close to it.
- Use small material groups when meaningful: a material test with a scrap or a mechanism sketch with a related part.
- Keep the visual focus on the experiments. Desk tools support the scene.
- Preserve an airy, personal, tactile feeling, even as the collection grows.

## Mixed-media language

The desk combines handdrawn black outlines with actual photographed material and artifact cutouts. Preserve transparent edges and natural textures. Small paper scraps or sketchbook pages can retain their own paper backgrounds.

Examples visible in the reference:

| Experiment or fragment | Visual treatment |
| --- | --- |
| Folded translucent fabric | Photo cutout, with a short handwritten question and arrow |
| Leaf circuit | Leaf photo/cutout with copper tape, coin cell, and LED |
| Mechanism test | Sequential pencil sketches on a loose paper scrap |
| Blue bioplastic samples | Irregular translucent material fragments |
| Paper folding | A small group of folded paper objects |
| Illustration in progress | Sketchbook with an unfinished character drawing |

Use these as examples of composition and media, not as a requirement to reproduce generated objects. Prefer Mari's actual photos, sketches, and experiments when assembling the final page.

## Typography and palette

| Role | Choice |
| --- | --- |
| Main page title | Pastel Crayon, uppercase, using the chosen portfolio display font |
| Subtitle, navigation, readable experiment labels | Courier Prime Regular with slightly increased letter spacing |
| Informal annotations | Mari's own handwriting or actual drawn assets where available |
| Background | Ivory `#FAF6EE` |
| Drawn outlines and primary text | Near-black `#211E1C` |
| Accent strokes and arrows | Magenta `#EB007A` |

The mockup's cursive title and annotations express the handdrawn atmosphere; they are not an additional selected font. Use the chosen display font for the built page title. For Courier Prime, start around `0.035em` letter spacing and adjust optically.

Keep object colors natural. Use magenta sparingly for annotation arrows, small emphasis marks, and navigation. Use actual portfolio arrow assets where suitable; keep the annotation text close to its arrow.

## Experiment notes and content

- Short questions and observations suit this section: what is being tried, what happened, and what might come next.
- Keep the overview text brief and close to the object. Longer explanations can live in a detail view if needed.
- Work in progress, failed tests, small discoveries, and material explorations all fit the concept.
- Do not imply an experiment is finished or invent results to fill the composition.
- Final experiment inventory and exact copy remain to be selected.

## Interaction intent

The approved artifact is a static visual mockup. The following carries the site's established interaction language into the desk; the exact detail-view behavior still needs a decision.

- For experiments with more content, treat the object and its related fragments as one link or control.
- Use a soft diffuse halo behind an interactive experiment on hover and keyboard focus. Keep it behind the object rather than drawing a rectangular button around it.
- Place the experiment name close to the object. The reference includes a small play triangle beside the fabric experiment, suggesting a motion clip where footage exists.
- If an experiment has a video or animation, provide intentional playback and respect reduced-motion preferences.
- Make any actionable label available on touch and to keyboard users. Decorative tools should not create unnecessary focus stops.
- Do not make purely decorative objects appear to promise unavailable content.
- Whether experiments open inline, in a small detail view, or on their own pages remains undecided.

## Build guidance — suggested, not yet visually approved

- Keep experiment content in semantic markup; use positioning to create the desktop composition rather than flattening the whole page into one image.
- Store each experiment's main asset, related fragments, short text, optional media, and chosen position together.
- Give each experiment a stable position and scale. Avoid random placement that changes on every visit.
- Keep related fragments inside one interaction group and avoid overlapping hit areas between neighboring experiments.
- Ensure arrows, labels, and objects remain together when the viewport changes.
- On narrow screens, adapt the desk into a vertically extending composition with a smaller number of experiments across. Keep labels readable and targets usable rather than shrinking the whole desktop image. A mobile composition still needs review.
- Draw the desk outline and decorative tools with original assets where possible. Keep black strokes slightly irregular and textured.
- Maintain enough surrounding space for the desk to feel inviting and uncluttered.
- No framework or implementation stack is selected by this brief.

## Review checklist

- Top-down handdrawn desk is immediately recognizable.
- Actual experiment fragments mix naturally with sketches and drawn tools.
- Ivory whitespace remains visible between items.
- Notes and arrow tails sit close together, with arrowheads close to their objects.
- Magenta accents remain selective.
- Current navigation and actual chosen fonts replace the older mockup's labels and approximate lettering.
- Interactive experiments have clear, accessible labels and grouped hit areas.
- The composition remains legible without relying on hover.
- Placeholder objects are replaced with real assets before publication.

