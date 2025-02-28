---
title: High School STEM
id: 3109872440554269080
author: Kirby Urner
published: 2015-08-15T21:18:00.000-07:00
updated: 2015-08-16T07:03:19.360-07:00
blog: bizmo_diaries
tags: 
---

[](https://www.flickr.com/photos/kirbyurner/20426299759/in/dateposted-public/)

The above is from a Clojure REPL in the Eclipse environment (IDE), whereas below is pretty much the same idea in a Python REPL, in PyCharm.

The symbol 'map' is a built-in function in both languages and does the same thing:  it applies a function to each member of a collection.

How the collections are named depends on the namespace:  Python or Clojure.

The square bracket collection above [1 2 3 4] is called a vector and needs no commas as commas count as whitespace in Clojure.

Below, in Python, [1, 2, 3, 4] is called a list, though a tuple might have been used, in which case parentheses replace square brackets.  Commas would be required either way.

What Python outputs is not another list (or vector) but an iterator, named mo in the example below.  An iterator is by definition responsive to the next() function.

Each time the iterator is fed to next( ), it yields its next value in the sequence, by applying the lambda to a next element.  One might also loop over mo in a "for elem in mo:" construct.

A lambda expression in Python is a way of defining a function on the fly that need not be remembered with a name.  The Clojure function is likewise anonymous, using fn instead of defn.

[](https://www.flickr.com/photos/kirbyurner/20425003958/in/dateposted-public/)

Although full blown mastery of either Python or Clojure might be too much to expect of an average busy high schooler, with limited study and practice time, some exposure to both is not out of the question.

Let the spiraling begin!

A strong STEM curriculum would likely include at least some dialog with the various REPLs, with mentor guidance, and combined with self study.

Yak with Python.  Chat with Clojure.  Get used to having these tools around.  They're free for the downloading (IDEs too).  Instructional materials abound.  Get in gear!