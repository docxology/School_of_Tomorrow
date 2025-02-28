---
title: Prepping for Class
id: 5506316809330147761
author: Kirby Urner
published: 2007-05-10T18:35:00.000-07:00
updated: 2008-11-15T02:36:47.856-08:00
blog: control_room
tags: 
---

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgd0NEwzDLLyMB0_HMCzQww5LFeIvvKy3gthkxuiIxaSGKXQ5vz2l_5F1tJu_wKDA1p7cgQLZF84pu6FoIsoMJ8jbr-URi7Pcyli2aUpNJs0JZeDajne_t50hrTgjQ8ldogREF7/s1600-h/icosahedron.png)output from first draft of povtoyz,after rendering in POV-Ray
Python for Wanderers, part three of four, is tonight, and I wanted to be up to date with part three for Saturday Academy, which I'm teaching @ PSU. To that end, I wanted something like VizToyz but geared to work with a ray tracer, POV-Ray, instead of VPython out the back end.In writing povtoyz.py this afternoon, I finally noticed my polyhedra.py was eight faces shy of the full complement for my Icosahedron subclass, duh. I hadn't noticed because I was so focussed on the wireframe view, but once I got experimenting in POV-Ray, the defect became obvious, as faces, defined by POV-Ray's polygon primitive, were missing from I, Icosa (a menu option parallel to the one in viztoyz.py). today's scribbles
Jennifer is presumably on her way over the mountains, if Judy was right about finally finding a rental car. Not someone I've met before, but she may come to Wanderers as a part of her tour of PDX. 

Another feature of the upcoming Wanderers class will be to review my work with Dr. Bob Fuller and team, getting that Studies in Human Motion CDR ready for the summer '04 meeting of the American Association of Physics Teachers. 

I used Python + POV-Ray for my part in that project, starting from Excel spreadsheets giving the successive (x,y,z) spatial locations (rows) of several sensors (columns) affixed to a ballet student going through her moves in Lincoln, Nebraska. Each row became a frame in a POV-Ray film, with my Python code doing the conversion (included as open source on the CDR).
[](http://photos1.blogger.com/blogger/1134/545/1600/fpp.jpg) studies in human motion CD