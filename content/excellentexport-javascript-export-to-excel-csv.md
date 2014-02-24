title: ExcellentExport.js update: Javascript export to Excel and CSV
date: 2014-02-18 23:00
author: Jordi Burgos
category: Programming
tags: javascript, export, excel, project
slug: excellentexport-javascript-export-to-excel-csv
summary: The [ExcellentExport.js](https://github.com/jmaister/excellentexport) library is having a lot of visits, from people coming directly to the page orredirected by search engines. So, I decided to update it.

<div class="alert alert-info" markdown="1">

Check the previous article for more information on: [Javascript export to Excel]({filename}/javascript-export-to-excel.md)

</div>

The [ExcellentExport](https://github.com/jmaister/excellentexport) library is having a lot of visits, from people coming directly to the page or
redirected by search engines. So, I decided to update it.

I have got some ideas from comments on the blog or discussions on reddit.

Download the new version from: [ExcellentExport.js v1.3](https://github.com/jmaister/excellentexport/releases/tag/v1.3)

New Changes
===========

IE6-IE9
-------
I've added support for old browsers, this is IE6 to IE9. These browsers do not provide the funcion *window.btoa(str)*,
so the code needs a Base64 encode function.

CSV
---
Besides to the Excel export, I've added Export to CSV function.

Working example
===============
    
<table class="table table-bordered" id="datatable" style="border: 1px solid black">
    <tr>
        <td>Title 1</td>
        <td>Title 2</td>
        <td>Title 3</td>
    </tr>
    <tr>
        <td>100</td>
        <td>200</td>
        <td>300</td>
    </tr>
    <tr>
        <td>400</td>
        <td>500</td>
        <td>600</td>
    </tr>
</table>

<script src="/js/excellentexport.js"></script>

* <a download="somedata.xls" href="#" onclick="return ExcellentExport.excel(this, 'datatable', 'Sheet Name Here');">Export table to Excel</a>
* <a download="somedata.csv" href="#" onclick="return ExcellentExport.csv(this, 'datatable');">Export table to CSV</a>

Conclusion
==========

Now [ExcellentExport.js](https://github.com/jmaister/excellentexport) basically works on all browsers.
It is ready for you to use on your projects.  

Check on github or this blog for updates. [ExcellentExport.js](https://github.com/jmaister/excellentexport).
