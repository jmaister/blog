#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

MARKUP = ('md', 'html')

AUTHOR = u'Jordi Burgos'
SITENAME = u'Jordi Burgos'
SITESUBTITLE = 'Programming, technology and random'
SITEURL = 'http://localhost:8000'

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

EMAIL = 'jordiburgos@gmail.com'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

####
## MY CONFIG
####

PATH  = 'content'
DELETE_OUTPUT_DIRECTORY = True

DISQUS_SITENAME = 'jordiburgos'
GITHUB_URL = 'http://github.com/jmaister'
GITHUB_USERNAME = 'jmaister'
GOOGLE_ANALYTICS_CODE = 'UA-41305783-1'
TWITTER_USERNAME = 'jordimaister'
FACEBOOK_APPID = '378472698924914'

# directories to be copied into output/static/
STATIC_PATHS = [
    'img',
    'css',
    'js',
    'extra/robots.txt',
    'extra/humans.txt',
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/humans.txt': {'path': 'humans.txt'},
}

THEME = './jmtheme'

DEFAULT_DATE_FORMAT = ('%d %b %Y')
