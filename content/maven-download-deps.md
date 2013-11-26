title: Download all project dependencies to a folder with Maven
date: 2013-11-21 20:00
author: Jordi Burgos
category: Programming
tags: tip, maven
slug: maven-download-dependencies-folder

Some days ago at work I had a new requirement, upload all our deliverable packages (\*.jar, \*.war) to a new service for a security analysis.

The first solution was to upload artifact after its build on the continuous integration server. However this was not a good solution as all the artifacts must be uploaded at the same time.

After some research I've found the [maven-dependency-plugin](http://maven.apache.org/plugins/maven-dependency-plugin/). A very helpful plugin to manage all the dependencies defined in a pom.xml.

It has lots of options but the one useful for this task is **copy-dependencies**. It downloads all the dependencies defined on a project to a folder.

Here is the resulting pom.xml that would place the artifacts on the **${project.build.directory}/dependency** by default. See the comments below in the code:

    <?xml version="1.0" encoding="UTF-8"?>
    <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    
        <modelVersion>4.0.0</modelVersion>
    
        <!-- Define repositories -->
        <parent>
            <groupId>com.test</groupId>
            <artifactId>base</artifactId>
            <version>1.0</version>
        </parent>
    
        <!-- Define identification of this artifact -->
        <groupId>com.test</groupId>
        <artifactId>download-artifacts</artifactId>
        <version>1.0</version>
        <packaging>pom</packaging>
    
        <properties>
            <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        </properties>

        <!-- Dependencies to be downloaded, RELEASES or SNAPSHOTS -->
        <dependencies>
            <dependency>
                <groupId>com.test</groupId>
                <artifactId>goodproject</artifactId>
                <version>1.0</version>
                <type>jar</type>
            </dependency>
            <dependency>
                <groupId>com.test</groupId>
                <artifactId>webproject</artifactId>
                <version>5.0</version>
                <type>war</type>
            </dependency>
            <dependency>
                <groupId>com.test</groupId>
                <artifactId>application</artifactId>
                <version>1.1-SNAPSHOT</version>
                <type>war</type>
            </dependency>
        </dependencies>
    
        <build>
            <plugins>
                <plugin>
                    <!-- Our helpful plugin -->
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-dependency-plugin</artifactId>
                    <version>2.8</version>
                    <executions>
                        <execution>
                            <id>copy</id>
                            <phase>package</phase>
                            <goals>
                                <goal>copy-dependencies</goal>
                            </goals>
                            <configuration>
                                <!-- Remove classfier and version from the target files. -->
                                <stripClassifier>true</stripClassifier>
                                <stripVersion>true</stripVersion>
                            </configuration>
                        </execution>
                    </executions>
                </plugin>
            </plugins>
        </build>
    </project>

By executing **mvn package** on the pom.xml folder, we would have the files on the destination folder (./target/dependency/):

* goodproject.jar
* webproject.war
* application.war

After giving this solution, I had a great ovation from the team.

<div class="center" markdown="1">

![Citizen Kane applause]({filename}/images/meme/citizenkane.gif)

</div>
