# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the [QANTA project](https://new.qanta.org) website — a Jekyll-powered static site migrated from Google Sites. Custom theme derived from the Apache Arrow website, deployed via GitHub Actions to GitHub Pages.

## Prerequisites (one-time setup)

| Tool | Version |
|---|---|
| Ruby | 3.3.x or 4.x (see `.ruby-version`) |
| Bundler | 4.0.x (`gem install bundler`) |
| Node.js | 22 LTS (see `.nvmrc`) |

```bash
bundle install   # Jekyll + plugins
npm install      # Bootstrap + Webpack
```

Make sure Homebrew or your version manager Ruby is first in `PATH` — macOS system Ruby (`/usr/bin/ruby`) is too old.

## Development Commands

```bash
# Dev server at http://localhost:4000 (runs Webpack + Jekyll + live reload)
bundle exec rake

# Production build → _site/
JEKYLL_ENV=production bundle exec rake generate
```

> **Never run `bundle exec jekyll serve` directly** — it skips Webpack, which breaks navbar dropdowns and other Bootstrap JS features.

## Architecture

- **Theme**: Custom, derived from the Apache Arrow site — all theme files live in `_layouts/`, `_includes/`, `css/` (not a Ruby gem)
- **JS**: Bootstrap 4 bundled via Webpack 5: `_webpack/main.js` → `javascript/main.js`
- **Build orchestration**: `Rakefile` runs npm → Webpack → Jekyll in the correct order
- **Markdown**: CommonMark (not Kramdown) — inline HTML in `.md` requires `UNSAFE: true` in `_config.yml`
- **Data files**: `_data/datasets.yml` and `_data/papers.yml` drive the datasets and publications pages via Liquid loops
- **Deployment**: GitHub Actions (`.github/workflows/deploy.yml`), **not** GitHub Pages' built-in builder
- **Build output**: `_site/` (gitignored)

## Key Files

| File | Purpose |
|---|---|
| `_config.yml` | Jekyll config (CommonMark + UNSAFE, SASS load paths, plugins, exclude list) |
| `Rakefile` | Build orchestration (npm → Webpack → Jekyll) |
| `_webpack/main.js` | JS entry point: Bootstrap import + table-responsive wrapper + external link handler |
| `css/main.scss` | Bootstrap SCSS import + QANTA brand overrides |
| `_layouts/` | `home`, `article`, `overview` (3 layouts — see Layout Reference below) |
| `_includes/header.html` | Nav bar — dropdowns hardcoded; simple links auto-rendered from `nav: true` front matter |
| `_includes/footer.html` | Footer credits |
| `_includes/top.html` | `<head>`: favicons, Inter font, Bootstrap Icons CDN, CSS/JS links |
| `_data/datasets.yml` | Dataset catalog: name, description, splits + URLs, license, paper ref |
| `_data/papers.yml` | Publications: title, authors, venue, year, URL |
| `CNAME` | Custom domain (`new.qanta.org`) |

## Content Structure

```
index.md                              # home layout — hero, quick links, news
CNAME                                 # new.qanta.org

# Standalone articles (one-off pages not belonging to a section)
articles/data-and-code.md             # GitHub repos, datasets table, CodaLab leaderboard
articles/get-involved.md              # volunteer, annotate, contribute
articles/stump-a-computer.md          # how adversarial questions work

# Competitions (one subdir per year, current first)
competition/index.md                  # overview + archive list
competition/2026/index.md             # current: first multimodal competition (text + images)
competition/2026/authors.md
competition/2026/computer-teams.md
competition/2026/human-teams.md
competition/2025/index.md             # past: Human–AI Cooperative QA
competition/2025/authors.md
competition/2025/computer-teams.md
competition/2025/human-teams.md
competition/2024/index.md
competition/2023/index.md
competition/2018/index.md

# Research (persistent academic output)
research/index.md                     # overview + publications table (from _data/papers.yml)
research/datasets.md                  # dataset catalog (from _data/datasets.yml)
research/projects/index.md            # project card grid (auto-populated from project pages)
research/projects/adversarial.md      # TACL 2019
research/projects/qblink.md           # EMNLP 2018
research/projects/canard.md           # EMNLP 2019
research/projects/delft.md            # WWW 2020

# Events and developer docs
events/index.md                       # full event timeline 2015–present
docs/content-guide.md                 # content editor reference
docs/theme-customization.md           # developer theming reference

# Data files (single source of truth — update once, reflected everywhere)
_data/datasets.yml                    # consumed by research/datasets.md + articles/data-and-code.md
_data/papers.yml                      # consumed by research/index.md
_data/competitions.yml                # drives Competition dropdown in nav
_data/news.yml                        # home page news/press items
_data/authors.yml                     # author avatars for research project pages
_data/badge_config.yml                # badge key → CSS class + label mapping
```

### Nav structure

```
Home | Competition ▾ | Research ▾ | Data & Code | Get Involved | Events
       2026 (current)  Projects
       Past Years      Datasets
```

**Competition dropdown**: driven by `_data/competitions.yml` (`current: true` sets the current year).
**Simple top-level links** (Data & Code, Get Involved, Events): auto-rendered from pages with `nav: true` in front matter, sorted by `nav_order`. To add a new top-level link, set `nav: true`, `nav_label`, and `nav_order` in the page's front matter.

### Layout Reference

| Layout | Use for | Width |
| --- | --- | --- |
| `home` | Site homepage only | Full-width hero |
| `overview` | Index/catalog/hub pages with tables, grids, or cards | `col-lg-10` |
| `article` | Single-topic reading-focused pages — guides, project pages, competition sub-pages | `col-lg-8` |

## Data Files

### Adding a dataset (`_data/datasets.yml`)

```yaml
- id: my-dataset
  name: My Dataset
  short_name: My Dataset          # used in compact tables
  description: One sentence.
  type: tossup                    # tossup | sequential | conversational | adversarial | graph | context
  paper_id: my-paper-id           # matches id in papers.yml (optional)
  splits:
    - name: Train
      url: https://...            # omit url to show "Contact us"
    - name: Test
      url: https://...
  code_url: https://github.com/...
  license: CC BY-SA 4.0
  page: /research/projects/my-project/
  notes: "Any extra note shown in italics."
```

### Adding a paper (`_data/papers.yml`)

```yaml
- id: my-paper-id
  title: "Full Paper Title"
  authors: "Author One, Author Two, Jordan Boyd-Graber"
  venue: EMNLP
  year: 2026
  url: https://aclanthology.org/...
  project_page: /research/projects/my-project/
  dataset_ids: [my-dataset]
```

## Theme Customization

| What to change | Where |
|---|---|
| Nav links | `_includes/header.html` |
| Footer | `_includes/footer.html` |
| Colors / fonts | `css/main.scss` (Bootstrap SCSS variables) |
| Home hero | `_layouts/home.html` |
| Favicons | `assets/images/favicon/` + `_includes/top.html` |
| Current competition | `competition/index.md` + `_layouts/home.html` CTA button |

Brand colors: `$primary: #CC412F` (rust red), `$dark: #3A3A3A` (charcoal), `$body-bg: #F0F0F0`.

See `docs/theme-customization.md` for full details.

## Gotchas

- `javascript/main.js` is gitignored and built by Webpack — Rake enforces this; bypassing Rake with direct `jekyll serve` breaks the build
- CommonMark's `UNSAFE: true` is required for inline HTML in Markdown to render
- Bootstrap 4 SCSS emits Dart Sass deprecation warnings — warnings only, not errors; build succeeds
- The GitHub Actions workflow must trigger builds — GitHub Pages' built-in builder cannot run the Webpack step
- When adding a new competition year, update `competition/index.md` (move old current to past table) **and** the CTA button in `_layouts/home.html`
- `_data/` YAML indentation must be consistent — Jekyll silently skips malformed entries

## Skills Reference

| Skill | Required for |
|---|---|
| Jekyll 4 (Liquid, layouts, includes, front matter) | All content and template work |
| Bootstrap 4 (grid, navbar, dropdowns, cards) | Customizing nav, layout, and responsive design |
| SCSS/Sass (variable overrides before `@import`) | Branding/color changes |
| CommonMark Markdown | Content authoring |
| Bundler / Ruby 3.3+ | Running the build |
| Node.js 22 LTS + npm | Webpack setup; required at build time |
| Rake | Understanding build task orchestration |
| GitHub Actions | Modifying the deploy pipeline |
| Jekyll `_data/` YAML | Updating datasets and publications |

## Further Documentation

- `docs/content-guide.md` — for content editors (front matter, layouts, nav wiring, Markdown conventions)
- `docs/theme-customization.md` — for developers modifying visual design (SCSS theming, Webpack, layouts)
