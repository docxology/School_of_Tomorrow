---
title: Visual Harmonies
id: 3038788993286211691
author: Kirby Urner
published: 2014-07-27T18:19:00.000-07:00
updated: 2014-07-27T21:34:01.699-07:00
blog: coffee_shops
tags: 
---

:: by synergetics explorer david koski ::

Multiplying is often a scaling operation such as when edges or volumes are doubled in size.  Given an unchanging shape, meaning central and surface angles are held fixed, a doubling in edge lengths results in a two to the second power or four folding in area, and a two to the third power or eight folding in volume.

Starting with a cuboctahedron of edges root-of-two i.e. ~1.414214 and multiplying all those edges by phi (φ) results in a phi-to-the-third-power increase in volume.  The cuboctahedron's 24 surface edges and 12 radials (24 if seen as doubled) will now be root-of-two times phi. φ = half of one plus root of five or approximately:

>>> (1 + sqrt(5))/2
1.618033988749895

Finally, halving the difference in radial increase between these two, results in a third cuboctahedron that "harmonizes" with the icosahedron of edge-length-two.  The harmony consists in having both intersecting edges and coincident facial areas.

This "geography" of differently scaled versions of these polyhedrons has been variously mapped, including by R. Buckminster Fuller in his "explorations in the geometry of thinking" (or "synergetics" for short).  A "highway" between "places" may be a transformation, such as the Jitterbug Transformation, or, as above, a simple resizing.

SuperRT:                21.2132034
VE    (edge 2):         20.0000000
Icosa (edge 2):         18.5122959
SmallGuy:               15.8606454
RD6:                     6.0000000
RT5+:                    5.0077580
RT5:                     5.0000000 

SmallGuy will seem an idiosyncratic name, but then maps often contain folk names.  "SuperRT" is a rhombic triacontahedron scaled up by phi from its original size of 120 E-modules, a shape well-defined in Synergetics.  Said SuperRT embeds our Icosa of edges two as its long diagonals.  This same Icosa intersects and shares facial area with SmallGuy.

In sum SmallGuy, in this map, is a cuboctahedron "half way between" (edge-wise) the rt2-edge cuboctahedron and the phi-times-rt2-edge or say (rt2)(phi)/2 is the scale factor.  Starting with the same SmallGuy volume and multiplying by the sFactor * sFactor gets us the Icosa of edges 2 in volume, whereas one more application of the sFactor gets us the Cuboctahedron of volume 20, edges 2 (at the start of our Jitterbug Transformation).

Using some rational approximations in the Python shell:

>>> 15.8606454 * 1.0803630269509035 * 1.0803630269509035
18.512295822967804

>>> 18.512295822967804 * 1.0803630269509035
19.999999951112063

That's SmallGuy * sFactor * sFactor = Icosahedron (a volume expression)
Icosahedron * sFactor = Cuboctahedron (same edge lengths as Icosahedron)

Note that we're using tetravolumes as our standard (same as Synergetics).  Four unit radius spheres closest pack to define a tetrahedron of edges 2R (1D) and volume one.  The Icosahedron of volume ~18.51 and cuboctahedron of volume 20 both have edges of this same length (2R).

[Another "harmonizing" to map](http://coffeeshopsnet.blogspot.com/2010/05/interlacing-test-pattern.html) is the edge-crossing of the rhombic dodecahedron of volume six, Kepler's favorite space-filler and a "voronoi cell" for our unit radius spheres, and the volume 7.5 rhombic triacontahedron, inflated (scaled) by a factor of 1.5 from it's T-module beginnings.

The T- and E-modules have a "same shape" relationship with the E a tad larger in size (T-volume is 1/24).  The sFactor, used above, is the ratio of the S-module to the E-module or about 0.045084/0.041731.  More output from [a Python program](https://mail.python.org/pipermail/edu-sig/2014-May/011026.html):

Amod volume = : 0.04166666666666668
Bmod volume = : 0.041666666666666595
Emod volume = : 0.04173131692777366
Tmod volume = : 0.04166666666666668
Smod volume = : 0.045084971874737034
================
sFactor (Svol/Evol) =    1.0803630269509035