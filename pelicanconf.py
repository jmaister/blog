#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

MARKUP = ('md', 'html')

AUTHOR = u'Jordi Burgos'
SITENAME = u'Jordi Burgos'
SITESUBTITLE = 'Programming, technology and random things.'
SITEURL = 'http://localhost:8000'

# Formatting for urls

ARTICLE_URL = "post/{date:%Y}/{slug}.html"
ARTICLE_SAVE_AS = "post/{date:%Y}/{slug}.html"

ARTICLE_LANG_URL = "post/{date:%Y}/{slug}-{lang}.html"
ARTICLE_LANG_SAVE_AS  = "post/{date:%Y}/{slug}-{lang}.html"

CATEGORY_URL = "category/{slug}.html"
CATEGORY_SAVE_AS = "category/{slug}.html"

TAG_URL = "tag/{slug}.html"
TAG_SAVE_AS = "tag/{slug}.html"

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
FEED_RSS = 'feeds/all.rss.xml'


# Blogroll
#LINKS =  (('GitHub', 'http://github.com/jmaister'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/jordimaister'),
          ('github', 'http://github.com/jmaister'),
          #('facebook', 'http://www.facebook.com/jordiburgos'),
          )

# SEO
# - Gravatar, for thumbnails
GRAVATAR_IMAGE='http://www.gravatar.com/avatar/9201c501532256286e60080ce8739045?s=300'
# - For linking to g+
GOOGLE_PLUS_ID=105036003303074734569
# - Current date
CURRENT_DATE = datetime.now()

EMAIL = 'jordiburgos@gmail.com'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

##
## MY CONFIG
##

PATH  = 'content'
DELETE_OUTPUT_DIRECTORY = True

GITHUB_USERNAME = 'jmaister'
TWITTER_USERNAME = 'jordimaister'

# directories to be copied into output/static/
STATIC_PATHS = [
    'img',
    'css',
    'js',
    'images',
    'extra/robots.txt',
    'extra/humans.txt',
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/humans.txt': {'path': 'humans.txt'},
}

THEME = './jmtheme'

DEFAULT_DATE_FORMAT = ('%d %b %Y')


##
## PLUGINS
##

PLUGIN_PATH = './pelican-plugins'
PLUGINS=['sitemap',]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.75,
        'indexes': 0.5,
        'pages': 0.75
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'weekly'
    }
}
