#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://jordiburgos.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = 'jordiburgos'
DISQUS_ID_SUFFIX = '_prod'
GOOGLE_ANALYTICS_CODE = 'UA-45872762-1'
GOOGLE_ANALYTICS_NAME = 'jordiburgos.com'
FACEBOOK_APPID = '378472698924914'
GITHUB_USERNAME = 'jmaister'
TWITTER_USERNAME = 'jordimaister'
REDDIT_USERNAME = 'jordimaister'

# SEO
# - For linking to g+
GOOGLE_PLUS_ID=105036003303074734569
# - Gravatar, for thumbnails
GRAVATAR_IMAGE='http://www.gravatar.com/avatar/9201c501532256286e60080ce8739045?s=300'
