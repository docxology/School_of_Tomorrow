---
title: Building Fractions
id: 5715661374884138815
author: Kirby Urner
published: 2017-06-17T17:44:00.001-07:00
updated: 2017-06-17T17:45:37.194-07:00
blog: control_room
tags: 
---

The code below shows a way of teaching operator overloading in Python.

Even
 though the standard library includes a Fraction type, it can't hurt to 
recreate it in a lesson, drawing on our knowledge of how fractions 
should behave.

Notice the embedded _gcd() method 
employs Euclid's Method to reduce fractions to lowest terms on 
initialization.  Since multiply and add operations, and their inverses, 
all end up creating new Q type instances (fractions), no attempt at 
reducing is made until then.

Hit the Run button to run the script.  Output appears at the bottom.