title: Creating a Pelican theme with Bootstrap 
date: 2013-11-28 23:00
author: Jordi Burgos
category: Technology
tags: javascript, css, bootstrap, pelican, blog, seo
slug: create-pelican-theme-bootstrap

I wanted to give the blog my personal touch by creating my own theme for [Pelican](http://getpelican.com). Here is the [getting started page](https://github.com/getpelican/pelican/blob/master/docs/getting_started.rst) for creating your own blog with this tool.

It is quite simple to setup and just start writing articles and pages with [Markdown](http://daringfireball.net/projects/markdown/). Markdown allows you to write using an easy-to-read, easy-to-write plain text format, then convert it to structurally valid XHTML (or HTML).  

There are a lot of good and nice themes, but I prefered to create/copy/inspire this by myself to meet my requirements. However, it follows the typical template rules to be useful for anyone to use it.

I called it jmtheme and you can download it form here [jmtheme](https://github.com/jmaister/jmtheme).

<div class="center" markdown="1">

![Theme]({filename}/images/theme_thumb.png)

</div>


Features
========

* Responsive theme: works well on desktops, tablets and mobiles
* Social icons
* Social share buttons (twitter, google+, facebook, reddit)
* Disqus comments
* Google Analytics


Personalization
===============

Option to add a list of icons pointing to the common social sites. Also the email icon.

    :::python
    # Social widget
    SOCIAL = (
        ('twitter', 'http://twitter.com/XXXXXX'),
        ('github', 'http://github.com/XXXXXX'),
    )
    EMAIL = 'user@example.com'
    

Social buttons on each article for sharing. Just add value to this variables.

    :::python
    GITHUB_USERNAME = 'jmaister'
    TWITTER_USERNAME = 'jordimaister'
    FACEBOOK_APPID = '999......999'

Disqus comments:

    :::python
    DISQUS_SITENAME = 'jordiburgos'
    
Google analytics:

    :::python
    GOOGLE_ANALYTICS_CODE = 'UA-9999999-1'
    GOOGLE_ANALYTICS_NAME = 'jordiburgos.com'

Icons for pages to show on the menu. Add "icon" value on the page.

    :::python
    icon: trophy


Conclusion
==========

I am thinking about adding some [microdata](http://en.wikipedia.org/wiki/Microdata_%28HTML%29) or [microformat](http://en.wikipedia.org/wiki/Microformat) on the templates to help search engines to crawl and index the site. This is called Search Engine Optimization or SEO. More on this implementation on next articles.

If you have any advise or comment about the theme, just tell me on the comments. 
