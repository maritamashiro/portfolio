# Project token editing notes

Built-in image generation was used for the four transparent photographic cutouts. The exported WebP assets are in `public/assets/tokens/`. Documentary project images were kept separately.

## Beyond Ornaments

Extract only the circular white paper ornament and delicate hanging fibers. Preserve crumpled paper texture and proportions; remove fingers and black background; complete the small missing rim where fingers overlap. Center the complete ornament with genuine transparent alpha; no new embellishments, text, floor, or cast shadow.

## Creature Kit

Extract only the bottom green corrugated cardboard creature from Projects.jpg, preserving four tan curved limbs, brass brads, googly eyes, small holes, and photographic materials. Remove other creatures and carpet. Keep full creature uncropped on transparent alpha. SVG layers split the upper limbs at their attachment points for puppet motion.

## Face Hacking

Extract the person together with the lime green and white Scroobly face-tracking drawing. Preserve glasses, mask, white turtleneck, hair/eye/tongue/hand doodles. Remove room and ceiling between doodle strokes. Transparent alpha; no face replacement or new lettering.

## Tinker Forest

Extract only the main purple light-up creature, preserving googly-eyed head, purple body, visible coin-cell/foil/copper-tape assembly, wire, glowing LED and orange pipe-cleaner limbs. Remove tabletop and other toys. Reconstruct cropped head edge and missing paw tips only. Preserve diagonal pose; transparent alpha.

## Animation sources

The initial files named .gif contained one PNG frame each. The later Beyond Ornaments ZIP preserved 34 real GIF frames, lasting 3.4 seconds, now used in the website with an SVG background alpha filter. Face Hacking remains static pending its animated original. Creature movement uses four independent Web Animations hinge tracks with a settle on exit; the lamp uses intermittent CSS glow. Both include reduced-motion alternatives.
