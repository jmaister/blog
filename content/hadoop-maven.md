title: Easy start a Hadoop project with Maven
date: 2013-12-15 00:00
author: Jordi Burgos
category: Programming
tags: java, hadoop, maven
slug: java-hadoop-maven
status: draft

For running a Hadoop job written in Java, it is needed to create a Jar file with the compiled classes and also include another dependencies of out code. This can be very time consuming if we do not automatise the tasks.

When we have the idea and want to start coding instead of thinking on compile, compress the jar file, organize folders, etc... This guide shows how to configure a [Apache Maven](http://maven.apache.org/) pom.xml file to obtain a single zip with code plus dependencies ready to be executed on a Hadoop environment.

Features:
- Create JAR file with the job classes.
- Download dependencies.
- Create a bundle ZIP file.

>***You can follow the guide step by step. However if you just want to reuse the resulting pom.xml of this guide, go to the end of the article.***

Start with an empty pom.xml file
================================

Let's start with a simple pom.xml. **archetype:generate** can make the work for us to start the configuration. It creates the folde structure and a pom.xml with the minimum data required. Change **groupId** and **artifactId** with your requirements.

    :::bash
    mvn archetype:generate -DgroupId=com.jordiburgos -DartifactId=wordcount -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

Add Hadoop dependencies
=======================

Hadoop dependencies can be download from Cloudera repositories.

    :::xml
	<repositories>
		<repository>
			<id>cloudera</id>
			<url>https://repository.cloudera.com/artifactory/cloudera-repos/</url>
		</repository>
	</repositories>

Add the dependencies. org.apache.hadoop:**hadoop-common** and org.apache.hadoop:**hadoop-core**. Version numbers can vary, 2.2.0 and 1.2.1 are the current ones. Also jdk.tools are needed, note that systemPath is used to locate tools.jar, it comes with your JDK installation.

    :::xml
	<dependencies>
		<dependency>
			<groupId>org.apache.hadoop</groupId>
			<artifactId>hadoop-common</artifactId>
			<version>2.2.0</version>
		</dependency>

		<dependency>
			<groupId>org.apache.hadoop</groupId>
			<artifactId>hadoop-core</artifactId>
			<version>1.2.1</version>
		</dependency>

		<dependency>
			<groupId>jdk.tools</groupId>
			<artifactId>jdk.tools</artifactId>
			<version>1.7</version>
			<scope>system</scope>
			<systemPath>${java.home}/../lib/tools.jar</systemPath>
		</dependency>
        [...]
    </dependencies>

Create a ZIP bundle
===================

Using **maven-assembly-plugin** the ZIP file is created. It includes all dependencies in the */lib/* folder and the project jar on the root folder. ZIP structure is defined on **assembly.xml**.

    :::xml
    [...]
	<fileSets>
		<fileSet>
			<directory>${project.build.directory}</directory>
			<outputDirectory>/</outputDirectory>
			<includes>
				<include>*.jar</include>
			</includes>
		</fileSet>
	</fileSets>

	<dependencySets>
		<dependencySet>
			<useProjectArtifact>false</useProjectArtifact>
			<outputDirectory>/lib</outputDirectory>
		</dependencySet>
	</dependencySets>
    [...]


Conclusion
==========

After implementing the pom.xml, all the deployment of the Hadoop job is automatized. We only need to focus on code now.

It is not needed to follow the steps for starting a new development. Just download the code from [WordCount](https://github.com/jmaister/wordcount) on my GitHub account. Adapt it to your needs and start Hadooping.
