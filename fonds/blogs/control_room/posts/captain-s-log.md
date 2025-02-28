---
title: Captain's Log...
id: 3825120723371679611
author: Kirby Urner
published: 2018-05-31T13:00:00.001-07:00
updated: 2018-05-31T13:07:37.359-07:00
blog: control_room
tags: 
---

[](https://www.flickr.com/photos/kirbyurner/41444713624/in/dateposted-public/)

I am mindful that some products have taken in Python for internal scripting purposes, which I think is a good choice, as that leverages an existing fluency in many cases, and also leads those new to Python into something they may already know well:  CAD drawing and rendering.

My background is more [raytracing and VRML](http://4dsolutions.net/ocn/pyx3d.html), meaning I would usually build my scenes programmatically, but in a tight feedback loop with the renderings, a process of gradual approximation.  My subjects were usually pretty stark and austere, involving simple polyhedrons with a minimum of texture and shadowing.  I'd use anti-aliasing and might dial up reflectivity.  I'm proud of some of what I did, but more awed by what others have accomplished, with POV-Ray and other tools.

I remember Kenneth Snelson wondering if he would be able to move to Maya, after all those years mastering his SGI workstation.  I'm certainly no Maya user and am finding the Rhino learning curve fairly steep, even coming from a Python background.

There's a huge vocabulary (namespace) of directives, allowing me to build whatever scenery or artifacts I please, in principle.  In practice, I've cannibalized an old example, in vbscript, from Rhino 4, to make an icosahedron, and written other code in Python 3 (externally to Rhino 5 [for OS X](http://worldgame.blogspot.com/2018/05/home-brewing.html)) to [figure out the centers of a CCP](https://github.com/4dsolutions/Python5/blob/master/Generating%20the%20FCC.ipynb) (= IVM = FCC).

Today I at least figured out what object I could use in place of rectangles, which disappear upon rendering, too ghostly to merit texturing.  A planar surface is something else again.  It behaves almost the same way a rectangle does, but I had to rewrite and add code to accommodate the differences.  The obvious advantage is that it renders and allows materials to be applied to it.  That's progress, for me at least.