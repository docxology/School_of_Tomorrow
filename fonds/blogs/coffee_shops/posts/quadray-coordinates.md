---
title: Quadray Coordinates
id: 3476799079968929270
author: Kirby Urner
published: 2016-04-20T00:14:00.002-07:00
updated: 2016-06-13T10:05:14.866-07:00
blog: coffee_shops
tags: 
---

[](https://upload.wikimedia.org/wikipedia/commons/9/99/Quadray.gif)

Traditional XYZ vectors:

A lot of what I'm writing here applies to teaching (x,y,z) vectors of the ordinary kind.  

Given six vectors: {(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)} we're able to reach any point in RxRxR (volume) as addressed by (x,y,z) using:

(A)  the operation of addition (V + V -> V, V a vector)
(B)  the operation of scaling (s * V -> V, s a scalar)

(A) is the familiar tip-to-tail linking of vectors, whereas (B) allows for "grow" (extend) and "shrink" (shorten), as well as "reversal" (180 degree flip).

One could say {(1,0,0),(0,1,0),(0,0,1)} with (A) and (B) is sufficient to span R3 (RxRxR) given simply negation, which we could call "multiplication by -1" i.e. (-1) * (1,0,0) = (-1,0,0).

Without flipping 180 degrees, and given only positive scalar multiplication, the original three basis vectors only span one octant of XYZ space: the all-positive octant.

If negation is allowed, then one more vector: -(x+y+z) would be sufficient to give an all-octant spanning set (we would have the caltrop again, albeit with different angles).

We may think of XYZ vectors as a "jack" of six spokes (six rays) emanating from the origin.  We can put a cube around the origin (0,0,0) and show the six rays poking through the face centers of said cube.  In this scenario, all vectors tail-originate i.e. they have one end at the origin.

When we add vectors, we may place them "tip to tail" which conceptually involves translating one vector such that its tail is at the tip of the other, but the sum of the two is once again tail-originating.

If we wish to express a line segment that does not have an end at (0,0,0), we express it with two end-point vectors.  That would give us the line segments needed to build any wire-frame polyhedron.

Quadrays:

Quadrays likewise span R3 but start with only four rays instead of the six in XYZ (including the three 180 degree flipped basis vectors, for reaching all eight octants with only positive number scaling).

These four basis vectors may be expressed as: {(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)} and span all
of R3 using addition and scaling, without needing the "flipping" operation.

All points are reached as a linear combination of these basis quadrays, each scaled in the direction it's already pointing.

Again, instead of a "jack" of six vectors, we have a "caltrop" of four.

We may draw them from the origin (0,0,0,0) to the four corners of a regular tetrahedron.

XYZ & Quadrays Together:

How shall we orient the regular Quadray tetrahedron vis-a-vis an XYZ cube?  

The canonical relationship I'm using puts (1,0,0,0) at the corner of a cube in the first XYZ octant, the all positives octant.  The corresponding tetrahedron has corners in octants (+,+,+), (-,-,+), (-,+,-) and (+,-,-).

Picture two line segments, one above the XY plane, the other below it, at 90 degrees to one another (but not intersecting).  Either edge may be considered a "spine" with "wings tips" at the other edge's end points.

See Figure:

[](http://www.grunch.net/synergetics/quadray/cube.gif)

The cube is upside down i.e. the XYZ positive octant is where we would usually put (1,0,0,0)). Quadrays are shown in blue.

However the size of this cube is "all face diagonals = 2" which means the so-called "basis vectors" (four of them) are not "unit" in length.  What's more important, for a starting place, is that the edges of this canonical tetrahedron have all edges 2.  We might call this the "basis tetrahedron" (or "home base").

What is this cube of face diagonals 2 relative to in terms of sphere packing?  Think of three unit radius balls packed tightly into a triangle with a fourth ball nested on the valley these three form, on either side of the triangle.

That makes a tetrahedron of balls with edges going from ball-center to ball-center.  Each edge has length 2R (twice the radius of each ball) or D (the diameter of each ball).

Figures:
[http://www.rwgrayprojects.com/synergetics/s09/figs/f86161.html](http://www.rwgrayprojects.com/synergetics/s09/figs/f86161.html)
[http://www.rwgrayprojects.com/synergetics/s04/figs/f1105.html](http://www.rwgrayprojects.com/synergetics/s04/figs/f1105.html)

Vector Addition:

How do we add two vectors in XYZ?  Easy:  we simply sum their respective (x,y,z) coordinates.  If v0 = (x0,y0,z0) and v1 = (x1,y1,z1) then v0 + v1 = (x0+x1, y0+y1, z0+z1).

Concrete example: (1,2,3) + (-1,-2,-3) = (0,0,0).

Negating the first set of basis quadrays to get a second set, i.e. the remaining four corners of the 8-vertex cube, may be done with scalar multiplication, however the second set of quadrays defining the "inverse tetrahedron" (the dual of the first, same volume) does not need to introduce any negative numbers.  

The first set was already sufficient to map (span, address) space, so our 4-tuples are free to remain entirely non-negative in their final (reduced, normalized, canonical) expression.

- (1,0,0,0) = (-1,0,0,0) = (0,1,1,1)  (i.e. 180 degree flipped)
i.e. a vector pointing oppositely.

The four "negative" quadrays, pointing at 180 degree to the first four would then be: 

{(0,1,1,1),(1,0,1,1),(1,1,0,1),(1,1,1,0)}.

The two sets together define the eight vertexes of a cube.

Note the four pairs of inverse vectors always sum to the identity vector e.

(1,0,0,0) + (0,1,1,1) = (1,1,1,1) = (0,0,0,0) = e

(0,1,0,0) + (1,0,1,1) = (1,1,1,1) = (0,0,0,0) = e

and so on.  XYZ is the same way:  v + (-v) = e = (0,0,0).

We see that the operation of vector addition with quadrays involves a two step algorithm: 

Step 1: add corresponding elements in each 4-tuple, then

Step 2: normalize to the canonical representation using an identity bringing the minimum element (which may be a negative number) to zero. 

Subtracting two quadrays is syntactic sugar for adding the inverse i.e. q0 - q1 = q0 + (-q1).  A negated quadray may always be expressed in canonical (non-negative element) form.

Example:

(1,1,2,0) - (3,1,1,0) = (1,1,2,0) + (-3, -1, -1, 0) = (-2, 0, 1, 0) = (-2, 0, 1, 0) + (2,2,2,2) = (0, 2, 3, 2)

We might also do it this way: (1,1,2,0) - (3,1,1,0) = (1,1,2,0) + (0, 2, 2, 3) = (1, 3, 4, 3) = (0, 2, 3, 2)

Note that (1,3,4,3) is not canonical form either, as we still need to apply Step 2:  subtract the minimum element from all four i.e. (1,3,4,3) - (1,1,1,1) = (0,2,3,2).

We're done when one or more elements is 0 and the others are non-negative.

A secondary canonical form, used interimly in some algorithms, allows negative numbers but requires the four coordinates add to zero.  (2,0,1,1) becomes (1,-1,0,0) by adding (-1, -1, -1, -1).

Any (a, a, a, a) = (0, 0, 0, 0) = e because the four vectors (a,0,0,0) + (0,a,0,0) + (0,0,a,0) + (0,0,0,a) cancel one another out and sum to the origin.   

XYZ is like this too: adding all six spokes of "the jack" nets to the zero sum vector i.e. e (identity element for vector addition).

Conclusions:

What's been defined above so far is sufficient to provide:

(i) a distance formula (length formula) for any quadray vector, such that |v| -> Number were v is a quadray (this is well developed in other writings, as well as in computer code).

(ii) a conversion algorithm whereby any (x,y,z) coordinate may be expressed as a unique quadray in canonical form, and vice versa:  every quadray may be expressed in (x,y,z) coordinates (also implemented).

One property of Quadrays that's interesting then, is they're isomorphic to XYZ. 

Consider that spherical coordinates (r, theta, alpha) are also a useful expression of all the same points  addressed by (x,y,z).  Isomorphism is a feature, not an unnecessary redundancy.  Sometimes computing in an alternative representation is more convenient and/or generative of new insights.

Quadray coordinates, like spherical coordinates, give another unique address for the same point in space. They could be introduced in conjunction with spherical coordinates as an alternative representation.

Another property of quadrays is their ability to sum, using only positive integer 4-tuples, to give the vertexes needed for a canonical set of concentric polyhedrons, starting with the basis tetrahedron of edges 2R and volume one.

Volume one?  That's not conventional in XYZ thinking either, but we have a logical foundation for using this alternative model, with [a triangular analog](http://controlroom.blogspot.com/2016/03/ethnomath.html). The implications of this alternative logic are worth exploring.

If we adopt the unit-tet model then we likewise get whole number volumes for (volumes in parens):

- the canonical quadray cube described above (3) 
- its dual octahedron where edges cross (4) 
- their combination as a rhombic dodecahedron (6) and 
- the 12-balls-around-1 cuboctahedron that characterizes any ball in the CCP lattice (20).  

For example the corners of the latter cuboctahedron are simply the 12 points: 

{(2, 1, 1, 0), (2, 1, 0, 1), (2, 1, 1, 0), (2, 1, 0, 1), (2, 0, 1, 1), (2, 0, 1, 1),
 (1, 2, 1, 0), (1, 2, 0, 1), (1, 1, 2, 0), (1, 1, 0, 2), (1, 0, 2, 1), (1, 0, 1, 2),
 (1, 2, 1, 0), (1, 2, 0, 1), (1, 1, 2, 0), (1, 1, 0, 2), (1, 0, 2, 1), (1, 0, 1, 2),
 (0, 2, 1, 1), (0, 2, 1, 1), (0, 1, 2, 1), (0, 1, 1, 2), (0, 1, 2, 1), (0, 1, 1, 2)}

i.e. all combinations of {2,1,1,0}.  

Restricting quadray addition to a pool of only these, disallowing any scaling, gives the vertexes of the CPP (= FCC), the dense-packing (~74% ) of unit-radius balls, a "home base" in crystallography.

Also true, though not proved here:  any tetrahedron defined by four CCP vertexes has a whole number volume relative to our canonical reference tetrahedron of volume one.

For further reading:
[The Quadray Papers](http://mathforum.org/library/view/6236.html)
[Posting to mathfuture](http://tinyurl.com/j2cslya) (April 25, 2016)

[](http://controlroom.blogspot.com/2016/03/ethnomath.html)