---
title: OSCON 2014 Tutorials (Day 1)
id: 1386532114334763568
author: Kirby Urner
published: 2014-07-20T09:50:00.001-07:00
updated: 2015-08-10T08:18:48.724-07:00
blog: control_room
tags: 
---

My notes from: [The Simplicity of Clojure](http://www.oscon.com/oscon2014/public/schedule/detail/33947) presented by Clinton Dreisbach and Bridget Hillyer.

Collections in Clojure:  Vectors, Lists, Maps, Sets.

Vectors are heterogeneous, as are all the collections, so like Python's lists. Also 0-based.

(nth [3 6 9] 1) ;=> 6.

A List is a unit of execution in that the first element is the function. Above: [3 6 9] is the Vector whereas (nth ...) is a List.

Collections are also immutable, like Python's tuples, so (conj (list 1 2) 3) ;=> (3 1 2).

Maps are similar to Python dicts.  Why are they associative again?  Sets (#) are like Python sets: no duplicates

:keywords have a magical property of serving as functions. (:a {:a 1}) ;=> 1.

A :keyword is a symbol that evaluates to itself. 

Function names (symbols) are common to all the collections wherever that makes sense.  This has to do with their all being Sequences (not just Collections).  The laziness of the Sequence should evoke Pythonic ideas of lazy iteration, as well as the general notion of sequence.

Strings are not sequences but get coerced into same in using sequence functions:

(first "this is it") ;=> \t

...where \t is the character type.

Python's special names enforce a kind of uniformity across types.  We get to the syntax level with __getitem__ and __getattr__ i.e. obj[x] and obj.x are things we define within the obj type.

First exercise (I'm in a tutorial): 

(list "Professor Plum" "Mrs. Peacock" "Mr. Green" "Mrs. White" "Colonel Mustered" "Miss scarlet")

(nth (list "Professor Plum" "Mrs. Peacock" "Mr. Green" "Mrs. White" "Colonel Mustered" "Miss scarlet") 3) ;=> "Mrs. White"

They had us [download LightTable](http://www.lighttable.com/) to follow along.  Here are [the slides](http://bridgethillyer.github.io/simplicity-ws/).  LightTable works with Python as well!

I met up with Tatia and Ed Leafe at the break.  Ed shares my FoxPro lineage.  Tatia is fresh off the plane from Brazil.  She's a Pythonista, like Ed and myself, fluent in both English and Portuguese.  We compared notes on Ruby (another OO language like Python) and clojure (functional, more LISP-like).

In a local scope, function let takes a Vector to give its bindings.  defn contracts def and fn.

Thanks to prefix notation, the hyphen is fine in variable names (symbols), no confusion with the minus symbol.

Polymorphism:  how?  If you don't have objects.  multi-methods maybe.  Helps to know some Java maybe as defrecord relates to Java's classes and interfaces.  "Make a Piece protocol" to model chess pieces, say with possible-moves and can-move? as methods.  OO thinking involves dispatching. 

Functional reactive programming:  Javelin treats your data like a spreadsheet.  Check [core.matrix](https://github.com/clojure-numerics) for an example of professional clojure code.  What's [ClojureScript](http://clojurescriptone.com/)?  Read more at [Hoplon.io](http://hoplon.io/).

For further reading:  [Clojure for the Brave and True](http://www.braveclojure.com/).