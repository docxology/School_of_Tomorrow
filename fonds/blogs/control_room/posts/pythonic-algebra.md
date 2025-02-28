---
title: Pythonic Algebra
id: 5128794171506239328
author: Kirby Urner
published: 2008-01-11T15:55:00.000-08:00
updated: 2008-11-15T02:36:13.929-08:00
blog: control_room
tags: 
---

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6y_blT1c96xWpuk5mRTe1xVwaYvUvjX7MJ9DSm3fhri6BUCsQagBrXYUfg-dVE6_dZz83rXEEr21T0_w_p9iYrdO8KKqloK-1iiRog72LKzVv2io0QogV2CUxA7xBqt6wyhQx/s1600-h/pyalgebra.jpg)The above screen snippet shows two algebraic functions, everyday inhabitants of classroom textbooks, getting wrapped by some Pythonic OO thing such that we're subsequently able to compose these functions using the multiplication operator, at no extra cost to administrators ([Python is free](http://www.python.org/)).That's how [group theorists](http://mybizmo.blogspot.com/2007/11/explaining-group-theory.html) want us to think of functions, or [permutations](http://www.4dsolutions.net/ocn/python/ciphers.py), as elements you might chain together by means of a binary operation variously called composition or multiplication.f(g(x)) and g(f(x)) are respective synonyms for (f*g)(x) and (g*f)(x).Does commutativity pertain? That depends on the group, if it is a group.  Maybe it's a ring too.Welcome to [high school algebra](http://controlroom.blogspot.com/2006/05/rsa-using-pythonic-notation.html).The wrapping Function class, shown below, overloads both __mul__ and __call__.  We don't just want to compose them, we want to pass them arguments (food) and have them do work (expend energy).[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgytj4r58-VG04bn9Ug8Fe3pwhucWBb315GbLyzNLq5rkWhn01Wst4hvI3WDksbkAF5RSSFIWa0C3Cw4uLqEgn7ZrIPctD2mRw8lAw44YKUYOntdM-GmGKDZQgT6kzYHfsUOU_3/s1600-h/pyalgebra2.jpg)click for larger viewRelated thread on [math-thinking-l](http://mail.geneseo.edu/pipermail/math-thinking-l/2008-January/date.html).