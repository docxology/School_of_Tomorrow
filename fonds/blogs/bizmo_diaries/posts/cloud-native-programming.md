---
title: Cloud Native Programming
id: 1580748741888830870
author: Kirby Urner
published: 2020-03-08T13:20:00.001-07:00
updated: 2020-03-08T13:41:59.971-07:00
blog: bizmo_diaries
tags: 
---

This talk was helpful in that it took me back to my "thick client" early days, pre web browser, when my Visual FoxPro stack, ODBC to big servers, was dealing in read-only health procedure data from the Cath Labs and operating rooms (CVOR).  My RDBMS tables mapped every artery of every patient affected by stenosis or other coronary pathology.  Complications led to procedures and their outcomes, some of which might be the inherited complications of a next procedure and so on.

The scene has changed since those days, as data turned into big data, and as analysis tools started combing over larger server farms, using map-reduce (Hadoop) and a host of Apache projects ([Spark](https://spark.apache.org/), [Flink](https://flink.apache.org/), [Kafka](https://kafka.apache.org/)).  The speaker takes us from those old days to how we do things today, assuming the need to scale up without falling over.  How does one deal with the pressure to grow?  That's like sails to the wind if you have a seaworthy craft.

The other revolution in cloud native ecology is the growth of containerized microservices ala [Docker](https://www.docker.com/) and [Kubernetes](https://kubernetes.io/).  Get a lot of producers and subscribers messaging one another, in response to the streamed data onslaught.  Push all the end user rendering cosmetics to the clients, with their web browsers and visualization tools.  Customize their dashboards.  Some workstations monitor, some upload new data, some report on trends and so forth.

I go around with my little laptop, like a guitar, and strum my sound, these days involving visualizing [Flextegrity in a Jupyter Notebook](https://github.com/4dsolutions/School_of_Tomorrow/blob/master/Flextegrity_Lattice.ipynb).  I learn about cloud native environments from [OSCON](https://worldgame.blogspot.com/search?q=OSCON) proposals and Youtubes, and O'Reilly Safari Online when I can afford it.  What would be [the Python API to Kafka](https://cwiki.apache.org/confluence/display/KAFKA/Clients#Clients-Python) for example?