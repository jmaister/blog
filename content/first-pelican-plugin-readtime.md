title: My first Pelican plugin: readtime
date: 2014-02-13 23:00
author: Jordi Burgos
category: Programming
tags: pelican, blog, python
slug: first-pelican-plugin-readtime

As I have seen in other blogs, I wanted to have a reading time estimation on my articles.

I'm using [Pelican](getpelican.com) as blog engine and it allows to write your
own plugins to process articles and pages of your blog. It is developed using Python, check the code on the github repository of [readtime](https://github.com/jmaister/readtime).

You can see the results on this screenshot:

<img class="img-responsive center-block" src="/images/readtime1.png" title="readtime screnshoot."/>

Plugin development
==================

The Pelican plugins works with signals, they are like events. You can register a method on the signal interested.
The method will be called each time that the signal is emited.

Here you can check the [list of signals](http://docs.getpelican.com/en/3.3.0/plugins.html#list-of-signals) on the documentation.
Each signal has its own parameters and details on when it is called.

The one I used is **content_object_init**, it is called on each page or article is read. This is how the signal is registered:


    :::python
    from pelican import signals

    def register():
        signals.content_object_init.connect(calculate_readtime)

Then, the calculations of the time needed for reading the article are done on the **calculate_readtime** method.
The information is stored on the *content_object* parameter for later access on the templates.

    :::python
    def calculate_readtime(content_object):
        if content_object._content is not None:
            content = content_object._content

        minutes = ... calculations ...
        
        content_object.readtime = {
            "minutes": minutes,
        }


Usage
=====

To use it you have to add the plugin name to the **pelicanconf.py** file.

    :::python
    PLUGINS=[ ... , 'readtime']

Then you can access the minutes variable to show on your **article.html** template. 

    :::python
    {% if article.readtime %}
    <div><b>Read in {{article.readtime.minutes}} min.</b></div>
    {% endif %}


Conclusion
==========

It is very easy to create a Pelican plugin. You just need an idea and a little time to add new functionality
for your favourite static blog engine.

<img class="img-responsive center-block" src="/images/meme/dogeyes.gif" title="Dog eyes."/>
