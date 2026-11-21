# Work page — composition and implementation brief

Approved direction: 21 November 2026.

## Visual reference

Use the final approved mockup, **Refined Art Portfolio Clusters.png**, as the composition reference:

[Open the approved mockup](https://chatgpt.com/library?file_id=libfile_1f6eaec01f948191b418e7a07783f507&account_id=personal).

The mockup establishes composition and atmosphere. Its generated objects are illustrative placeholders, its project classifications are provisional, and its typography approximates the chosen fonts. Replace placeholders with Mariana's actual project assets and use the actual fonts when building the site.

## Core idea

The Work overview presents three small collections of project collages: **Art, Research, Education**. Each project is a miniature assemblage of related objects, sketches, and material fragments. The overall feeling is a minimal cabinet of curiosities: tactile, personal, playful, and airy.

This page uses category collections rather than a filter bar. All three collections are visible together on desktop. The handdrawn shelves belong to the landing page; the Work page has no shelves.

## Page structure

1. Small handwritten name/signature at upper left; navigation at upper right: Work, On my desk, Illustration, About me, Contact. Mark Work with a small magenta handdrawn underline.
2. Large uppercase textured heading: **WORK**.
3. Small typewriter subtitle beneath it. Current mockup copy: “A collection of things I make, explore, and share.” Treat this as draft copy.
4. Three equally prominent category headings: **ART**, **RESEARCH**, **EDUCATION**, aligned on the same horizontal baseline and spaced across the page.
5. A compact collection of project collages directly beneath each category heading, with a relatively small heading-to-collection gap.

## Composition and spacing

- Keep the category headings aligned; let the objects beneath them be informal and irregular.
- Vary object size, angle, and position. Avoid a rigid internal thumbnail grid or matching object dimensions.
- Each project has one main recognizable object with roughly one or two smaller supporting fragments.
- Tuck those fragments closely around their main object. Small overlaps are welcome when the main object stays legible.
- Bring neighboring project collages fairly close together within a category, as in the final reference, while preserving enough blank space to distinguish projects.
- Leave wider ivory gutters between categories than between projects within a category.
- Keep substantial blank space around the overall composition, especially below it.
- Preserve a hierarchy of spacing: fragments within a project are closest; projects within a category have a little more separation; categories have the most separation.
- Keep the objects small relative to the page. Richness comes from related fragments and varied scales, rather than oversized thumbnails.
- Use the approved reference to judge density. Earlier sparse versions and shelf layouts are superseded for this page.

## Project collage ingredients

Mix photographic cutouts with transparent backgrounds, pencil/crayon drawings, small photo scraps, material samples, words where meaningful, and symbolic objects. Every fragment should relate to its project, rather than act as unrelated decoration.

Examples discussed:

| Project | Main object | Supporting fragments |
| --- | --- | --- |
| Xenoflora Olfacta | Blue bioplastic flower | Translucent petal and small botanical sketch |
| Tinker Forest | Paper leaf with a copper circuit | Small craft creature and copper tape scrap |
| Movement Kit | Mechanism drawing or artifact | Loose gear and drawn movement arrow |

These illustrate the composition principle; they are not a final project inventory. Confirm final project selection and category assignments during content assembly. A project can have more than one category, while linking to a single project page.

## Typography and colors

| Role | Choice |
| --- | --- |
| Main Work heading | Pastel Crayon, uppercase, textured |
| Category headings | Uppercase textured crayon treatment matching the approved mockup |
| Navigation, subtitle, project labels | Courier Prime Regular, with slightly increased letter spacing |
| Background | Ivory `#FAF6EE` |
| Primary ink | Near-black `#211E1C` |
| Accent | Magenta `#EB007A` |

For Courier Prime, begin around `0.035em` letter spacing and adjust optically at the actual font size. Use the real font files instead of relying on the mockup's generated letterforms. The category crayon headings are specific to this overview; retain the separate typography hierarchy in project-page-design-rules.md for individual project pages.

## Interaction intent

- Treat each whole project collage as one link to its project page. Supporting fragments belong to that same link.
- On hover, show a soft diffuse halo behind the project assemblage, rather than a rectangular highlight. The mockup illustrates this with a warm halo behind Tinker Forest.
- Reveal the project name close to its object in Courier Prime. Avoid detached captions far from their object.
- Provide the same feedback on keyboard focus. Keep project links named for assistive technology.
- On touch devices, expose project names without requiring hover.

## Build guidance — suggested, not yet visually approved

- Use a responsive outer layout for category sections and locally positioned fragments within each project link. Store object positions, scale, and rotation deliberately so the arrangement remains stable.
- Preserve semantic category headings and one link per project; decorative fragments should not create duplicate links or focus stops.
- Let project collages share small internal overlaps, but keep neighboring project hit areas from overlapping.
- On smaller screens, stack the category collections in Art → Research → Education order, preserving each project's grouping and readable labels. Review a mobile mockup separately.
- Keep image transparency and natural edges. Use shadows sparingly and avoid boxed thumbnail backgrounds.
- No framework or implementation stack has been selected by this composition brief.

## Review checklist

- Three category headings share one desktop baseline.
- Objects are small, varied, and informally arranged.
- Each project reads as a compact related group of fragments.
- Neighboring projects sit close enough to create a cohesive collection.
- Wider gutters clearly separate categories.
- Project links remain identifiable and usable.
- Hover/focus halo sits behind the project and its label stays nearby.
- The page retains generous ivory whitespace and the approved magenta accent.
- Real project assets and actual fonts replace mockup placeholders.

