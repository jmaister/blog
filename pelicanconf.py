#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jordi Burgos'
SITENAME = u'Jordi Burgos'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

####
## MY CONFIG
####

DELETE_OUTPUT_DIRECTORY = True

SITESUBTITLE = 'Computing Life'
#DISQUS_SITENAME = ''
GITHUB_URL = 'https://github.com/jmaister'
#GOOGLE_ANALYTICS 	‘UA-XXXX-YYYY’ to activate Google Analytics.
#MENUITEMS = ('Blog', 'CV', 'About')
TWITTER_USERNAME = 'jordimaister'


# static files to copy into root, very useful for robots.txt
FILES_TO_COPY = (
   ('extra/robots.txt', 'robots.txt'),
   ('extra/humans.txt', 'humans.txt'),
)
# directories to be copied into output/static/
STATIC_PATHS = ['img', 'css', 'js']
# very useful for debugging purposes
DELETE_OUTPUT_DIRECTORY = True

THEME = 'pelican-chunk'
