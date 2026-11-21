# Live Illustration — composition and implementation brief

Documented: 21 November 2026.

## Approved direction and reference

[Editorial Live Illustration Portfolio.png](https://chatgpt.com/library?file_id=libfile_5feee073b89081919e86b7ad589a6bfb&account_id=personal) is the approved visual reference.

Direction: a professional editorial presentation with a restrained postcard/keepsake feeling. Use straight alignment, consistent artwork sizes, generous margins, light typewriter text, and quiet captions. The drawings supply the expressive detail. This supersedes the earlier rotated-postcard layout with decorative envelopes, stamps, and arrows.

The user subsequently proposed a carousel of all illustrations. This brief includes the agreed direction for it; its appearance has not yet been mocked up.

## Location in the website

Dedicated Live Illustration page within Illustration. Provide a clear entry from the Illustration overview. Use the shared navigation: Work · On my desk · Illustration · About me · Contact, with Illustration marked by a small magenta underline. A small “illustration / live illustration” breadcrumb provides context.

## Purpose

Show how Mari captures important, funny, joyful moments and turns them into illustrated notes participants can keep. Let prospective collaborators understand her style and contact her about an event. Use actual examples and accurate descriptions; final service formats and commercial details remain to be defined.

## Page sequence

### 1. Opening

- Small handwritten name/signature at upper left and shared navigation at upper right.
- Breadcrumb above the title.
- **LIVE ILLUSTRATION** in uppercase Pastel Crayon, prominent but restrained relative to the page width.
- Introduction close beneath it, in Courier Prime Regular at a comfortable reading width.

Use Mari's original text:

> I capture important, funny, and joyful moments of a workshop and later share the illustrated notes with participants as a meaningful souvenir.

### 2. Selected collaboration

Use a light divider followed by an editorial two-column block: small “SELECTED COLLABORATION” label and “Tinkering World Tour” heading on the left, descriptive copy on the right.

Use Mari's original text:

> The illustrated notes below are from a collaboration with the Wonderful Idea Co., from the "Tinkering World Tour" in which artists, makers, and tinkerers from around the world virtually showed their studios and shared their work.

### 3. Featured illustrations

Show two or three large selected illustrations before the carousel. The approved mockup features New Mexico, Kyoto & Tokyo, and Berlin.

- Display the complete artwork, preserving its proportions, original colors, handwriting, and details.
- Align the sheets to one left edge with a consistent display width and consistent vertical spacing. Let height follow the original aspect ratio.
- Use square corners, a narrow quiet paper border, and at most a very subtle shadow.
- Place a small left-aligned typewriter caption immediately to the right of each image, aligned with its top edge.
- Mockup captions: “01 / New Mexico”, “02 / Kyoto & Tokyo”, “03 / Berlin”. These are gallery sequence labels, not invented dates.
- Let the artwork lead. Avoid decorative stamps, envelopes, arrows, overlapping stacks, large frames, and forced crops.

### 4. Full collection carousel

Place a section titled **More illustrated moments** after the featured examples and before the closing invitation.

- Include the complete selected collection of illustrated notes. Keeping featured drawings in the full collection is acceptable; final ordering remains to be chosen.
- Show one complete illustration at a time, with a small portion of the next slide visible to suggest browsing.
- Use simple previous/next arrows and a short caption identifying the current illustration.
- Navigation is manual: **no autoplay**.
- Selecting an illustration opens a larger view so its writing and details can be read.
- Preserve whole-image proportions; a partial preview is for the adjacent slide only.
- Keep controls restrained and consistent with Courier Prime, ivory, near-black, and magenta.
- Exact control placement, slide count treatment, and mobile composition still need a visual review.

### 5. Closing invitation

Use a light divider and generous space before a magenta Courier Prime Bold question:

> What are you bringing people together for?

Follow it with a clear understated link:

> Tell me about your event →

This is proposed CTA copy carried from the mockup. Connect it to the final chosen contact route when implementing. Do not invent availability, prices, testimonials, or service promises.

## Typography and colors

| Role | Choice |
| --- | --- |
| First heading only | Pastel Crayon, uppercase |
| Body, navigation, captions | Courier Prime Regular |
| Section headings | Larger Courier Prime; bold where useful for hierarchy |
| Closing question | Courier Prime Bold, magenta |
| Background | Ivory `#FAF6EE` |
| Primary text | Near-black `#211E1C` |
| Accent | Magenta `#EB007A` |

Keep body text visually light using Regular weight, comfortable line-height, and subtle letter spacing. Start near `0.035em` tracking and adjust at actual size. The generated mockup approximates typography; build with the actual selected fonts. Keep the signature as a separate handwritten identity asset.

## Source artwork

Original website page: https://maritamashiro4.wixsite.com/mariana-tamashiro/illustrations

The three actual drawings recovered for the mockup:

| Artwork | Original image URL |
| --- | --- |
| New Mexico | https://static.wixstatic.com/media/324ae7_b59666c45b0f4f1fb183f7aa5205d778~mv2.jpg |
| Kyoto & Tokyo | https://static.wixstatic.com/media/324ae7_aadf2f91ba0348b792b30436bf19d78b~mv2.jpg |
| Berlin | https://static.wixstatic.com/media/324ae7_6548ed0fe0d7404ca1c0d533b77e59ab~mv2.jpg |

Use original artwork files in the website, rather than extracting illustrations from the generated mockup. Recover and review the remaining collection before filling the carousel; verify captions against each original.

## Implementation guidance — to validate during build

- Keep featured images, captions, and text in semantic page markup.
- Use a responsive image/caption layout; move captions directly below images on narrow screens.
- Keep carousel controls keyboard operable and clearly named. Provide swipe support without making it the only navigation method.
- For an enlarged modal view, provide a visible close control, Escape-to-close, focus management, and return focus to the selected illustration.
- Provide useful alt text and, where needed, a readable text summary of dense illustrated notes.
- Preserve image sharpness when enlarged. Reserve dimensions to prevent layout jumps and load later gallery images as needed.
- Do not add animation beyond what is useful for manual navigation; honor reduced-motion preferences.
- Final contact destination, service details, gallery order, and mobile design remain open. No technology stack is selected by this brief.

## Review checklist

- Professional editorial structure and consistent alignment.
- Full, uncropped original illustrations remain the focus.
- Restrained postcard feeling through paper edges and presentation.
- Pastel Crayon limited to the opening heading; Courier Prime elsewhere.
- Two or three featured drawings plus the full-collection manual carousel.
- Captions remain close to images and align at the top on desktop.
- No autoplay; larger illustration view is available.
- Clear contact invitation using accurate, reviewed copy.

