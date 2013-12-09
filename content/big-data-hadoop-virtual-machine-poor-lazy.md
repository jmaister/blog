title: Big Data: Hadoop installation on virtual machine, for the poor and lazy
date: 2013-12-06 22:00
author: Jordi Burgos
category: Programming
tags: big data, hadoop, virtualization, vagrant
slug: big-data-hadoop-virtual-machine-poor-lazy
status: draft

***You can check the first article of this series: [Big Data: Get the data](./big-data-get-data.html)***

After having the data, next step is to have a Hadoop cluster or single machine installation to "upload" the data and run the processes.

Even that Hadoop is meant to run on lots and lots of machines, we can make a single **virtual machine** installation to make tests and start hacking on it.

If the purpose of your Hadoop learning is just to learn to program and not be a full system administrator, this is a good point to start.

**Pros**

* There is no need to buy and build several machines
* All inside your own machine
* Running in minutes

**Cons:**

* Slower than a real cluster
* Just for testing purposes

Create the Virtual Machine
==========================

The company [Hortonworks](http://hortonworks.com/) provides the [Hortonworks Sandbox](http://hortonworks.com/products/hortonworks-sandbox/) a Virtual Machine image with a full Hadoop environment. It saves us the time and pain of installing and configuring the machine.

It comes out of the box with Hadoop, HBase, ZooKeeper, Hive, etc. Just take a look at the sandbox page to see all the details.

Step 1: Install [VirtalBox](https://www.virtualbox.org/wiki/Downloads) 4.2+
Step 2: Download the [Sandbox 2 for Virtualbox (2.5 GB)](http://hortonworks.com/products/hortonworks-sandbox/#install)
Step 3: Install the **.ova** image downloaded on VirtualBox and follow the instructions.
Step 4: Run!!!

Just wait to full start of the machine and you will get a screen with the instructions. It lets you:

* Enter the web interface on [http://127.0.0.1:8888/](http://127.0.0.1:8888/) (Needs registration). It gives you tutorials and tool preferences.
* SSH the server with **ssh root@127.0.0.1 -p 2222**, the password is "hadoop".
* Change to another console inside the virtual machine with Alt+F5

Start hacking with Hadoop
=========================

For testing that it works, let's run a little test using Hadoop.

Upload data to HDFS
-------------------

First, the data. To upload data into Hadoop environment, we use HDFS (Hadoop Distributed File System). It holds and manages the files and allows access to the processes. In a multi-server environment, HDFS would replicate and share data between several machines.

hdfs dfs -mkdir boe

F:\workspace\boescrap\files>type boe-A-2013-1 | ssh root@127.0.0.1 -p 2222 "hdfs dfs -put - boe/boe-2013-1"




Run a map/reduce program
------------------------


