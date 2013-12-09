title: Hadoop cluster with Vagrant
date: 2013-12-06 22:00
author: Jordi Burgos
category: Programming
tags: big data, hadoop, virtualization, vagrant
slug: big-data-hadoop-cluster-vagrant
status: draft

After having the data, next step is to have a Hadoop cluster to "upload" the data and run the processes.

This cluster is for the poor and lazy because it is group of virtualized machines running Hadoop.

**Pros:**

* There is no need to buy and build several machines
* All inside your own machine
* Running in minutes

**Cons:**

* Slower than a real cluster
* Just for testing purposes


Building virtual machines with Vagrant
======================================

As its site says: *"Vagrant provides easy to configure, reproducible, and portable work environments built on top of industry-standard technology and controlled by a single consistent workflow to help maximize the productivity and flexibility of you and your team."*

**tl;dr**: Vagrant creates virtual machines using configuration files. It is possible to start, stop, create, destroy virtual machines easily.

And here is the magic recipe:

* Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) for the virtual machines.
* Install [Vagrant](http://downloads.vagrantup.com/) for create, start and stop.
* Prepare the configuration files:

    > git clone [https://github.com/jmaister/vagrant-hadoop-cluster](https://github.com/jmaister/vagrant-hadoop-cluster)
    >
    > cd vagrant-hadoop-cluster
    >
    > vagrant box add precise64 http://files.vagrantup.com/precise64.box

* Start the machines!

    > vagrant up --provider=virtualbox
