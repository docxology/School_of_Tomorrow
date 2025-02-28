---
title: Scala Tutorial at OSCON
id: 76948131056572300
author: Kirby Urner
published: 2014-07-20T13:47:00.002-07:00
updated: 2014-11-30T10:07:42.270-08:00
blog: control_room
tags: 
---

My notes from [Get Started Developing with Scala](http://www.oscon.com/oscon2014/public/schedule/detail/34095) by Jason Swartz and Kelsey Gilmore-Innis.

This is my day for JVM languages i.e. languages that compile to the Java Virtual Machine.  [Clojure](http://controlroom.blogspot.com/2014/07/oscon-2014-tutorials-day-1.html) and Scala both fit that bill and have other features in common as well:  immutable data, functional programming, first class functions. 

I opted for this tutorial based on a lunch conversation at one of the i18n tables and showed up with nothing working or even installed.  One of the minders got me up and running, getting stuff off a memory stick.

Turns out my version of Java was too old on the OST Mac Air.  I'm grabbing jdk-7u65-macosx-x64.dmg.  That worked. 

Now I have a little web servlet going, controlled by the tutorial code.

Starting SBT for OSCON Scala tutorial
mackurner:scala-tutorial kurner$ ./sbt.sh 
Starting SBT for OSCON Scala tutorial
[info] Loading project definition from /Users/kurner/Documents/scala-tutorial/project
[info] Set current project to Scala Tutorial (in build file:/Users/kurner/Documents/scala-tutorial/)
> console
[info] Generating /Users/kurner/Documents/scala-tutorial/target/scala-2.10/resource_managed/main/rebel.xml.
[info] Starting scala interpreter...
[info] 
Welcome to Scala version 2.10.4 (Java HotSpot(TM) 64-Bit Server VM, Java 1.7.0_65).
Type in expressions to have them evaluated.
Type :help for more information.

scala> "Hello, Scala"
res0: String = Hello, Scala 
scala> var started_programming: Map[String,Int] = Map("Kirby" -> 24, "Odd" -> 25)
started_programming: Map[String,Int] = Map(Kirby -> 24, Odd -> 25)

The language is not entirely unlike Java, statically typed, object oriented, but is more spare, more "expression-oriented" according to our presenter.  Someone who knows Java might move to Scala next.

Like Python and Clojure, Scala has [a REPL](http://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) (shown above). 

I'm sitting next to a man named Odd Are. I like that.

For those who know Python:

>>> list(filter(lambda i: i < 3, [1, 2, 3]))

is the same as

scala> List(1, 2, 3).filter(i => i < 3)

or even

scala> List(1,2,3).filter(_ < 3). 

Both Python and Scala feature top-level functions, meaning you're free and encouraged to pass them as arguments on occasion.  The methods map, reduce and filter give you a basis for functional programming.

Our presenters recommend easing into Scala by using it to write tests for Java code.

Recommended followup tutorial:  [The Neophytes Guide to Scala](http://danielwestheide.com/scala/neophytes.html).