title: Draft title
date: 2013-11-26 01:00
author: Jordi Burgos
category: Programming
tags: javascript, export, excel, project
slug: hadoop-maven
status: draft

Create and run a map/reduce program with Java
---------------------------------------------

Let's create the first mapreduce program with Java. Using maven to have a good start for next programs.

    mvn archetype:generate -DgroupId=com.jordiburgos -DartifactId=wordcount -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

    cd wordcount
    
    mvn eclipse:eclipse
