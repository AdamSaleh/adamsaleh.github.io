#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Adam Saleh'
SITENAME = 'asaleh/notebook'
SITEURL = 'https://adamsaleh.github.io/'
SITETITLE = AUTHOR
SITESUBTITLE = 'QE Engineer'
SITEDESCRIPTION = 'Programming Languages Enthusiast'

THEME = '/usr/local/lib/python3.4/dist-packages/pelican/themes/Flex'

PATH = 'content'
SITELOGO = SITEURL + '/images/profile.png'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ['/home/ubuntu/workspace/adamsaleh/plugins']
MARKUP = ('md', 'ipynb')

PLUGINS = ['ipynb.markup','filetime_from_git']

# Blogroll

# Social widget
SOCIAL = (('github', 'https://github.com/adamsaleh'),)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = False

IGNORE_FILES = ['.ipynb_checkpoints']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
