# -*- coding: utf-8 -*-

import time


# Data about this site
BLOG_AUTHOR = "Justin Pierel"
BLOG_TITLE = "Justin Pierel"
SITE_URL = "http://www.justinpierel.com/"
BLOG_EMAIL = "justinpierel@gmail.com"
BLOG_DESCRIPTION = ""

# What is the default language?
DEFAULT_LANG = "en"

# What other languages do you have?
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location
TRANSLATIONS = {
    DEFAULT_LANG: "",
    # Example for another language:
    # "es": "./es",
}

FAVICONS = (
     ("icon", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRm0W4-F8C4WkBe6x9v70qBOaoRWmZRuCOAUw&usqp=CAU", "32x32"),
)

TRANSLATIONS_PATTERN = '{path}.{lang}.{ext}'


# Links for the sidebar / navigation bar.
# You should provide a key-value pair for each used language.
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ('/', 'Home'),
        # ('/code', 'code'),
        # ('/research', 'research'),
        # ('/cv_jrp.pdf','cv'),
        ('/categories/index.html', 'Tags'),
        #('/rss.xml', 'RSS'),
    ),
}

NAVIGATION_ALT_LINKS = {
    DEFAULT_LANG: {}
}

import os
EXTRA_THEMES_DIRS = [
    os.path.join(os.path.dirname(__file__), "themes")
    ]
#THEME = 'iceland'
#THEME_COLOR = '#5670d4'
THEME = "srcco.de"
CODE_COLOR_SCHEME = 'friendly'


POSTS = (
    ("posts/*.html", "posts", "game.tmpl"),
)
PAGES = (
    ("pages/*.rst", "", "story.tmpl"),
    ("pages/*.html", "", "story.tmpl"),
    # ("games/*.html","categories","post.tmpl")
    )

COMPILERS = {
    "rest": ('.rst', '.txt'),
    "markdown": ('.md', '.mdown', '.markdown'),
    "textile": ('.textile',),
    "txt2tags": ('.t2t',),
    "bbcode": ('.bb',),
    "wiki": ('.wiki',),
    "ipynb": ('.ipynb',),
    "html": ('.html', '.htm'),
    # Pandoc detects the input from the source filename
    # but is disabled by default as it would conflict
    # with many of the others.
    # "pandoc": ('.rst', '.md', '.txt'),
}

HIDDEN_TAGS = ['mathjax']


WRITE_TAG_CLOUD = False


INDEX_PATH = "blog"


CREATE_SINGLE_ARCHIVE = True
ARCHIVE_PATH = "archive"


DATE_FORMAT = 'YYYY-MM-dd'


INDEX_TEASERS = False

LICENSE = ""
from nikola import filters
from functools import partial
import re
WHITESPACE_PATTERN = re.compile('\s+')
PRE_BLOCKS = re.compile(r'<pre.*?pre>', re.DOTALL)
def repl(m, captures):
    name = '$$CAPTURE-{}$$'.format(len(captures))
    captures[name] = m.group(0)
    return name
def compress_whitespace(x):
    '''
    >>> compress_whitespace('a  b')
    'a b'
    >>> compress_whitespace('a <pre> \\n </pre> b')
    'a <pre> \\n </pre> b'
    '''
    text = x.decode('utf8')
    captures = {}
    text = PRE_BLOCKS.sub(partial(repl, captures=captures), text)
    text = WHITESPACE_PATTERN.sub(' ', text)
    for key, val in captures.items():
        text = text.replace(key, val)
    return text.encode('utf8')
FILTERS = {
    #".css": [filters.yui_compressor],
    # ".js": [filters.yui_compressor],
    #".jpg": [filters.jpegoptim],
    #".png": [filters.optipng],
    # ".html": [filters.apply_to_file(compress_whitespace)]
}

CONTENT_FOOTER = """<hr>
&copy; {date}  {author} |
built with <a href="http://getnikola.com" rel="nofollow">nikola</a> """
CONTENT_FOOTER = CONTENT_FOOTER.format(author=BLOG_AUTHOR,
                                       date=time.gmtime().tm_year)

THUMBNAIL_SIZE = 140

COMMENT_SYSTEM = None #"disqus"
COMMENT_SYSTEM_ID = None #"kbarbary"


PRETTY_URLS = False


SOCIAL_BUTTON_CODE = ""


SHOW_SOURCELINK = False
COPY_SOURCES = False


BODY_END = """
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-48255812-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
"""


USE_BUNDLES = False


LOGGING_HANDLERS = {
    'stderr': {'loglevel': 'WARNING', 'bubble': True},
}

GLOBAL_CONTEXT = {}
