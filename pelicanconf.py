#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jordi Burgos'
SITENAME = u'Jordi Burgos'
SITEURL = './'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
#FEED_RSS = 'feeds/all.rss.xml'
#CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
#LINKS =  (('GitHub', 'http://github.com/jmaister'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/jordimaister'),
          ('github', 'http://github.com/jmaister'),
          ('facebook', 'https://www.facebook.com/jordiburgos'),
          #('blogger', 'http://theanalystquotes.blogspot.com')
          )
EMAIL = 'jordiburgos@gmail.com'
MENUITEMS = (('Blog', ''), ('CV', ''), ('About', 'asdf'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

####
## MY CONFIG
####

PATH  = 'content'
DELETE_OUTPUT_DIRECTORY = True

SITESUBTITLE = 'Computing Life'
DISQUS_SITENAME = 'jordiburgos'
GITHUB_URL = 'http://github.com/jmaister'
GOOGLE_ANALYTICS = 'UA-41305783-1'
TWITTER_USERNAME = 'jordimaister'

COLOPHON=True
COLOPHON_TITLE='Colophon'
COLOPHON_CONTENT='Hello there, thanks coming to this blog.'


# static files to copy into root, very useful for robots.txt
FILES_TO_COPY = (
   ('extra/robots.txt', 'robots.txt'),
   ('extra/humans.txt', 'humans.txt'),
)
# directories to be copied into output/static/
STATIC_PATHS = ['img', 'css', 'js']

#THEME = 'pelican-chunk'
#THEME = './maistertheme'
THEME = './pelican-themes/bootstrap2'
THEME = './pelican-themes/tuxlite_tbs'
THEME = './pelican-themes/pelican-fresh'
THEME = './pelican-themes/iris'
THEME = './pelican-themes/lannisport'
THEME = './pelican-themes/pelican-mockingbird'
THEME = './pelican-themes/built-texts' # http://theanalyst.github.io/static-site-generators-everything-else.html


DEFAULT_DATE_FORMAT = ('%d %b %Y')
