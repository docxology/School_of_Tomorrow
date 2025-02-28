---
title: The Farmer in the Dell
id: 7099888627293978663
author: Kirby Urner
published: 2015-08-20T17:58:00.001-07:00
updated: 2015-08-21T09:00:26.537-07:00
blog: bizmo_diaries
tags: 
---

[](https://www.flickr.com/photos/kirbyurner/20718348826/in/dateposted-public/)

... the Dell in the Farmer.  Lets think of a farmer riding a tractor, the tractor in a field.  Yes, the farmer is in the field, but then so has the farmer internalized the field, a mental field.  People do that with fields.  In the computer language I'm learning, Python, the method for adding a Tractor to a field is a time to give the farmer, the self of the Tractor, a handle on the Field.

[](https://www.flickr.com/photos/kirbyurner/20753300841/in/dateposted-public/)

the self of "this Field" is provided to the "self" of the added Tractor

One may view that in source code at GitHub, where [Lesson1.py](https://github.com/4dsolutions/Python5/blob/master/Lesson1.py) defines the Field and Tractor, along with a subclass of Tractor for writing in the field. 

Then [Lesson2.py](https://github.com/4dsolutions/Python5/blob/master/Lesson2.py) defines another subclass of Tractor, the CropCircleTractor, that appropriately plows or plants a Mandelbrot in its Field.  The output is just a text file, ASCII art, whereas in future Lessons one [might use PIL](https://mail.python.org/pipermail/edu-sig/2015-June/011280.html), or [POV-Ray](http://www.4dsolutions.net/ocn/numeracy0.html), or VRML or even Visual Python.

The Field is an XY layer, a grid of cells each addressed by two numbers, a familiar tool.  Piling up these layers, 3D Printer style, would be a way to encompass Volume which contains shapes we might address in various ways, perhaps with XYZ coordinates, [adding Quadrays](https://en.wikipedia.org/wiki/Quadray_coordinates) as a less familiar tool for contrast.  The Mandelbrot might become [a Mandelbulb](http://worldgame.blogspot.com/2012/08/adventures-in-teaching-and-driving.html) instead.

The Tractor comes with a TV-like raster motion.  A real tractor would turn around and come back the other way, but this one works more like a spiral, as if the end of a row connected to the beginning of the next at the other side of the field. 

[](https://www.flickr.com/photos/kirbyurner/18932679492/in/album-72157654417641521/)

Then, having traversed the very last row and coming to the end, the Tractor magically reappears at the start again, to begin its trek all over.  What we lose in freedom, we gain in the simplicity of the code.  Provided the Tractor has enough fuel (there's a fuel_level), every cell will get visited within a circular topology.

Another subclass yet, of which I've already done some versions, plays a Game of Life using rule-governed cellular automata. 

Might we alter the Field class to consist of hexagons instead? Games of Life may be played [that way too](http://www.4dsolutions.net/ocn/life.html), and are, quite a lot.

Could our Volume be as if filled with [rhombic dodecahedra](http://controlroom.blogspot.com/2015/07/of-kepler-and-aristotle.html), perhaps using Quadrays again? 

These vistas stretch out before us, which speaks well for the simple ladder that got us up this high, where we get [lots of overview](http://mybizmo.blogspot.com/2015/08/stem-carbon-as-theme.html).

[](https://www.flickr.com/photos/kirbyurner/18315135184/in/album-72157654417641521/)