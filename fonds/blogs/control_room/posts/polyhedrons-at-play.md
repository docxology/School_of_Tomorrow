---
title: Polyhedrons at Play
id: 1689996032985345540
author: Kirby Urner
published: 2013-09-27T19:20:00.002-07:00
updated: 2013-09-29T11:05:14.524-07:00
blog: control_room
tags: 
---

These two videos stem from conversations between David Koski and myself.  There's a lot more to it, so let me not try to reveal all here.  [Visual Python](http://www.vpython.org/) is a fine platform for outputting 3D animations as a result of running Python code.  They're interactive animations, meaning even as they play, you can change the viewing angle and distance.  Computer games may provide even more fluidity of motion but at least we've moved a step in that direction.

In the 2nd video I tell the listeners they might not agree with my volume figure and suggest they try with red edges = 2.  In XYZ, they should get a volume of 1, modeled likewise by a cube with edges half the reds, i.e. 1 x 1 x 1.  The shape is a reflected 1/6th corner of a rectangular brick where the brick is volume √3 x √3 x 1, so two of those is 2 x 1/6 of 3 = 1.

In [Synergetics](http://www.rwgrayprojects.com/synergetics/synergetics.html), the "prime vector" (PV) against which the others are scaled, is typically twice that of [the unit-radius sphere's](http://www.rwgrayprojects.com/synergetics/s09/figs/f86161.html) ([540.14](http://540.14/)) four of which pack to create the regular tetrahedron of edges 2R, or D (Diameter = 2 x Radius).

That's the 2nd tetrahedron I pause at, with all edges D, and is the [Synergetics](http://worldgame.blogspot.com/2013/09/an-introduction-to-synergetics.html) unit of volume.  The geometric model of multiplication is different, even in Flatland, so 3rd powering is [not cube-shaped](http://www.rwgrayprojects.com/synergetics/s09/figs/f9001.html) at the end of the day.  I use the brand '[Martian Math](http://wikieducator.org/Martian_Math)' to share it sometimes, in contrast to 'Earthling Math' which is the XYZ stuff we both know.

Sometimes another edge, usually R, or even an edge of the T module, is so important to the discussion you consider it the prime vector instead (think of "__main__" in Python). Synergetics names (tools) tend to adapt to the namespace (problem area) you're working in (a kind of pneumatic flexibility built in to the language).

So the XYZ unit and IVM unit are both in the same animation, but with [our volume numbers](http://www.rwgrayprojects.com/synergetics/plates/figs/plate03z.html) staying with IVM i.e. with "tetravolumes".  This would be a door to a "concentric hierarchy" of volumes, a somewhat familiar assortment of nested polys, but with more whole number volumes then you get from the XYZ namespace.

Making the cube your unit came at a cost and Synergetics helps us investigate the consequences by giving us workarounds.  [Art courses](http://mybizmo.blogspot.com/2006/03/biosculpture-take-two.html) (including in Cyberia) focusing on the concentric hierarchy have been a source of ideas for more straitlaced (as in straitjacketed) where experimental geometry is less well established.

What's this "[IVM](http://www.rwgrayprojects.com/synergetics/s10/figs/f7413.html)"?  Same as "[octet truss](http://worldgame.blogspot.com/2006/02/octet-truss.html)" in architecture, on which for awhile Fuller held a patent (even though Alexander Graham Bell did the same constructions).

[Here's the source code](https://mail.python.org/pipermail/edu-sig/2013-September/010897.html) for the above videos.  Sorry about the word-wrapping, in the comments too.  You'll need to fix that on your end, a good way to start familiarizing yourself with the code.