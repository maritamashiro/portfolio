# First website pass — 21 November 2026

## Implemented

- Landing: responsive cabinet, individually linked objects, hover/focus halos and labels.
- Work: aligned Art, Research, Education collections; compact grouped SVG/image tokens.
- Xenoflora: actual images, what-if opening, author credit, collage, design/fabrication, scent/interaction, FAB2026 photo with caption at top right, magenta closing question. No pending TEI submission or paper thumbnail.
- Tinker Forest: initial project page with original photos and a concise source-based description.
- On my desk: initial responsive experiment composition and image enlargement.
- Illustration overview and Live Illustration: actual original notes, supplied intro, featured sheets and manual carousel.
- About and Contact: simple working first drafts based on public professional information and the original website's public contact links.
- Shared mobile menu, keyboard focus, native image dialog, manual carousel, reduced-motion support.

## Still to refine

- DK Cool Crayon has replaced Pastel Crayon using Mariana’s supplied TTF. Further refine the handwritten name asset if desired.
- Replace provisional SVG project symbols with Mariana's own sketches/cutouts. Current symbols are visual proposals, not documentary photos.
- Complete Work curation, especially additional art/research projects; avoid adding filler. Some unmigrated projects currently open their original Wix pages and are labelled as archive links in accessible names.
- Review newly condensed project copy, author credits, and exhibition details before public launch.
- Replace On my desk symbolic experiment placeholders with a chosen inventory and decide detail-view behavior. Current decorative drawings do not pretend to open new content.
- Design About and Contact fully, including the intended Rube Goldberg contact concept. Current contact uses working email/social links.
- Recover/review all remaining illustrated notes; carousel currently contains the three recovered sheets.
- Review mobile layouts on actual devices. Responsive CSS is included; desktop interactions were checked in the available browser.
- Supply page sharing images and final metadata, then verify the published GitHub Pages URL.

## Publishing status

Repository created: https://github.com/maritamashiro/portfolio

First successful deployment verified: https://maritamashiro.github.io/portfolio/

Publishing uses GitHub Actions on main. The custom domain is not connected. The initial downloadable ZIP predates repository creation; the GitHub repository is the current source of truth.

## Selected homepage projects

The eight shelf projects follow `content/portfolio-project-questions.md` in order. Xenoflora and Tinker Forest have full initial pages. Beyond Ornaments, Creature Kit, Teaching IoT, Face Hacking, Immersive Coding, and Talk to Me currently have clearly marked migration previews with their exact questions. The shelf SVG symbols are provisional illustrations.

## Authentic shelf imagery

Six selected projects use actual project images: Xenoflora (existing cutout), Creature Kit (cardboard creature), Teaching IoT (electronics activity), Face Hacking (recognition experiment), Immersive Coding (projected artwork), and Tinker Forest (light-up creature). New source URLs and image treatments are recorded in `content/project-token-sources.json`. Beyond Ornaments and Talk to Me use their names as temporary tokens until original project images or drawings are supplied. The new photographs retain their original backgrounds and appear as small prints.

## Custom project tokens — 22 November

- Beyond Ornaments: paper ornament cutout from uploaded `12 - papergif4.gif`.
- Creature Kit: green-bodied creature extracted from `Projects.jpg`; two upper cardboard limbs lift around their brad pivots on hover/focus, with a reduced-motion alternative.
- Teaching IoT: native SVG sketch based on supplied laptop/lamp photograph; lamp illuminates intermittently.
- Face Hacking: photo-and-doodle cutout from uploaded `scroobly (2).gif`.
- Immersive Coding: SVG viewport crops out the original right-side caption.
- Tinker Forest: main purple creature cutout from `project2_edited.jpg`, including reconstructed missing extremities.
- Talk to Me: drawn typewriter.
- Homepage labels show only the exact Markdown question on hover or keyboard focus. Crayon headings and signature have no CSS rotation.

The two uploaded files ending in `.gif` contain single-frame PNG data, not animation. Their current tokens are static pending animated source uploads. Four photographic tokens use AI-assisted extraction/reconstruction and remain separate from documentary photos.
