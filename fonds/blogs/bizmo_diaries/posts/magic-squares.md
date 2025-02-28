---
title: Magic Squares
id: 904163979598662104
author: Kirby Urner
published: 2018-02-19T02:39:00.000-08:00
updated: 2018-02-25T17:04:18.064-08:00
blog: bizmo_diaries
tags: 
---

[](https://www.flickr.com/photos/kirbyurner/40283905522/in/dateposted-public/)

Magic Squares in NumPy, [who is doing them](https://www.linkedin.com/learning/numpy-data-science-essential-training/magic-squares-and-numpy)? I'm not saying they need to be auto-generated. Copy some well known ones into code and run the NumPy version of sum along each of the two Magic Square axes.

[A sudoku](https://scipython.com/book/chapter-6-numpy/examples/checking-a-sudoku-grid-for-validity/) would be another data structure to model.  You can get to each sector with what's called a "view" or slice into just those cells, no extra memory for the data, just the overhead of the frame. A sum in each sector keeps track of same.

As a former calculus teacher, now [into statistics](https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.norm.html), I'm thinking we don't do enough in standard high school calc, to bridge [probability density functions](https://youtu.be/Fvi9A_tEmXQ) (PDFs) with their integrals, their cumulative distribution functions (CDFs).  So what if closed forms don't always jump out at us?  We've got the numerical tools to power through without those if need be.

I'm glad to have an API with the school system.  I thought [Measure 97](http://mybizmo.blogspot.com/2016/10/measure-97-again.html) might bring that about, and approached the Methodists about [a certain Code Castle](http://controlroom.blogspot.com/2017/03/n8v-american.html).  I also named a sculpture in my living room "code castle" and covered it with stuffed dragons.

Instead, I got a part time teaching job after school and get to chat with parents and teachers, other guardians, several times a week.  When it comes to teaching adults, Californians are more ravenous for a geek diet than Oregonians it seems.  I'm happy to feed a hungry neighbor.

"Code castle" (the sculpture) is being recycled for parts and [the Spooky Castle](http://controlroom.blogspot.com/2016/07/base-10-ghetto.html) (former church and community center) showed up in [my Jupyter Notebooks](https://github.com/4dsolutions/Python5/blob/master/SpookyCastle.ipynb) on what we call "context managers" in Python.  They have their __enter__ and __exit__ methods, the latter perhaps charged up with Exceptions it needs to deal with.

Jupyter Notebooks, for those of you who wish to learn, are interactive web pages you may run locally (i.e. on localhost 127.1.1.1) that talk to a kernel such as Python or Haskell or maybe R, the statistics engine.  I need to remind my students:  [Jupyter](http://blog.revolutionanalytics.com/2015/09/using-r-with-jupyter-notebooks.html) came from Julia, Python, R as the initial target languages of an expanded I-Python Notebook project.