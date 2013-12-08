title: Better SEO for your blog
date: 2013-12-06 20:00
author: Jordi Burgos
category: Technology
tags: seo, google, blog, pelican
slug: better-seo-pelican-blog

For having a better exposure of our blog (or any page) on Internet, one of the important things is to have a good position on search results.

The techniques used to achieve this are called **SEO**, *Search Engine Optimization*.

Here I will show you two techniques that I used on this blog and, by extension, on my Pelican theme, [jmtheme](https://github.com/jmaister/jmtheme).

Pelican theme with better SEO
==============================

Adding some information about your blog can be done automatically from the Pelican theme. It helps the indexer bots to know what is in your pages.

Pagemaps
--------

PageMaps is a structured data format that Google created to enable website creators to embed data and notes in their pages.

It is an XML structure inserted in the HEAD tag of the HTML page as a comment, between &lt;!-- ... --&gt;.

Here is a sample of the code used on the theme, full code on [seo_pagemap.html](https://github.com/jmaister/jmtheme/blob/master/templates/seo_pagemap.html):

    :::html
    <html>
    <head>
        ....
    <!--
    <PageMap>
    <DataObject type="document">
        <Attribute name="title">{{article.title|striptags}}</Attribute>
        <Attribute name="author">{{ article.author }}</Attribute>
        <Attribute name="description">{{ article.summary|striptags }}</Attribute>
        <Attribute name="last_update">{{ article.date.isoformat() }}</Attribute>
    </DataObject>
    </PageMap>
    -->
    ...
    </head>
    ...

Here is the sample for a **document** information. There are more types like publication, action or thumbnail.
    
Microformats
------------

[Microformats](http://en.wikipedia.org/wiki/Microformat) are semantic markup formats for (X)HTML pages that help make the content accessible for search robots. Microformats allow the webmaster to indicate the meaning of specific fragments of text explicitly by supplementing existing HTML markup with special blocks of code. 

There are several types of microformats to tag contacts, recipes, reviews, products, etc.

Sample of hCard, the markup format for a contact. In this example, it is used to tag the author of an article. Using **vcard** on the class of the main tag and **name**, **fn**, **photo**, etc... on the child tags.

    :::html
    By <span>
        <!-- SEO: vcard -->
        <address id="hcard-Jordi-Burgos" class="vcard author">
            <a class="name" href="http://jordiburgos.com/author/jordi-burgos.html">Jordi Burgos</a>
            <a class="fn" href="http://jordiburgos.com/author/jordi-burgos.html">Jordi Burgos</a>
            <img src="http://jordiburgos.com/images/gravatar300.jpeg" alt="photo of " class="photo"/>
            <span class="title">Software Engineer</span>
            <span class="org">jordiburgos.com</span>
            <a class="url" href="http://jordiburgos.com">jordiburgos.com</a>
            <a class="email" href="mailto:jordiburgos@gmail.com">jordiburgos@gmail.com</a>
            <span class="address">
                <span class="region">Valencia</span>
                <span class="country-name">Spain</span>
            </span>
        </address>
    </span>

Maybe this is much information and we just want to show the name, and let the spiders to catch all the data. We can use CSS to hide data that is not important for the user on that part of the page.

    :::css
    .vcard * {
        display: none;
    }
    .vcard .name {
        display: inline;
    }


Show your picture on the search results
=======================================

Ever seen some people faces on the search results?

I you want your faces close to the search results of your pages, you need to link your Google+ account with your pages.

**Step 1**: Add a link on your pages to your Google+ account with the "rel=author":

    :::html
    <a href="https://plus.google.com/105036003303074734569?rel=author">Google+</a>

**Step 2**: Add you as a contributor to your Google+ account. Go to https://plus.google.com/&lt;your-id&gt;/about and add on "Contributes to"

<div class="center" markdown="1">

![Photo on search results]({filename}/images/seo/results_photo.png)

</div>

Conclusion
==========

With this easy configuration to add your picture and adding a little more information inside your pages, it is possible to have better positioning and visibility on search results.

These are just some examples of what can be done. There are much more tips and tricks waiting to be used. Stay tuned!
