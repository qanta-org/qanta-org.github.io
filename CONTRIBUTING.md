# Contributing to the QANTA Website

This guide covers how to add and update content on the QANTA website. For setup instructions, see [README.md](README.md).

---

## Table of Contents

1. [Site Overview](#site-overview)
2. [Adding a Page](#adding-a-page)
3. [Layout Reference](#layout-reference)
4. [Front Matter Reference](#front-matter-reference)
5. [Adding to the Nav Bar](#adding-to-the-nav-bar)
6. [Adding a Competition Year](#adding-a-competition-year)
7. [Adding a Research Project](#adding-a-research-project)
8. [Adding a Dataset](#adding-a-dataset)
9. [Adding a Paper](#adding-a-paper)
10. [Adding a News Item](#adding-a-news-item)
11. [Updating Authors](#updating-authors)

---

## Site Overview

Content lives in three places:

| Location | What goes here |
|---|---|
| Markdown files (`.md`) | Page content — prose, headings, links |
| `_data/*.yml` | Structured data — datasets, papers, news, authors, competitions |
| `_includes/*.html` | Reusable template fragments (rendered by layouts and pages) |

Most content additions are just YAML edits to `_data/` or new `.md` files — no HTML required.

---

## Adding a Page

**Where to put it:**

| Page type | Directory |
|---|---|
| Standalone article (guide, explainer) | `articles/` |
| Competition year | `competition/YEAR/` |
| Research project | `research/projects/` |
| Top-level section index | its own directory (e.g., `events/`) |

**Steps:**

1. Create `articles/my-page.md` (or in the appropriate directory).
2. Add front matter — at minimum `layout`, `title`, and `description`:

```yaml
---
layout: article
title: My Page Title
description: One-sentence summary used for SEO and social sharing.
permalink: /my-page/      # optional — defaults to directory path
---
```

3. Write your content in CommonMark Markdown below the `---`.
4. If the page should appear in the nav bar, see [Adding to the Nav Bar](#adding-to-the-nav-bar).

---

## Layout Reference

| Layout | When to use | Column width |
|---|---|---|
| `home` | The site homepage only | Full-width hero |
| `overview` | Section index pages with tables, grids, or card layouts | `col-lg-10` |
| `article` | Single-topic reading-focused pages — guides, project pages, competition sub-pages | `col-lg-8` |

**When in doubt:** use `article` for leaf pages, `overview` for hub/index pages.

---

## Front Matter Reference

All supported front matter fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `layout` | string | **yes** | One of `home`, `overview`, `article` |
| `title` | string | **yes** | Page title — used in `<title>`, nav, headings |
| `description` | string | recommended | One-sentence summary for SEO meta description and Open Graph |
| `permalink` | string | sometimes | Override the generated URL (always set this when moving files) |
| `nav` | boolean | no | `true` → include as a top-level nav link |
| `nav_label` | string | no | Label shown in navbar (defaults to `title`) |
| `nav_order` | integer | no | Left-to-right sort order for nav links (lower = further left) |
| `venue` | string | no | Conference/journal name — shown as a badge on project cards |
| `year` | integer | no | Publication year — used to sort project cards newest-first |
| `badges` | list | no | Badge keys from `_data/badge_config.yml` (e.g., `[dataset, system]`) |
| `authors` | list | no | Author IDs from `_data/authors.yml` — renders an avatar grid via `{% include author-grid.html %}` |

---

## Adding to the Nav Bar

The nav bar has two types of links:

**Dropdowns** (Competition, Research) — managed in `_includes/header.html` and `_data/competitions.yml`. Edit these directly.

**Top-level links** (Data & Code, Get Involved, Events, and any new ones) — data-driven from page front matter. To add a new top-level nav link:

1. Add these fields to the page's front matter:

```yaml
nav: true
nav_label: "My Page"   # label shown in navbar
nav_order: 7           # position (current: Data & Code=4, Get Involved=5, Events=6)
```

2. That's it — no changes to `header.html` needed.

---

## Adding a Competition Year

1. Create a directory `competition/YEAR/` with these files:
   - `index.md` — main competition page (use `layout: overview`)
   - `authors.md` — author guidelines (use `layout: article`)
   - `computer-teams.md` — AI team info (use `layout: article`)
   - `human-teams.md` — human team info (use `layout: article`)

2. Add the year to `_data/competitions.yml`:

```yaml
- year: 2027
  label: "2027"
  current: true   # set current: true on the new year, remove it from the old current
```

3. Update `competition/index.md` to add the previous current year to the past-years table.

---

## Adding a Research Project

1. Create `research/projects/my-project.md` with this front matter:

```yaml
---
layout: article
title: My Project Name
description: One-sentence summary shown on the project card grid.
venue: EMNLP 2027          # conference/journal and year
year: 2027                 # used for card sort order
badges: [dataset, system]  # see _data/badge_config.yml for available keys
authors: [author-id-1, author-id-2]  # see _data/authors.yml
---
```

2. The project card will automatically appear on the [Projects page](/research/projects/) — no template edits needed.

3. Available badge keys (defined in `_data/badge_config.yml`):

| Key | Label | Meaning |
|---|---|---|
| `dataset` | Dataset | Project released a dataset |
| `system` | System | Project released a runnable system |
| `interface` | Interface | Project includes a web interface |
| `ongoing` | Ongoing | Project is actively maintained |

To add a new badge type, add an entry to `_data/badge_config.yml`:

```yaml
my-badge:
  class: badge-secondary   # Bootstrap badge class
  label: My Label
```

---

## Adding a Dataset

Edit `_data/datasets.yml`. Each entry renders automatically on the [Datasets page](/research/datasets/) and the [Data & Code page](/data-and-code/).

```yaml
- id: my-dataset                        # unique slug (used for cross-references)
  name: My Dataset                      # full display name
  short_name: My Dataset                # compact label for tables
  description: One-sentence summary.
  type: tossup                          # tossup | sequential | conversational | adversarial | graph | context
  paper_id: my-paper-id                 # id from papers.yml (optional)
  splits:
    - name: Train
      url: https://...                  # omit url to show "Contact us"
    - name: Test
      url: https://...
  code_url: https://github.com/...      # optional
  license: CC BY-SA 4.0                 # optional
  page: /research/projects/my-project/  # internal link (optional)
  notes: "Any extra note shown in italics."  # optional
```

---

## Adding a Paper

Edit `_data/papers.yml`. Each entry renders in the [Research publications table](/research/).

```yaml
- id: my-paper-2027                   # unique slug (referenced by datasets.yml paper_id)
  title: "Full Paper Title"
  authors: "Author One, Author Two, Jordan Boyd-Graber"
  venue: EMNLP                        # conference/journal abbreviation
  year: 2027
  url: https://aclanthology.org/...   # link to paper
  project_page: /research/projects/my-project/  # optional
  dataset_ids: [my-dataset]           # optional — list of dataset ids introduced by this paper
```

---

## Adding a News Item

Edit `_data/news.yml`. Items render on the home page in order.

**Simple item with a link:**

```yaml
- year: "2027"
  text: "UMD System Wins National Quiz Bowl Championship"
  url: "https://example.com/article"
```

**Item with complex inline HTML** (e.g., multiple links in one line):

```yaml
- year: "Events"
  html: "Spring 2027 exhibition &mdash; <a href=\"/competition/2027/\">details</a>"
```

---

## Updating Authors

Edit `_data/authors.yml`. Author entries are referenced by `id` in project page front matter (`authors: [id1, id2]`) and rendered as an avatar grid via `{% include author-grid.html author_ids=page.authors %}`.

```yaml
- id: my-author
  name: Author Name
  url: https://example.com/author
  image: /assets/images/people/my-author.jpg
```

Place the author photo in `assets/images/people/` as a square image (displayed as a circle, 90px).
