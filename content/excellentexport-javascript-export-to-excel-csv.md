title: ExcellentExport.js update: Javascript export to Excel and CSV
date: 2014-04-24 20:00
author: Jordi Burgos
category: Programming
tags: javascript, export, excel, project
slug: excellentexport-javascript-export-to-excel-csv
summary: The [ExcellentExport.js](https://github.com/jmaister/excellentexport) library is having a lot of visits, from people coming directly to the page orredirected by search engines. So, I decided to update it.

<div class="alert alert-info" markdown="1">

Check the previous article for more information on: [Javascript export to Excel]({filename}/javascript-export-to-excel.md)

</div>
<div class="alert alert-info" markdown="1">

Updated to v1.4

</div>

The [ExcellentExport](https://github.com/jmaister/excellentexport) library is having a lot of visits, from people coming directly to the page or
redirected by search engines. So, I decided to update it.

I have got some ideas from comments on the blog or discussions on reddit.

Download the new version from: [ExcellentExport.js v1.4](https://github.com/jmaister/excellentexport/releases/tag/v1.4)

New Changes
===========

UTF-8
-----
Now the export data supports UTF-8 characters.

IE6-IE8
-------
IE8 or lower do not support *data:* url schema.

CSV
---
Besides to the Excel export, I've added Export to CSV function.

Working example
===============
    
<table class="table table-bordered" id="datatable" style="border: 1px solid black">
            <tr>
                <th>Column 1</th>
                <th>Column "cool" 2</th>
                <th>Column 3</th>
                <th>Column 4</th>
            </tr>
            <tr>
                <td>100,111</td>
                <td>200</td>
                <td>300</td>
                <td>áéíóú</td>
            </tr>
            <tr>
                <td>400</td>
                <td>500</td>
                <td>600</td>
                <td>àèìòù</td>
            </tr>
            <tr>
                <td>Text</td>
                <td>More text</td>
                <td>Text with
                new line</td>
                <td>ç ñ ÄËÏÖÜ äëïöü</td>
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
