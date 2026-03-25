---
layout: article
title: Theme Customization
description: Guide for developers modifying the QANTA site's visual design, SCSS theming, and Webpack build pipeline.
---

This guide is for developers who want to modify the visual design or build pipeline.

## Overview

The theme is a custom fork of the [Apache Arrow website](https://arrow.apache.org) theme. All theme files live directly in the repository (not in a gem), so every file is editable.

## Bootstrap SCSS Theming

Bootstrap 4 is imported via SCSS in `css/main.scss`. To override Bootstrap variables, define them **before** the `@import`:

```scss
// css/main.scss

// --- QANTA brand overrides ---
$primary:                #CC412F;   // burnt orange/rust — matches qanta.org
$dark:                   #3A3A3A;   // charcoal — nav bar, footer
$body-bg:                #F0F0F0;   // light gray page background
$body-color:             #212121;   // near-black body text
$font-family-sans-serif: "Source Sans Pro", sans-serif;

// --- Bootstrap core ---
@import "bootstrap/scss/bootstrap";

// --- Site-specific styles below ---
```

The full list of Bootstrap 4 SCSS variables is in `node_modules/bootstrap/scss/_variables.scss`.

### QANTA Brand Colors

Derived from the existing qanta.org (Google Sites) stylesheet:

| Token | Hex | Use |
|---|---|---|
| Primary | `#CC412F` | Buttons, links, active nav, accents |
| Dark | `#3A3A3A` | Nav bar background, footer |
| Background | `#F0F0F0` | Page background |
| Surface | `#FFFFFF` | Cards, content panels |
| Text | `#212121` | Body text |

Update these in `css/main.scss` as the brand evolves.

## Adding a New Layout

1. Create `_layouts/your-layout.html`.
2. Start with a front matter block specifying which layout it extends:

```html
---
layout: default
---

<div class="container">
  {{ content }}
</div>
```

3. Reference it in a page's front matter: `layout: your-layout`.

## Modifying the Webpack Bundle

JavaScript lives in `_webpack/main.js` and is bundled by Webpack 5 into `javascript/main.js`.

To add a new JS dependency:

1. Install it: `npm install some-package`
2. Import it in `_webpack/main.js`:

```js
import 'some-package';
```

3. Run `bundle exec rake` — Webpack will re-bundle automatically.

Webpack config is in `webpack.config.js`. The entry point is `_webpack/main.js`; the output is `javascript/main.js`. Do not edit `javascript/main.js` directly — it is generated and will be overwritten on the next build.

## Modifying the Nav

Edit `_includes/header.html`. The nav uses Bootstrap 4 navbar markup with dropdown support.

To add a dropdown:

```html
<li class="nav-item dropdown">
  <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown">
    Section Name
  </a>
  <div class="dropdown-menu">
    <a class="dropdown-item" href="{{ site.baseurl }}/page-one/">Page One</a>
    <a class="dropdown-item" href="{{ site.baseurl }}/page-two/">Page Two</a>
  </div>
</li>
```

Dropdowns require the Bootstrap JS bundle, which is provided by Webpack. This is why running `bundle exec jekyll serve` directly (without Rake) breaks dropdowns.

## Build Pipeline Details

`Rakefile` defines the following tasks:

| Task | What it does |
|---|---|
| `rake` (default) | Runs `webpack` then `jekyll serve --watch` |
| `rake generate` | Runs `webpack` then `jekyll build` (for production) |
| `rake webpack` | Runs Webpack only |

The ordering is intentional: `javascript/main.js` must exist before Jekyll tries to copy it into `_site/`.

## GitHub Actions Deploy

The deploy workflow lives at `.github/workflows/deploy.yml`. It:

1. Checks out the repo
2. Sets up Ruby and Node.js
3. Runs `bundle install` + `npm install`
4. Runs `JEKYLL_ENV=production bundle exec rake generate`
5. Pushes `_site/` to the `gh-pages` branch (or deploys via Pages artifact)

GitHub Pages' built-in Jekyll builder is **disabled** — a `.nojekyll` file (or equivalent Pages config) prevents it from running. All builds go through the Actions workflow.
