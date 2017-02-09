title: Change on the comment system
date: 2014-04-21 20:40
author: Jordi Burgos
category: Misc
tags: blog, comments
slug: change-comment-system
summary:
    I changed the blog comment system. Now powered by [IntenseDebate](http://www.intensedebate.com).
    Disqus was giving a lot of headaches. The comments were appearing on all the pages, mixed comments between articles, and they were supposed to be separated by article.

I changed the blog comment system. Now powered by [IntenseDebate](http://www.intensedebate.com).

Disqus was giving a lot of headaches. The comments were appearing on all the pages, mixed comments between articles, and they were supposed to be separated by article.

Installing
==========

It just took 2 minutes to test the new commenting site, less than writing this article, and it works great.

Here is the code on the Pelican template to show or hide the comments.

    :::html+jinja
    {% if INTENSEDEBATE_ACCOUNT %}
    <script>
    var idcomments_acct = '{{INTENSEDEBATE_ACCOUNT}}';
    var idcomments_post_id = '{{ article.slug }}';
    var idcomments_post_url;
    </script>
    <span id="IDCommentsPostTitle" style="display:none"></span>
    <script type='text/javascript' src='http://www.intensedebate.com/js/genericCommentWrapperV2.js'></script>
    {% endif %}

Conclusion
==========

We have lost the previous comments, but we won a new commenting system that really works.
    
Keep commenting all the articles!!!

<div class="center" markdown="1">
![Not bad]({filename}/images/meme/surprise.gif)
</div>
