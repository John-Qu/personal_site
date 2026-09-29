# AGENTS.md

Guidance for AI coding agents working in this repository.

## Project overview

This repository hosts the Markdown source of **John Qu's personal website** (`https://johnqu.site/`), a bilingual (primarily Chinese) static blog. It is built with [blogdown](https://github.com/rstudio/blogdown), the R package that wraps the [Hugo](https://gohugo.io/) static site generator, and uses Yihui Xie's **hugo-ivy** theme (`themes/hugo-ivy`, vendored in-repo). All page content is licensed under CC BY-NC-SA 4.0.

The site has four content sections:

- `content/cn/` — Chinese blog posts (~650 files)
- `content/cn-note/` — Chinese notes (shorter form)
- `content/en/` — English posts
- `content/mit6000/` — MIT 6.0001/6.0002 course book notes; some of these are `.Rmd` files that are knitted (Python/R code chunks) before Hugo builds

Root-level pages in `content/` (`_index.md`, `cn-resume.md`, `cn-vitae.md`, `cn-about.md`, `en-about.md`, plus PDF/DOCX/RTF resume artifacts) render as standalone pages such as the homepage and resume.

## Technology stack

- **Hugo** `v0.147.3+extended` (installed via Homebrew at `/opt/homebrew/bin/hugo`); config in `config.toml` (TOML format, no YAML config)
- **blogdown** R package — declared in `index.Rmd` (`site: blogdown:::blogdown_site`) and the RStudio project file `johnqu_site.Rproj` (`BuildType: Website`)
- **R / knitr / rmarkdown** — for `.Rmd` posts under `content/mit6000/`; knitted output (`.html` + `*_files/`) is committed alongside the source
- **Python via reticulate** — `.Rprofile` sets `RETICULATE_PYTHON` to a virtualenv (`mit600env/`, gitignored) used for Python code chunks in the MIT 6000 notes
- Custom JS in `static/js/` (TOC fixes, image centering, footnote fixes, math code, external-link handling, etc.), listed in `config.toml` under `params.customJS`
- Custom CSS override at `static/css/custom.css`

## Build and serve commands

```bash
hugo server          # local preview with live reload
hugo                 # build the site into public/
```

`public/` (577M, includes rendered images) and `static/` (542M) are large; `public/`, `mit600env/`, and `content/ref` are gitignored. There is **no CI configuration and no deployment script in the repo** — the site is built locally and deployed manually by the owner (the deployment target/pipeline is not recorded in this repository; do not invent one).

If R is available, blogdown equivalents are `blogdown::serve_site()` and `blogdown::build_site()`. When editing `.Rmd` posts, the rendered `.html` and `*_files/` directories must be regenerated (via knitr/blogdown) before running `hugo`, because Hugo ignores raw `.Rmd`/`*_files`/`*_cache` paths (`ignoreFiles` in `config.toml`).

Note: on a fresh machine R itself may not be installed; Hugo alone can build the site, but `.Rmd` posts will only reflect their last committed knitted output.

## Content conventions

- **Front matter is YAML** with `title`, `date`, `slug`, `tags`, `categories`, often `author` and `typora-root-url: ../../static` (the author writes in Typora; image paths resolve into `static/`).
- **File naming**: posts are named `YYYY-MM-DD-title.md` (date-prefixed). The `date` in front matter is authoritative for ordering; permalinks are `/cn/:year/:month/:slug/` etc. per section (`[permalinks]` in `config.toml`).
- **Images** live in `static/images/<post-slug>/` and are referenced as `/images/...`. Do not put images in `content/`.
- **Section menus** are defined per-section (`[[menu.cn]]`, `[[menu.en]]`, `[[menu.cn-note]]`, `[[menu.MIT6000]]`, `[[menu.Reference]]`) — when adding a section, update its menu block too.
- Draft/expired/future posts are not built (`buildDrafts/buildFuture/buildExpired = false`).
- Hugo renders unsafe HTML (Goldmark `unsafe = true`) and TOCs from level 2–4.
- New posts can be scaffolded with `hugo new` using `archetypes/default.md`.

## Layout overrides

The vendored theme is at `themes/hugo-ivy/`. Site-specific overrides live in the top-level `layouts/` directory (Hugo merges these over the theme):

- `layouts/_default/list.html` — archive-style list page grouped by year
- `layouts/partials/foot_custom.html` — prev/next post navigation
- `layouts/partials/head_custom.html` — loads `/css/custom.css`
- `layouts/partials/disqus.html` — comment partial
- `layouts/shortcodes/center.html` — `{{< center >}}` shortcode for centered content

Prefer adding overrides in top-level `layouts/`/`static/` rather than editing `themes/hugo-ivy/` directly.

## Git workflow

- Remote: `git@github.com:John-Qu/personal_site.git`, default branch `master`.
- Long-lived topic branches exist (`change-menu`, `try-to-add-note-dir`, `withref`, `writing`); commit directly to `master` unless told otherwise.
- Commit messages are written in **Chinese**; match that convention.
- The site content language is primarily Chinese — keep existing Chinese titles/tags/categories intact when editing posts.

## Testing

There is no automated test suite. Verification is:

1. `hugo` builds without errors (watch for broken shortcodes/front matter).
2. `hugo server` and manually checking affected pages.
3. For `.Rmd` changes: re-knit and confirm the rendered HTML is updated before building.

## Security / privacy considerations

- `config.toml` contains a Valine comment-system `appId`/`appKey` (`[params.valine]`). These are already public on the live site; do not treat them as secret, but do not expose additional credentials.
- Never commit `.env`-style files, SSH keys, or the gitignored `mit600env/` virtualenv.
- Resume files and personal PDFs under `content/` are intentionally public site assets.
- Large binary assets (images, PDFs) are committed to git as part of `static/` — keep that pattern rather than introducing external asset hosting.
