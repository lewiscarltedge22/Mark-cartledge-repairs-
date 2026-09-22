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
| `llms.txt` | Plain-text/markdown summary of the business for AI assistants and answer engines (AEO) to cite from |
| `images/favicon.svg` | Placeholder favicon — edit initials/colors, or regenerate with the script below |
| `images/og-image.png` | Placeholder 1200x630 social share image — regenerate with the script below |
| `scripts/generate-favicon.py` | Regenerates `favicon.ico`, `favicon-16.png`, `favicon-32.png`, `apple-touch-icon.png` for a new brand |
| `scripts/generate-og-image.py` | Regenerates `images/og-image.png` for a new brand |

## SEO / AEO / social sharing — what's already wired in

Every page already has (all using placeholder values — see the checklist below):

- Canonical `<link>`, `theme-color`, and unique `<title>`/meta description
- Open Graph tags (`og:title`, `og:description`, `og:image`, `og:url`, `og:type`, `og:site_name`, `og:locale`) and Twitter Card tags, so shared links get a proper preview card on Facebook, WhatsApp, LinkedIn, X, iMessage, etc.
- A `BreadcrumbList` JSON-LD block matching the page's position in the site
- `index.html` carries an expanded `HomeAndConstructionBusiness` JSON-LD block with a stable `@id`, a `hasOfferCatalog` listing every service, and an `image` array — swap that array for real photos once you have them
- `project-page-template.html` carries a `Service` JSON-LD block (`provider` references the homepage's `@id`) — update its `name`/`description` per trade when you duplicate the page
- `contact.html` carries a visible FAQ section with matching `FAQPage` JSON-LD — the questions are safe to reuse, but the placeholder answers must be replaced with facts that are actually true of the new business (never invent an insurance status, response time, etc.)
- `llms.txt` at the project root, for AI answer engines

**Deliberately left out:** `AggregateRating`/review-star schema. Only add that once there are genuine star-rated reviews to back it up — Google's structured data guidelines treat a fabricated rating as a policy violation, and it's straightforwardly dishonest besides.

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

1. **Find and replace placeholders** across all HTML files (and `llms.txt`):
   - `[Owner Name]`, `[Business Name]`, `[XX]` (logo/favicon initials)
   - `07000 000000` / `07000000000` / `447000000000` (phone, in three formats
     — plain, tel: link, WhatsApp international format)
   - `you@example.com`
   - `[Your Town]`, `[Your County]`
   - `your-domain.example` — appears a LOT: canonical links, `og:url`,
     `og:image`, `twitter:image`, every JSON-LD block, `robots.txt`,
     `sitemap.xml`, `llms.txt`. A single find-and-replace across the whole
     folder for this one is worth doing first.
   - `[Trade Category]` / `[Trade]` / `PAGE-NAME.html` in each copy of
     `project-page-template.html` (title, meta description, breadcrumb,
     Service schema, hero heading)
2. **Swap in real photos** — replace the `images/example-*` paths in
   `project-page-template.html` and the gallery tile paths in `work.html`,
   write real captions (see the crop tip below), and duplicate
   `project-page-template.html` once per multi-job trade. Once you have real
   photos, also swap them into `index.html`'s JSON-LD `image` array.
3. **Write real copy** — the About page bio paragraph and the two example
   reviews are marked with `[...]` placeholders; replace with the real
   owner's story and real customer quotes.
4. **Regenerate the favicon and social share image** — edit
   `scripts/generate-favicon.py` and `scripts/generate-og-image.py`'s CONFIG
   blocks (initials, business name, colors) and run both, or edit
   `favicon.svg`/`og-image.png` by hand for a quick placeholder.
5. **Wire up the contact form** — it posts to Web3Forms
   (`api.web3forms.com/submit`). Get a free access key at web3forms.com (just
   an email address, no account) and paste it into `contact.html` in place
   of `YOUR_WEB3FORMS_ACCESS_KEY`.
6. **Fill in the FAQ** — `contact.html` has a visible FAQ section and a
   matching `FAQPage` JSON-LD block with placeholder answers (insurance
   status, response time). Replace both with real, true facts — keep the two
   copies in sync.
7. **Turn on analytics** — the Vercel Web Analytics snippet
   (`/_vercel/insights/script.js`) is already on every page; enable Web
   Analytics in the Vercel project's dashboard (free tier) to activate it.
8. **Update `sitemap.xml`** with one `<url>` per page you actually publish,
   including each project sub-page.
9. **Structured data** — update the JSON-LD blocks in `index.html` (name,
   phone, email, address, description, service catalog) and in each
   `project-page-template.html` copy (Service name/description) so Google
   and AI answer engines can show accurate rich results.
10. **`llms.txt`** — fill in every `[...]` placeholder (services, coverage
    area, key facts, contact, page list) so AI assistants have an accurate
    summary to cite from.
11. Once there's a real Google Business Profile, consider embedding a live
    reviews widget/map instead of (or alongside) the static review cards —
    and only then add `AggregateRating` schema, backed by real star ratings.

## Photo cropping tip (from real use)

If working from customer WhatsApp/Facebook screenshots, they often have a
status bar, header, or app chrome baked in. A quick Pillow crop removes it:
sample average row brightness across the image width, find where it
transitions from dark (chrome) to bright (photo) at the top and bottom, and
crop to that bounding box. Worked reliably across multiple photo batches on
the original site.
