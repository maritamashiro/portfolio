# Mariana Tamashiro — portfolio

A small, portable static website. HTML, CSS, and JavaScript with a Python standard-library build step. No npm dependencies or framework are required.

## Run it

Requires Python 3.12+ (Node is optional, for npm script shortcuts).

```sh
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000. After changes, run the build again and refresh the browser. `npm run build` and `npm run check` are equivalent shortcuts.

## Where to edit

| File or folder | Purpose |
| --- | --- |
| `content/portfolio-project-questions.md` | Homepage project names, questions, and display order |
| `scripts/build.py` | Page content, shared layout, project links, and illustrated SVG tokens |
| `public/style.css` | Palette, typography, layouts, responsive rules, halos |
| `public/site.js` | Mobile menu, image enlargement, manual carousel |
| `public/assets/` | Optimized website assets |
| `public/fonts/` | Self-hosted fonts and their licenses |
| `docs/design/` | Design briefs approved during the mockup phase |
| `docs/content-status.md` | What is implemented and what still needs editorial review |
| `scripts/check.py` | Internal link, fragment, asset, and heading checks |
| `.github/workflows/pages.yml` | Build and deploy to GitHub Pages |
| `dist/` | Generated website, recreated by the build; not committed |

The build uses relative URLs, so the website works both under a GitHub repository path and at a custom domain. Original full-resolution assets and unpublished manuscripts do not belong in this public repository.

## GitHub Pages

1. Create a repository named `portfolio` under `maritamashiro` (a public repository works with GitHub Pages on GitHub Free).
2. Push this project to its `main` branch.
3. In repository **Settings → Pages → Build and deployment**, select **GitHub Actions**.
4. Run **Publish portfolio** from the Actions tab, or push a new commit.
5. The completed deployment reports the live URL. Check it before changing domain settings.
6. Connect `marianatamashiro.com` only when the site is ready; configure the custom domain and its DNS records then.

The first version is published at https://maritamashiro.github.io/portfolio/ from https://github.com/maritamashiro/portfolio. GitHub Actions builds and deploys changes to main. The custom domain has not been connected.

## Fonts

Courier Prime Regular/Bold are the text fonts. DK Cool Crayon is the display face supplied by Mariana, replacing Pastel Crayon. The supplied license PDF and archive metadata are preserved beside the TTF in `public/fonts/`.

## Image provenance

Documentary project images come from Mariana's supplied Xenoflora files and original Wix project pages. Illustration sheets come from her original website. `xenoflora-cutout.webp` is an AI-assisted background extraction of the actual flower photograph, used as a visual token; documentary images remain separate. SVG tokens are provisional drawn symbols, intended to be replaced or refined with Mariana's own illustration assets.

All artwork and portfolio content remain the property of their respective authors. No blanket open-source license is applied to artwork or photographs.
