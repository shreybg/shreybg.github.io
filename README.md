# Tarski-for-Pelican

A Pelican theme and starter project that reproduces the reading experience of
`terrytao.wordpress.com`: full-width header banner, horizontal page nav,
wide content column with a widget sidebar on the right, full post text on the
front page, and boxed theorem environments.

Tested against Pelican 4.12.

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

pelican content -s pelicanconf.py     # build once
pelican --autoreload --listen         # dev server on http://localhost:8000
```

## Layout

```
pelicanconf.py            settings for local development
publishconf.py            production overrides (set SITEURL here)
content/
  posts/*.md              blog posts
  pages/*.md              static pages — each one appears in the nav bar
  images/header.jpg       the banner; replace this
themes/tarski/
  templates/              Jinja2 templates
  static/css/main.css     all the styling, variables at the top
```

## Writing math

`pymdownx.arithmatex` runs in generic mode, converting `$...$` and `$$...$$`
into `\(...\)` and `\[...\]` **before** Markdown sees them. This is why
`$a_{i,j}$` and `$x_1 \cdot x_2$` come out intact instead of having their
underscores turned into emphasis. KaTeX then renders the result in the
browser.

Custom macros live in the `macros` object in `templates/base.html` —
`\R`, `\C`, `\Z`, `\N`, `\Q`, and `\eps` are predefined.

If you'd rather render server-side, so pages carry no JavaScript at all,
swap in `pelican-katex` and delete the KaTeX `<script>` tags from
`base.html`.

## Theorem environments

```markdown
<div class="theorem" markdown="1">
**Theorem 1 (Euclid)** There are infinitely many primes.
</div>

<div class="proof" markdown="1">
Suppose $p_1, \dots, p_n$ were all of them...
</div>
```

Available classes: `theorem`, `lemma`, `proposition`, `corollary`,
`definition`, `conjecture`, `remark`, `example`, `exercise`, `proof`.
The first six are boxed and italicised; `remark` and `example` use a lighter
box; `proof` is unboxed with a run-in "Proof." and a closing tombstone.

The `markdown="1"` attribute is what allows Markdown inside the `div`. It
needs the `md_in_html` extension, already enabled.

If you find yourself typing those `div`s constantly, define a numbering
scheme with a small Pelican plugin, or write a Markdown snippet in your
editor. Tao numbers his by hand.

## Tuning the look

Everything visual is in the `:root` block at the top of `main.css` — fonts,
colours, body size, wrapper and sidebar widths. The current values approximate
Tarski's defaults: Lucida Grande at 13px, blue `#1b6da5` links, a 940px
wrapper with a 210px sidebar.

Two changes people usually want first:

- **Serif body text.** Set `--font-body` to a serif stack and bump
  `--size-body` to 15px.
- **Excerpts instead of full posts on the front page.** In
  `templates/index.html`, replace `{{ a.content }}` with `{{ a.summary }}`
  plus a link to `{{ a.url }}`.

## Comments

Static sites have none by default. Set `DISQUS_SITENAME` in `pelicanconf.py`
to switch on the Disqus block in `article.html`. If you'd rather keep
everything on GitHub, replace that block with utterances or giscy — both back
comments with GitHub issues and need no third-party account.

## Deploying

Set your real domain in `publishconf.py`, then:

```bash
pelican content -s publishconf.py
```

`output/` is a plain static directory. For GitHub Pages, commit it to a
`gh-pages` branch or point a GitHub Action at the build. Netlify and
Cloudflare Pages both take `pelican content -s publishconf.py` as the build
command and `output` as the publish directory.

## Search

The sidebar search box posts to DuckDuckGo scoped to your domain, which works
from day one but only covers pages the crawler has seen. For real local
search, add a Lunr.js or Stork index — both have Pelican plugins.
