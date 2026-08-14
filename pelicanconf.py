from datetime import date

# ---------------------------------------------------------------- identity

AUTHOR = "Shrey Sharma"
SITENAME = "Varia"
SITESUBTITLE = "A collection of assorted thoughts."
SITEURL = ""  # empty for local dev; publishconf.py overrides it

PATH = "content"
TIMEZONE = "America/Los_Angeles"
DEFAULT_LANG = "en"

# ---------------------------------------------------------------- theme

THEME = "themes/tarski"

# A banner across the top of every page. Drop the file in content/images/
# and it gets copied to output/images/. Comment out for no banner.
HEADER_IMAGE = "images/header.jpg"

STATIC_PATHS = ["images", "extra"]
# Drop a favicon.ico in content/extra/ to enable this.
# EXTRA_PATH_METADATA = {
#     "extra/favicon.ico": {"path": "favicon.ico"},
# }

# ---------------------------------------------------------------- URLs
# Dateless post URLs, like Evan Chen's scheme: /my-post-title/

ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"
AUTHOR_URL = "author/{slug}/"
AUTHOR_SAVE_AS = "author/{slug}/index.html"

INDEX_SAVE_AS = "blog/index.html"
INDEX_URL = "blog/"
ARCHIVES_SAVE_AS = "archives/index.html"
CATEGORIES_SAVE_AS = "categories/index.html"
TAGS_SAVE_AS = "tags/index.html"

# Month archives — the sidebar "Archives" widget links to these.
YEAR_ARCHIVE_SAVE_AS = "archives/{date:%Y}/index.html"
MONTH_ARCHIVE_SAVE_AS = "archives/{date:%Y}/{date:%m}/index.html"

# ---------------------------------------------------------------- content

DEFAULT_PAGINATION = 10
DEFAULT_DATE_FORMAT = "%-d %B, %Y"   # "6 August, 2026"
SUMMARY_MAX_LENGTH = 60
TAG_CLOUD_STEPS = 5
TAG_CLOUD_MAX_ITEMS = 60

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Sidebar blogroll — (name, url) pairs. Set to () to hide the widget.
LINKS = (
    # ("Terence Tao", "https://terrytao.wordpress.com/"),
    # ("Power Overwhelming", "https://blog.evanchen.cc/"),
    # ("arXiv math", "https://arxiv.org/list/math/new"),
)

# Extra nav items beyond your Pages.
MENUITEMS = ()

# ---------------------------------------------------------------- feeds

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# ---------------------------------------------------------------- math
#
# arithmatex converts $...$ and $$...$$ into \(...\) and \[...\] *at parse
# time*, so Markdown never gets a chance to eat your subscripts and
# underscores. base.html then renders those with KaTeX in the browser.

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.attr_list": {},
        "markdown.extensions.md_in_html": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.toc": {"permalink": False},
        "markdown.extensions.smarty": {},
        "pymdownx.arithmatex": {"generic": True},
    },
    "output_format": "html5",
}

# ---------------------------------------------------------------- comments
# Static sites have no comment system of their own. Uncomment to enable
# Disqus; or swap article.html's comment block for utterances/giscus,
# which back comments with GitHub issues.
#
# DISQUS_SITENAME = "your-disqus-shortname"

# ---------------------------------------------------------------- misc

DELETE_OUTPUT_DIRECTORY = True
RELATIVE_URLS = True          # good for `pelican --listen`; publishconf turns it off
CACHE_CONTENT = False
COPYRIGHT_YEAR = date.today().year

LANDING_POST_COUNT = 5
ELSEWHERE = (
    ("GitHub", "https://github.com/shreybg"),
    ("LinkedIn", "https://www.linkedin.com/in/shrey-sharma-996452273/"),
)

PLUGINS = ["pelican.plugins.sitemap"]

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.7, "indexes": 0.5, "pages": 0.4},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}