title: Javascript web tools
date: 2013-11-26 01:00
author: Jordi Burgos
category: Programming
tags: javascript, web, tools
slug: javascript-web-tools
status: draft
js: /js/tools.js

Here are some tools that are useful in **Javascript** and **HTML** for developing, investigating, web scraping...

I'll be adding tools as they are developed, needed or asked. **Use the comments!**


Encoding/Decoding
=================

<div id='encodedecode' markdown=0>
Source text:<br/><textarea id='text'>Text</textarea>
<br/>
<div class="row">
<div class="col-sm-3">
Base64 Encode:<br/><textarea id='base64encode'>base64encode</textarea>
</div>
<div class="col-sm-3">
Base64 Decode:<br/><textarea id='base64decode'>base64decode</textarea>
</div>
<div class="col-sm-3">
URL encode:<br/><textarea id='uencode'>uencode</textarea>
</div>
<div class="col-sm-3">
URL decode:<br/><textarea id='udecode'>udecode</textarea>
</div>
</div>

Numbers
=======

<div id='numbers' markdown=0>
Source number:<br/><textarea id='number'>10</textarea>
Source base:
<select id="base">
<option value="2">2</option>
<option value="8">8</option>
<option selected="selected" value="10">10</option>
<option value="16">16</option>
</select>
<br/>
<div class="row">
<div class="col-sm-3">
binary:<br/><textarea id='binary'>999</textarea>
</div>
<div class="col-sm-3">
decimal:<br/><textarea id='decimal'>999</textarea>
</div>
<div class="col-sm-3">
octal:<br/><textarea id='octal'>999</textarea>
</div>
<div class="col-sm-3">
hexadecimal:<br/><textarea id='hexadecimal'>999</textarea>
</div>
</div>

Regular expressions
===================

<div markdown=0>
<div class="row">
<div class="col-sm-4">
Source text:<br/><textarea id='string'>aaabbbaaabbb</textarea>
</div>
<div class="col-sm-4">
Regular expression:<br/><textarea id='pattern'>a*b*</textarea>
</div>
<div class="col-sm-4">
Replace:<br/><textarea id='replace'>ccc</textarea>
</div>
</div>

<div class="row">
<div class="col-sm-4">
Test:<br/><textarea id='pattern-test'>test</textarea>
</div>
<div class="col-sm-4">
Find:<br/><textarea id='pattern-match'>match</textarea>
</div>
<div class="col-sm-4">
Replaced:<br/><textarea id='pattern-replaced'>replaced</textarea>
</div>
</div>
