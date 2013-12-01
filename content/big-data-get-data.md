title: Big Data: Get the data
date: 2013-12-02 20:00
author: Jordi Burgos
category: Programming
tags: big data, small data, hadoop
slug: big-data-get-data

Lastly, there is a lot of news, work offers, noise, ads, ... about **Big Data**. Because of this I decided to make my own Big Data project.

As this just would be to implement a map-reduce algorithm in any language, quite easy for any programming exercise, I wanted to give this technology an use for something real.

The data
========

Any Big Data project is nothing without the data. Otherwise, it would be called **small data** or   **medium data** (by the way, I should register this new trademarks).

The data to be processed is the files of the [BOE](http://www.boe.es). The **Bolet&iacute;n Oficial del Estado** (BOE) is a daily Spanish-government publication in which new laws, directives and executive decisions are published together with advertisements for public-sector posts and contracts. It is provided free of charge to all government agencies and state organizations including schools, embassies and public libraries. (Collins Spanish Dictionary)


Get the data
============

For scrapping the data from the website, first approach is always to use Python tools like [Scrapy](http://scrapy.org/) or [webscraping](http://docs.webscraping.com/index.html). I used these tools some times before and make very easy to crawl a full website looking for information. But after some research of the pages, it would be very over-engineered to use these tools.

All the files follow the same pattern:

* Format: *xml* for marked documents; *txt* for plain text.
* Code: *A* for general orders, personnel and misc; *B* for Justice administration.
* Year
* ID: from *1* to the *number of documents*.


    http://www.boe.es/diario_boe/[format].php?id=BOE-[code]-[year]-[id]

For starting, I downloaded the files for years 2012 and 2013. 182694 files with 1,67 GB (1.800.364.500 bytes).

    '''
    Scrapping BOE (boe.es) bulletins.

    Created on 30/11/2013
    @author: Jordi Burgos
    '''

    # pip install webscraping
    # http://docs.webscraping.com/examples.html#business-directory-threaded-scraper

    from webscraping import download, xpath

    import itertools
    import urlparse
    import re
    import os.path

    import urllib2

    DOMAIN = "http://www.boe.es"
    BOE_LINK = "/diario_boe/xml.php?id=%s"
    FILENAME = "BOE-%s-%d-%d"
    OUTPUT = "files/"

    MAX_IDS = {
        2013: {'A': 12536, 'B': 45197},
        2012: {'A': 15822, 'B': 45222},    
        2011: {'A': 20867, 'B': 43026},    
    }

    def main():
        for year, max_codes in MAX_IDS.items():
            for code, max_id in max_codes.items():
                for id in xrange(1, max_id):
                    fullid = FILENAME % (code, year, id)
                    filename = OUTPUT + fullid
                    link = urlparse.urljoin(DOMAIN, BOE_LINK % (fullid))
                    save_url(link, filename)

    def save_url(link, filename):
        if os.path.exists(filename):
            pass
        else:
            try:
                data = urllib2.urlopen(link).read()
                out = open(filename, 'w')
                out.write(data)
                out.close()
            except e:
                print "error", e, link, filename


    if __name__ == '__main__':
        main()


Conclusion
==========

After getting the data, on next articles I will set up a Hadoop environment for programming and analyse the data.
