title: Flappy Bird fake score generator in HTML5
date: 2014-02-15 12:00
author: Jordi Burgos
category: Programming
tags: html5, javascript
slug: flappy-bird-fake-socre-generator-html5

We all know how famous and viral went Flappy Bird. It is really hard to get a good score.

You can be playing for hours just getting crappy scores. That has ended.

Now you can fake your score with this app!!! Send the image to your friends, Twitter, Facebook, etc... Enjoy !

How it's done
=============

The generator is done with the *canvas* tag of HTML5. Also with a lot of patience cutting the numbers from the game.

The *canvas* tag allows to draw images. With some calculations about the with of each number,
the score is drawn on a base picture of the "New score" screen. 

I made the image draw and calculations with Javascript. Check on the source code if you are interested. 

Score Generator
================

Insert score: <input id="score" type="text"/> <button id="btn" onclick="draw()">Draw</button>


<canvas id="canvas" width="720" height="1280">
</canvas>

<script src="/js/flappyfake.js"/>

