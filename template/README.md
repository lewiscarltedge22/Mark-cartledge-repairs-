# One-Trader Business Website — Base Template

This is a genericized copy of the MC Property Repairs site, stripped of all
business-specific content so it can be reused as the starting point for a
future single-owner trade/service business site. No build tooling — plain
HTML/CSS/JS, one self-contained file per page, deployable as-is to Vercel,
Netlify, GitHub Pages, or any static host.

## What's included

| File | Purpose |
|---|---|
| `index.html` | Homepage — hero, pride-quote section, services grid, reviews |
| `about.html` | About/bio page with a personal quote and stats strip |
| `work.html` | Gallery hub — mix of inline-lightbox tiles and links to project sub-pages |
| `project-page-template.html` | Copy this once per trade that has multiple distinct jobs (e.g. `bathroom.html`, `kitchen.html`) — shows a grid of project cards, each opening its own before/after photo lightbox |
| `contact.html` | Contact page with a working quote form (see setup below) |
| `robots.txt` / `sitemap.xml` | Basic SEO plumbing |
| `images/favicon.svg` | Placeholder favicon — edit initials/colors, or regenerate with the script below |
| `scripts/generate-favicon.py` | Regenerates `favicon.ico`, `favicon-16.png`, `favicon-32.png`, `apple-touch-icon.png` for a new brand |

## Design system

All colors/spacing are CSS custom properties in each page's `:root` block —
change them once per page (or extract to a shared `theme.css` if you want a
single source of truth across pages):

```
--ink       body text
--charcoal  headings, dark panels, footer
--slate     muted/secondary text
--brick     accent color (buttons, links, highlights)
--brick-dark  accent hover state
--cream     page background
--cream-dim alternate light background
--white     cards
--line      borders
--radius    corner radius (6px)
--max       content max-width (1180px)
```

Fonts: Poppins (headings/buttons/logo), Inter (body), Caveat (cursive —
signature-style flourishes only). Loaded via a single Google Fonts `<link>`
in each `<head>`; drop the `Caveat` family if you don't use a signature.

## Patterns to know

- **Photo lightbox** (`work.html`, `project-page-template.html`): a
  `photoSets` object (or `projects` array) of `{src, tag, caption}`, with
  `openExplorer`/`closeExplorer`/`stepExplorer` handling a fullscreen
  overlay, keyboard nav (Escape/arrows), and click-outside-to-close.
- **Single-job vs multi-job trades**: a trade with one completed job gets an
  inline tile on `work.html` (`onclick="openExplorer(...)"`, see the
  Plastering tile). A trade with multiple distinct jobs gets its own page
  copied from `project-page-template.html`, with a `<a href="...">` tile on
  `work.html` instead.
- **Mobile nav**: a hamburger toggle at 920px that slides the nav links down;
  same three lines of JS at the bottom of every page.
- **`color-scheme: light` meta tag + CSS**: prevents Android/Chrome's
  forced-dark-mode heuristic from recoloring the light theme unpredictably.
  Keep this on every page.

## Setup checklist for a new project

1. **Find and replace placeholders** across all HTML files:
   - `[Owner Name]`, `[Business Name]`, `[XX]` (logo/favicon initials)
   - `07000 000000` / `07000000000` / `447000000000` (phone, in three formats
     — plain, tel: link, WhatsApp international format)
   - `you@example.com`
   - `[Your Town]`, `[Your County]`
   - `your-domain.example` (in `robots.txt`, `sitemap.xml`, and the JSON-LD
     block in `index.html`)
2. **Swap in real photos** — replace the `images/example-*` paths in
   `project-page-template.html` and the gallery tile paths in `work.html`,
   write real captions (see the crop tip below), and duplicate
   `project-page-template.html` once per multi-job trade.
3. **Write real copy** — the About page bio paragraph and the two example
   reviews are marked with `[...]` placeholders; replace with the real
   owner's story and real customer quotes.
4. **Regenerate the favicon** — edit `scripts/generate-favicon.py`'s CONFIG
   block (initials + colors) and run it, or just edit `favicon.svg` by hand
   for a quick placeholder.
5. **Wire up the contact form** — it posts to Web3Forms
   (`api.web3forms.com/submit`). Get a free access key at web3forms.com (just
   an email address, no account) and paste it into `contact.html` in place
   of `YOUR_WEB3FORMS_ACCESS_KEY`.
6. **Turn on analytics** — the Vercel Web Analytics snippet
   (`/_vercel/insights/script.js`) is already on every page; enable Web
   Analytics in the Vercel project's dashboard (free tier) to activate it.
7. **Update `sitemap.xml`** with one `<url>` per page you actually publish,
   including each project sub-page.
8. **Structured data** — update the JSON-LD block in `index.html` (name,
   phone, email, address, description) so Google can show rich results.
9. Once there's a real Google Business Profile, consider embedding a live
   reviews widget/map instead of (or alongside) the static review cards.

## Photo cropping tip (from real use)

If working from customer WhatsApp/Facebook screenshots, they often have a
status bar, header, or app chrome baked in. A quick Pillow crop removes it:
sample average row brightness across the image width, find where it
transitions from dark (chrome) to bright (photo) at the top and bottom, and
crop to that bounding box. Worked reliably across multiple photo batches on
the original site.
