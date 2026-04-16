# QANTA Website

Website for the [QANTA project](https://new.qanta.org), hosted at GitHub Pages. Built with Jekyll 4, Bootstrap 4, and Webpack 5. Custom theme derived from the Apache Arrow website.

---

## Tool Requirements

| Tool | Version | Notes |
|---|---|---|
| Ruby | 3.3.x or 4.x | See `.ruby-version` (3.3.7); Ruby 4.0.x also works |
| Bundler | 4.0.x | Installed automatically via `gem install bundler` |
| Node.js | 22 LTS | See `.nvmrc` (`lts/*`, currently v22) |
| npm | 10.x | Bundled with Node.js 22 |
| Jekyll | See Gemfile | Installed via Bundler |
| Webpack | 5.x | Installed via npm |

---

## Setup (First Time)

### 1. Install Ruby

**macOS (recommended: Homebrew)**
```bash
brew install ruby
# Add to your shell profile so Homebrew Ruby takes precedence:
echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**Or use a version manager:**
```bash
# rbenv
brew install rbenv
rbenv install 3.3.7   # matches .ruby-version
rbenv global 3.3.7

# asdf
asdf plugin add ruby
asdf install ruby 3.3.7
asdf global ruby 3.3.7
```

### 2. Install Bundler

```bash
gem install bundler
```

### 3. Install Node.js

**nvm (recommended):**
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
nvm install --lts   # installs v22 LTS, matches .nvmrc
nvm use --lts
```

**Or Homebrew:**
```bash
brew install node@22
```

### 4. Install project dependencies

```bash
bundle install   # Ruby gems (Jekyll, plugins)
npm install      # Node packages (Bootstrap, Webpack)
```

---

## Running Locally

```bash
bundle exec rake
```

Opens at **http://localhost:4000**. The server auto-reloads on file changes.

> **Do not** run `bundle exec jekyll serve` directly — it skips the Webpack build and breaks Bootstrap JS features (navbar dropdowns, etc.).

### Production build (generates `_site/`)

```bash
JEKYLL_ENV=production bundle exec rake generate
```

---

## Deployment

Deployment is fully automated via GitHub Actions (`.github/workflows/deploy.yml`). On every push to `main`:

1. Ruby and Node.js are installed
2. `bundle install` and `npm ci` run
3. `JEKYLL_ENV=production bundle exec rake generate` builds `_site/`
4. `_site/` is deployed to GitHub Pages

**GitHub Pages' built-in Jekyll builder is disabled** — builds go exclusively through the Actions workflow because the built-in builder cannot run the Webpack step.

The site is served at the custom domain `new.qanta.org` via the `CNAME` file.

---

## Content Overview

```
index.md                              # Home page
competition/
  index.md                           # Competition archive
  2026/index.md                      # Current — first multimodal competition
  2025/index.md                      # Past — Human–AI Cooperative QA
research/
  index.md                           # Research overview + publications
  projects/index.md                  # Project card grid
  projects/{qblink,canard,delft,adversarial}.md
data-and-code.md                     # Repos, datasets, leaderboard
get-involved.md
events/index.md
stump-a-computer.md
```

### Data files (edit to update datasets and papers everywhere)

```
_data/datasets.yml    # Dataset catalog — name, description, splits, download URLs, license
_data/papers.yml      # Publication list — title, authors, venue, year, URL
```

These are consumed by `research/index.md` and `data-and-code.md` via Liquid loops. Updating the YAML automatically updates both pages.

---

## Documentation

- `CLAUDE.md` — architecture, key files, and gotchas (for AI-assisted development)
- `docs/content-guide.md` — adding and editing pages (for content editors)
- `docs/theme-customization.md` — modifying the theme, SCSS, and Webpack bundle (for developers)

---

## Troubleshooting

**`bundle exec rake` fails with Ruby version error**
Make sure Homebrew (or your version manager) Ruby is first in `PATH`. The system Ruby on macOS is too old:
```bash
which ruby          # should NOT be /usr/bin/ruby
ruby --version      # should be 3.3.x or 4.x
```

**`npx webpack` not found**
Make sure Node.js is active before running Rake:
```bash
nvm use --lts
bundle exec rake
```

**Sass deprecation warnings**
Bootstrap 4's SCSS uses some deprecated Dart Sass APIs. These are warnings only — the build succeeds. They will be resolved when Bootstrap 5 is adopted.

**`javascript/main.js` missing**
This file is built by Webpack and is gitignored. Run `bundle exec rake` (not `jekyll serve`) to generate it before a Jekyll build.
