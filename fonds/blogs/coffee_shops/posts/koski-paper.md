---
title: Koski Paper
id: 3865809573570449770
author: Kirby Urner
published: 2017-06-17T15:05:00.000-07:00
updated: 2018-12-12T14:32:03.689-08:00
blog: coffee_shops
tags: 
---

[Original 2015 paper](http://controlroom.blogspot.com/2015/04/trite-math.html) by David Koski:

[ note typo:  "It has a volume of 5(√2)ø2 = 18.52295." should read "18.512296...". ]

What's an S module?

The canonical octahedron of volume 4 has inscribed within it, faces flush, an icosahedron of smaller volume.

Their volumetric difference, carved into 24 modules, four meeting at each octahedron vertex, comprise the S modules, 12 the mirror image of the other 12.

The S mod's volume is (φ **-5)/2 relative to unit volume tetrahedron of edges equal those of the canonical octahedron.

[](https://www.flickr.com/photos/kirbyurner/6335726352/in/photolist-vLby2U-ujipN3-f75zUP-aDSfHf-8ryEix-8ryECF-7mcmne-5zTRjp-5zY9gA-7k4Eid-7k4Em5-7jZLe2-7jZLhp-7k4Ejf)

What's an E module?

Take the Rhombic Triacontahedron (RT) that precisely shrink-wraps a sphere (as does the Rhombic Dodecahedron of volume six), and you will find that in tetravolumes it slightly outweighs the RT of volume precisely 5, with 0.9994... the radius.  Explode this 5+ volume RT into 120 wedges and you'll have your E modules, left and right.  The slightly smaller RT of volume 5 is made from T modules.

Following David's paper, we scale S and E modules up and down, by the golden ratio.

I use the convention that lowercase means "scale down" as in "shrink" and capitalized means "scale up" as in "expand".

Since to scale edges by a linear factor (in this case φ) is to change volume by a 3rd power of that factor, the numbers 3, 6, 9... are used to indicate by how much volume has changed up or down i.e. by φ**3, φ**6 or by φ-3, φ-6.

Examples:
smod6 means Smod * (φ**-6) 
Smod6 means Smod * (φ ** 6)

In the Python code below, we're confirming that the concentric hierarchy volumes of the tetrahedron, cube, octahedron, icosahedron, may be expressed in lowest term sums of S and E modules of mix scale.

Related Python code (hit the run button to compute output, appears at bottom):