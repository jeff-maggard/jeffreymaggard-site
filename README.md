# jeffreymaggard.com

Static portfolio site. Plain HTML/CSS, no build step.

- `site/`: everything that is deployed
- `docs/site-package.md`: source of truth for design, copy and facts
- `docs/home-design-reference.dc.html`: approved Home page design

## Preview locally

    python3 -m http.server 8080 -d site

## Deploy (Cloudflare Pages)

The Cloudflare Pages project `jeffreymaggard-site` is connected to this repo. Every push to `main` deploys automatically. There is no build command, and the output directory is `site`.

Preview: https://jeffreymaggard-site.pages.dev
