---
title: Putting a Lid on It
id: 1028236666068672867
author: Kirby Urner
published: 2016-06-13T09:32:00.003-07:00
updated: 2016-06-13T10:32:32.531-07:00
blog: control_room
tags: 
---

Imagine an operation with two vectors as input, called "close the lid".  Given v1, v2 as lengths with an included angle, the 3rd length is determined, meaning the area in question is unique, determinate.  Run the operation on v1 and v2, called "close the lid" and every time, v3 is the same length and A is the returned Area.  A triangle.

Now extend this operation to three vectors not in the same plane.  They "fan out" from the same starting point, a common origin, and point to three points in space (given the common origin, we have four points total, not forgetting the observing camera is a point as well, and whatever [light sources](http://worldgame.blogspot.com/2008/10/claymation-station.html)...).  The tetrahedron is unique, with V the Volume.  "Closing the lid" makes sense here as well.

Given we already have a formula that returns a tetrahedron's volume, given six edge lengths, it's pretty easy to modify that to where three edges get determined by subtracting pairs of input vectors.  Given |v1|, |v2| and |v3| as inputs, the three lengths we need, in addition, to put a lid on it (on the tetrahedron) will be: |v1 - v2|, |v1 - v3| and |v2 - v3|.  In not forcing these lengths independently, but computing them as a consequence, we ensure the six edges are "legal" i.e. such a tetrahedron really exists (important for our algorithm to work right).

Consider three vectors from (0, 0, 0, 0), [the origin](http://mybizmo.blogspot.com/2016/06/wheres-origin.html) of the Quadray Coordinate System (Chakovians), with vectors (1, 0, 0, 0), (0, 1, 0, 0) and (0, 0, 1, 0) pointing to three corners of a regular tetrahedron from its center.  Lets define the quadrant of said tetrahedron to be our 1/4 unit, where all six edges of the canonical home base are defined by edges D of the IVM ball packing.

That's a lot of jargon, so if this is a new-to-you namespace, [follow some links](http://coffeeshopsnet.blogspot.com/2016/04/quadray-coordinates.html) for a stronger ability to tune in.  Basically, four quadrays divide space into four quadrants, just as the XYZ basis vectors and their reflections create the eight octants of the Cartesian scaffolding.

In some of the comics and cartoons I've been working on  (manga and anime), we introduce "close the lid" triangular and tetrahedral treatments as how "Martians" learn math in some science fiction narrative (we're not requiring true belief in specific ET stories, which may get quite ornate, featuring many species).

The Martian Math narrative helps build a story line wherein more details get remembered, such as how the Martians and Earthlings agree to use a conversion constant between their respective models.  They need to pour concrete after all, given they're collaborating on a canyon dam.

The R-cube of the Earthlings (unit volume for them) and the D-tetrahedron for the Martians (unit volume for them) are within shouting distance of "same size" i.e. the 2nd root of 9/8, although not unity (about 1.06), obviously, is close enough for quick and dirty back-of-the-napkin type operations, as when sharing a booth in the company diner.