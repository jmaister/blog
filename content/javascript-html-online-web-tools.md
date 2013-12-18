title: Javascript/HTML online web tools
date: 2013-12-18 23:00
author: Jordi Burgos
category: Programming
tags: javascript, html, web, tools
slug: javascript-html-online-web-tools
js: /js/tools.js

<style>
.result {
    background-color: #F0F0F0;
}
</style>

Here are some useful tools for developing, investigating, web scraping... Mainly for **Javascript** and **HTML**.

I'll be adding tools as they are developed, needed or asked. **Use the comments!**


Encoding/Decoding
=================

<div id='encodedecode' markdown=0>
Source text:<br/><textarea id='text' class="form-control">Text</textarea>
<br/>
<div class="row">
<div class="col-sm-3">
Base64 Encode:<br/><textarea id='base64encode' class="form-control result">base64encode</textarea>
</div>
<div class="col-sm-3">
Base64 Decode:<br/><textarea id='base64decode' class="form-control result">base64decode</textarea>
</div>
<div class="col-sm-3">
URL encode:<br/><textarea id='uencode' class="form-control result">uencode</textarea>
</div>
<div class="col-sm-3">
URL decode:<br/><textarea id='udecode' class="form-control result">udecode</textarea>
</div>
</div>

Time and Date
=============

<div markdown=0>
<div class="row">
<div class="col-sm-3">
Milliseconds:<br/><textarea id='millis' class="form-control">1000000</textarea>
</div>
<div class="col-sm-3">
Date local timezone:<br/><textarea id='date' class="form-control result">1000000</textarea>
</div>
<div class="col-sm-3">
Date UTC:<br/><textarea id='date-utc' class="form-control result">1000000</textarea>
</div>
<div class="col-sm-3">
</div>
</div>
</div>


Regular expressions
===================

<div markdown=0>
<div class="row">
<div class="col-sm-4">
Source text:<br/><textarea id='string' class="form-control">Is this all there is?</textarea>
</div>
<div class="col-sm-4">
Regular expression:<br/><textarea id='pattern' class="form-control">/is/gi</textarea>
</div>
<div class="col-sm-4">
Replace:<br/><textarea id='replace' class="form-control">AAA</textarea>
</div>
</div>

<div class="row">
<div class="col-sm-4">
Test:<br/><textarea id='pattern-test' class="form-control result">test</textarea>
</div>
<div class="col-sm-4">
Matches:<br/><textarea id='pattern-match' class="form-control result">match</textarea>
</div>
<div class="col-sm-4">
Replaced:<br/><textarea id='pattern-replaced' class="form-control result">replaced</textarea>
</div>
</div>

Numbers
=======

<div id='numbers' markdown=0>
<div class="row">
<div class="col-sm-3">
Source number:<br/><textarea id='number' class="form-control">10</textarea>
</div>
<div class="col-sm-3">
Source base:<br/>
<select id="base" class="form-control">
<option value="2">2</option>
<option value="8">8</option>
<option selected="selected" value="10">10</option>
<option value="16">16</option>
</select>
</div>
</div>
<br/>
<div class="row">
<div class="col-sm-3">
binary:<br/><textarea id='binary' class="form-control result">999</textarea>
</div>
<div class="col-sm-3">
decimal:<br/><textarea id='decimal' class="form-control result">999</textarea>
</div>
<div class="col-sm-3">
octal:<br/><textarea id='octal' class="form-control result">999</textarea>
</div>
<div class="col-sm-3">
hexadecimal:<br/><textarea id='hexadecimal' class="form-control result">999</textarea>
</div>
</div>
