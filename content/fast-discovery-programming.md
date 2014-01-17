title: Fast Discovery programming
date: 2014-01-04 20:00
author: Jordi Burgos
category: Programming
tags: programming, fast, discovery
slug: fast-discovery-programming

I would like to introduce you the **Fast Discovery** programming. It is based on the discovery on errors or failures as fast as possible to keep going on the good way to achieve the goals.

**Fast Discovery**, comes from the concepts like fail-fast or fail-early, but fail is not what we want to achieve. What we want is to know what we are doing works. So that, *Discovery* is a better term than *Fail*.

This concept can be applied to many fields on your life, like engineering or design, but the below examples are especially for programming.

This tips can help to become faster at programming, saving time for thinking and make things, and not waiting for things to happen like restarting a server or wait for the "Compiling..." alert to be closed.

IDE / Editor
============

First of all, learn your IDE or editor. Learn how to use it, how it can help you on your workflow.

### Shotcuts

Learn the shortcuts for the most common actions you usually do. Here are some examples for Eclipse, that you can do instead of moving the mouse wheel up and down or finding a menu options:

1. To find and open a file, use *Alt + R*. It shows a pop up, while you type it shows the files that follow that pattern. Wildcards '*' and '?' can be used.
2. Common for saving a file: *Shift + Alt + F* to format the code and *Control + S* to save the file.
3. Find some string in all file: *Control + H*.
4. Customize the search options, just select the ones that you use. Probably it is just "File Search".
<div class="center" markdown="1">
![Search customize]({filename}/images/eclipse/search-customize.png)
</div>
5. For faster results, select the folder or project you want to look for and check the option "Selected resources". It will not search in ALL the workspace
<div class="center" markdown="1">
![Search scope]({filename}/images/eclipse/search-scope.png)
</div>

You name them. Just look for your more used actions and try to find the shortcut on the menu.

### Selection

These are the most important shotcuts! Too obvious for some, and very unknown for others. You loose important seconds by moving your hand to the mouse, and trying to select some words. Just use the keyboard.

1. Control + C for Copy
2. Control + V for Paste
3. Control + X for Cut
4. Shift + (up,down,left,right) for Selection

### Mouse Selection

If there is no more choice and you use the mouse, keep in mind the tips below. You will not need to aim your selection like a *sniper*. Try it now!

1. Double click: select a full word.
2. Double click + move: select full words while moving.
3. Triple click: select a full paragraph.
4. Triple click + move: select full paragraphs while moving.


### Unwanted pop-ups

Fix common options or questions. How many times do you click on an "OK/Cancel" alert on each save or compile. Have you read it carefully? Is it a "Do not ask me again" checkbox? This can save some precious time.

On this example... yes click the checkbox "Run always in background", and then you can continue working while it executes. It will never show up again.
<div class="center" markdown="1">
![Search progress]({filename}/images/eclipse/search-progress.png)
</div>


Unit Testing
============

Unit testing is good for testing, we all know it (well others just hate it). It can help also while we are coding. A piece of code does not need to be finished to be executed with a unit test. Either it is needed the unit test before the code, like on [Test-driven development (TDD)](http://en.wikipedia.org/wiki/Test-driven_development).

While working on a piece of code, it is possible to isolate its execution with a unit test. With this it is not needed to start up a full application and test just what we want. So much time is saved until the code is finished and tested on the real application.


Network
=======

Network times are always a pain. Try to make your workflow as offline as possible, by using a local server instead of a server located in another network.

Also make your tools not to connect to internet. For example: Maven has the *-o* option to just use the local repository and do not connect to the remote repositories.

    mvn -o install

Conclusion
==========

These are the goodnes of **Fast Discovery** progarmming. Saving time, just a little or a lot, on each step of your workflow can significantly improve your speed at programming.

And more speed at programming means more results achieved. And that is good for your job. Do not work like this again:

<div class="center" markdown="1">
![Waiting]({filename}/images/waiting.gif)
</div>

These are just some examples, of course, there are much more. Just tell yours!!! 
