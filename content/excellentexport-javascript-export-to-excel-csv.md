title: ExcellentExport.js update: Javascript export to Excel and CSV
date: 2017-09-26 23:00
author: Jordi Burgos
category: Programming
tags: javascript, export, excel, project
slug: excellentexport-javascript-export-to-excel-csv
summary: The [ExcellentExport.js](https://github.com/jmaister/excellentexport) library is having a lot of visits, from people coming directly to the page orredirected by search engines. So, I decided to update it.

<div class="alert alert-info" markdown="1">

Check the previous article for more information on: [Javascript export to Excel]({filename}/javascript-export-to-excel.md)

</div>
<div class="alert alert-info" markdown="1">

Updated to v2.1.0

</div>

The [ExcellentExport](https://github.com/jmaister/excellentexport) library is having a lot of visits, from people coming directly to the page or
redirected by search engines. So, I decided to update it.

I have got some ideas from comments on the blog or discussions on reddit.

Download the new version from: [ExcellentExport.js v2.1.0](https://github.com/jmaister/excellentexport/releases/tag/2.1.0)

Change history
==============

# Revision history:

### 3.0.0 (Work in progress)

* XLSX support. This bumps the build size to 639 KB.
* New API: ExcellentExport.convert(...)

### 2.1.0 (24/09/2017)

* Add Webpack build.
* Create UMD JavaScript module. Library can be loaded as a module (import, RequireJS, AMD, etc...) or standalone as window.ExcelentExport.

### 2.0.3 (21/01/2017)

* Fix export as a module.
* Changed minifier to UglifyJS.

### 2.0.2 (10/01/2017)

* Fix CSV Chinese characters and other special characters display error in Windows Excel.
* Fix URL.createObjectURL(...) on Firefox.


### 2.0.0 (03/10/2016)

* Now it can export to big files +2MB.
* Minimum IE 11.
* Links open with URL.createObjectURL(...).
* NPM package available.
* Using Semantic versioning (2.0.0 instead of 2.0).
* Module can be loaded standalone or with RequireJS.
* Change license to MIT.

### 1.5

* Possibility to select a CSV delimiter.
* Bower package available.
* Compose package available.

### 1.4

* Add LICENSE.txt with GPL v3.
* UTF-8 characters fixed.

### 1.3

* Added minified version.

### 1.1

* Added CSV data export

### 1.0

* Added Excel data export

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
