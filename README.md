# jeffreymaggard.com

Static portfolio site. Plain HTML/CSS, no build step.

- `site/`: everything that is deployed
- `docs/site-package.md`: source of truth for design, copy and facts
- `docs/home-design-reference.dc.html`: approved Home page design

## Preview locally

    python3 -m http.server 8080 -d site

## Deploy (Cloudflare Pages)

Needs `CLOUDFLARE_API_TOKEN` (Cloudflare Pages: Edit) and `CLOUDFLARE_ACCOUNT_ID` set in the environment.

    npx wrangler pages deploy site --project-name jeffreymaggard --branch main

Preview: https://jeffreymaggard.pages.dev
