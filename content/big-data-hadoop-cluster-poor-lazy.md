title: Big Data: Hadoop cluster for the poor and lazy
date: 2013-12-02 22:00
author: Jordi Burgos
category: Programming
tags: big data, hadoop, virtualization, vagrant
slug: big-data-hadoop-cluster-poor-lazy
status: draft

***You can check the first article of this series: [Big Data: Get the data](./big-data-get-data.html)***

After having the data, next step is to have a Hadoop cluster to "upload" the data and run the processes.

This cluster is for the poor and lazy because it is group of virtualized machines running Hadoop.

**Pros:**

* There is no need to buy and build several machines
* All inside your own machine
* Running in minutes (maybe hours)

**Cons:**

* Slower than a real cluster
* Just for testing purposes


Building virtual machines with Vagrant
======================================

As its site says: *"Vagrant provides easy to configure, reproducible, and portable work environments built on top of industry-standard technology and controlled by a single consistent workflow to help maximize the productivity and flexibility of you and your team."*

**tl;dr**: Vagrant creates virtual machines using configuration files. It is possible to create



