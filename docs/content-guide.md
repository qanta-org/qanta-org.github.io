# Content Guide

This guide is for content editors who want to add or update pages without touching the build system.

## Prerequisites

Follow the setup in `CLAUDE.md`, then start the local dev server:

```bash
bundle exec rake
```

Open `http://localhost:4000` in your browser. The server auto-reloads when files change.

## Front Matter

Every content page starts with a YAML front matter block:

```yaml
---
layout: article        # required — see layouts below
title: "Page Title"    # used in <title> and page headings
---
```

### Available Layouts

| Layout | Use for |
|---|---|
| `home` | The main landing page (`index.md`) |
| `article` | Standard content pages (most pages) |
| `overview` | Section index pages (e.g. `projects/index.md`) |
| `post` | Blog/news posts |

## Site Structure

```
index.md                              # Home
competition/index.md                  # Competition overview + archive
competition/2025/index.md             # Current year (+ authors, teams subpages)
competition/2024/index.md             # Past year recap
research/index.md                     # Research overview
research/datasets.md                  # All datasets
research/projects/index.md            # Projects grid
research/projects/qblink.md           # Individual project pages
data-and-code.md                      # GitHub repos, CodaLab, downloads (top-level nav)
stump-a-computer.md                   # Human challenge
get-involved.md                       # Volunteer / contribute
events/index.md                       # Seminars, workshops
resources.md                          # Papers, tools, external links
```

### Nav layout

```
Home | Competition ▾ | Research ▾ | Data & Code | Get Involved | Events
       2025 (current)   Projects
       Past Years       Datasets
```

`Data & Code` is a top-level nav link (not a dropdown) pointing directly to `data-and-code.md`.

## Adding a New Page

1. Create a Markdown file at the path that matches the structure above.
2. Add the required front matter (at minimum `layout` and `title`).
3. Write your content below the front matter.
4. Wire it into the nav — edit `_includes/header.html` and add a link in the appropriate section.

Example minimal page:

```markdown
---
layout: article
title: "Get Involved"
---

Content goes here.
```

### Adding a new competition year

1. Create `competition/YYYY/index.md` (copy from the previous year and update).
2. Add a link to it in the "Past Years" dropdown in `_includes/header.html`.
3. Update `competition/index.md` to include it in the archive list.

### Adding a new research project

1. Create `research/projects/your-project.md` with `layout: article`.
2. Add a card for it in `research/projects/index.md`.
3. No nav change needed — projects live under the Research dropdown.

## Markdown Conventions (CommonMark)

This site uses **CommonMark**, not GitHub Flavored Markdown or Kramdown. Key differences:

- **Inline HTML renders** — but only because `UNSAFE: true` is set in `_config.yml`. Do not remove that setting.
- **Footnotes** — CommonMark does not support `[^1]` footnote syntax by default. Avoid them or use inline HTML.
- **Tables** — use the standard pipe syntax; these are supported via the `table` extension in `_config.yml`.
- **Heading IDs** — auto-generated from heading text (lowercase, spaces → hyphens).

## Images

1. Put image files in the `img/` directory.
2. Reference them in Markdown using the `site.baseurl` variable so paths work in all environments:

```markdown
![Alt text]({{ site.baseurl }}/img/filename.png)
```

Or in HTML (useful for controlling size):

```html
<img src="{{ site.baseurl }}/img/filename.png" alt="Alt text" width="400">
```

## Wiring a Page into the Nav

Edit `_includes/header.html`. Nav links use Bootstrap 4 markup. To add a top-level link:

```html
<li class="nav-item">
  <a class="nav-link" href="{{ site.baseurl }}/your-page/">Your Page</a>
</li>
```

To add a dropdown group, follow the existing dropdown pattern in `header.html`.

## Liquid Templating

Jekyll uses [Liquid](https://shopify.github.io/liquid/) for templating. In content files you can use:

```liquid
{{ site.title }}          — site title from _config.yml
{{ site.baseurl }}        — base URL prefix (important for links and images)
{{ page.title }}          — current page title
```

Avoid complex Liquid logic in content files; keep that in `_layouts/` and `_includes/`.
