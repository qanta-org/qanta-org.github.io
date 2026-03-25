# Assets

Static assets for the QANTA website. All paths are relative to `assets/` and referenced in templates as `{{ site.baseurl }}/assets/...`.

## Directory Structure

```
assets/
  images/
    branding/     # Logo, wordmark, and brand assets
    heroes/       # Full-width hero/banner images
    projects/     # Research figures, diagrams, system architecture images
    people/       # Author and team headshots
    events/       # Event photos, competition action shots
  pdfs/           # Papers, guides, and downloadable documents
```

---

## images/people

Headshots used on project pages and team listings. Target: 400×400px or larger, square crop.

| File | Person | Source | Used on |
|---|---|---|---|
| `jordan-boyd-graber.png` | Jordan Boyd-Graber | cs.umd.edu/~jbg | research/index.md, adversarial project |
| `eric-wallace.jpg` | Eric Wallace | ericswallace.com | adversarial project |
| `shi-feng.jpg` | Shi Feng | shi-feng.super.site | adversarial project |
| `pedro-rodriguez.jpg` | Pedro Rodriguez | GitHub avatar | adversarial project |
| `ikuya-yamada.jpg` | Ikuya Yamada | GitHub avatar | adversarial project |

**To add a headshot:** Drop a square-cropped JPG/PNG (≥ 400×400) into `people/`, then reference it as:
```html
<img src="{{ site.baseurl }}/assets/images/people/filename.jpg" alt="Name"
     class="rounded-circle" style="width:80px;height:80px;object-fit:cover;">
```

---

## images/branding

| File | Description | Status |
|---|---|---|
| `qanta-logo.png` | Full QANTA wordmark/logo | **Needed** — source on Google Sites requires auth |

Favicons live in `assets/images/favicon/`, referenced by `_includes/top.html`:
- `assets/images/favicon/favicon-32x32.png`
- `assets/images/favicon/favicon-16x16.png`
- `assets/images/favicon/apple-touch-icon.png`

**To generate favicons:** Upload a square logo to [realfavicongenerator.net](https://realfavicongenerator.net), download the package, and drop the files into `assets/images/favicon/`.

---

## images/heroes

Full-width banner images used as section backgrounds or featured visuals.

| File | Description | Status |
|---|---|---|
| `home-hero.jpg` | Home page hero banner | **Needed** — source on Google Sites requires auth |
| `competition-2025.jpg` | 2025 competition visual | **Needed** — source on Google Sites requires auth |

Google Sites images are behind auth and cannot be downloaded via script. To retrieve them: open the Google Sites page in a browser, right-click the image → Save As, then place it here.

---

## images/projects

Research figures, paper diagrams, system architecture illustrations.

| File | Description | Status |
|---|---|---|
| `delft-diagram.jpg` | DELFT graph-based QA architecture | **Needed** — source on Google Sites requires auth |

To add a figure from a paper: use the published PDF version (CC BY or fair use for research) and export at ≥ 1280px wide.

---

## images/events

Event photos, competition action shots, venue photos.

Currently empty. Photos from past competitions (2018 NeurIPS, 2023, 2025) can be added here as they become available.

---

## pdfs

PDFs linked from content pages (papers, guides, handouts).

Currently empty. When adding a PDF, also update `_data/datasets.yml` or the relevant content page with a link to `{{ site.baseurl }}/assets/pdfs/filename.pdf`.
