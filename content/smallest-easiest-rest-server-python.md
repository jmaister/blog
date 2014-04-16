title: The smallest and easiest REST server in Python
date: 2014-04-16 23:00
author: Jordi Burgos
category: Programming
tags: AngularJS, Python, JSON, project
slug: smallest-easiest-rest-server-python

I am creating a web application for writing. This is just the beginning and I am making some experiments.

I decided to use AngularJS for the interface, as it solves most of the problems of any web application interface. Templates, two-way data binding between template and code, easy REST actions, etc...

As I understand, I am just learning, AngularJS is mostly designed for using a REST server for the data load and store. Any server would work whenever it responds to REST requests. For this reason, this solution is the fastest and easiest for creating a REST server in Python.

REST server with web.py
=======================

Here is the python script to define and start the REST server.

It defines two endpoints, */authors* and */suggest/[param1]/[param2]*.

    :::python
    #!/usr/bin/env python
    import web
    import json

    # Define exposed URL's
    urls = (
        '/authors', 'authors',
        '/suggest/(.*)/(.*)', 'suggest'
    )

    # Define the application
    app = web.application(urls, globals())

    AUTHORS = ['Miguel de Cervantes', 'William Shakespeare', 'Francisco de Quevedo', ...]
    
    # Define the actions when the URL's are called
    class authors:
        def GET(self):
            return json.dumps({'authors': AUTHORS})


    class suggest:
        def GET(self, author, words):
            if author in AUTHORS:
                suggestions = find_suggestions(author, words)
                return json.dumps(suggestions)
            else:
                return 'Error: author not found.'

    if __name__ == "__main__":
        # Start the server
        app.run()

Call using AngularJS
====================

The JavaScript code to make the request to the */authors* URL. It updates the *$scope.authors* variable with the data received.

    :::javascript
    var AUTHOR_URL = 'http://localhost:8080/authors';
    
    $http.get(AUTHOR_URL).success(function(data, status, headers, config) {
        console.log('success');
        $scope.authors = data.authors;
        console.log(arguments);
    }).error(function(data, status, headers, config) {
        console.log('error');
        console.log(arguments);
    });

This is the HTML code with the AngularJS directives to populate the data received to a SELECT component.
    
    :::html
    <select ng-model="author" ng-options="a for a in authors">
    </select>


Conclusion
==========
This solution is adequate if you need a REST server for learning or evaluating a new technology as it is easy and fast.
It is also good for mocking REST responses for unit testing purposes.
On next articles, I will show some samples of the AngularJS application.
