---
title: Eclipse for (+ Python (+ Java Clojure))
id: 6432562477278382028
author: Kirby Urner
published: 2015-08-06T16:19:00.003-07:00
updated: 2015-08-09T13:09:00.595-07:00
blog: bizmo_diaries
tags: 
---

[](https://www.flickr.com/photos/kirbyurner/20355152725/in/dateposted-public/)

:: Eclipse + Python ::

Some folks are understandably confused by all the jargon, as in "what's a virtual machine?" -- one needs context to resolve that.  Some VMs host operating systems however more usually it's the reverse:  an operating system (such as Windows 10 or Yosemite) hosts one or more VMs.

A breakthrough in recent computer science was the building of some "Great Pyramids" we never see in the desert, and yet they take gazillions of people hours to build.  They're packed with fancy algorithms.

I'm talking about the engines that specify their own bytecodes to which other higher languages might compile, and then those languages the run on top of them.

The JVM is one of the best known of these pyramids and is the target for several not-Java languages, the Java Virtual Machine having started out as Java's host within a platform (also known as the JRE or the Java Runtime Environment).

Whether you have Android or Windows or Linux, you have a JRE free for the downloading, plus often it's pre-installed.

Thanks to the JVM, one of the paradigm Object Oriented languages (Java) and one of the newest Functional Programming languages (Clojure) have become interoperable.  They both target the JVM.  Java coders can take advantage of what a Clojure genius writes, and vice versa.

The .NET VM, another virtual machine with open standards (i.e. world class), is likewise a shared target for interoperability:  as long as we all share the same Common Language at Runtime (or CLR), we're able to interweave our programs, and therefore our subcultures.  

[IronPython](https://en.wikipedia.org/wiki/IronPython) and [IronRuby](https://en.wikipedia.org/wiki/IronRuby) are examples of the higher languages targeting this VM.

Python has not been left out of this equation as Jython, supported by Oracle, likewise targets the JVM.  Learn Python on its native C-language VM, then move to Jython and Java, in route to Clojure as a way of rounding out your language savvy.  From that beginning, you're in a strong position to branch out.

On edu-sig (Python.org) and the Clojure list (a Google Group) and other places, I'm noticing this ecosystem, of Python + Java + Clojure, and suggest we embrace it.

Having one IDE (integrated development environment) that does all three is a big plus.  Eclipse and IntelliJ both come out on top as strong candidates for this role.

[ ](https://www.flickr.com/photos/kirbyurner/20362086511/in/dateposted-public/)
:: Eclipse + Clojure ::