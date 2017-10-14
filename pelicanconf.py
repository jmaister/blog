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
FEED_RSS = None # 'feeds/all.rss.xml'


# Social widget
SOCIAL = (('twitter', 'http://twitter.com/jordimaister'),
          ('github', 'http://github.com/jmaister'),
          #('facebook', 'http://www.facebook.com/jordiburgos'),
          ('google-plus', 'https://plus.google.com/105036003303074734569?rel=author')
          )

# - Current date
CURRENT_DATE = datetime.now()

TWITTER_USERNAME = '@jordimaister'
EMAIL = 'jordiburgos@gmail.com'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

DEFAULT_PAGINATION = 10

##
## MY CONFIG
##

PATH  = 'content'
DELETE_OUTPUT_DIRECTORY = True

# directories to be copied into output/static/
STATIC_PATHS = [
    'img',
    'css',
    'js',
    'images',
    'extra/robots.txt',
    'extra/humans.txt',
    'extra/google40f5a38880d4cc70',
    'extra/favicon.ico',
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/humans.txt': {'path': 'humans.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/google40f5a38880d4cc70': {'path': 'google40f5a38880d4cc70.html'},
}


THEME = './jmtheme2'

DEFAULT_DATE_FORMAT = ('%d %b %Y')

COINHIVE_ID = 'KQCpW8hVz1mn4HUDmsI8FJLaAOjycAlN'
COINHIVE_OPTIONS = '{throttle: 0.2}'

##
## PLUGINS
##

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS=['sitemap', 'readtime']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.9,
        'indexes': 0.5,
        'pages': 0.3
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

GRAVATAR_IMAGE = 'https://gravatar.com/userimage/52050482/0bba5c8dfa3c8956951c861d8103fe43'
