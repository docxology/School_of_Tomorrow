---
title: Math Avoidance?
id: 6497961184668196792
author: Kirby Urner
published: 2015-06-24T11:53:00.001-07:00
updated: 2017-04-01T10:39:22.491-07:00
blog: control_room
tags: 
---

The accusation of "[math avoidance](http://mathforum.org/kb/message.jspa?messageID=9803473)" comes from those claiming our K-12 maths curriculum (using the UK plural) is too watered down, too diluted with geegaws and gizmos.  It's just "toy math".

Whereas I'm sympathetic to the accusation, I do need to ask if it's "math avoidance" to simply bury all the [late 20th Century innovations](http://controlroom.blogspot.com/2015/04/trite-math.html) documented in architecture, regarding the relationship of geodesic spheres to [the virus and buckyball both](http://www.4dsolutions.net/synergetica/synergetica1.html).

Is it wise to be so ignorant of this heritage?

[](https://www.flickr.com/photos/kirbyurner/18934772150)

Fig. 988.12 Icosahedron Inscribed Within Octahedron:
The four-frequency tetrahedron inscribes an
internal octahedron within which may be inscribed a
skew icosahedron. Of the icosahedron's 20
equiangular triangle faces, four are congruent with
the plane of the tetra's faces (and with four external
faces of the inscribed octahedron). Four of the icosahedron's
other faces are congruent with the
remaining four internal faces of the [ octahedron ]. Two-fifths
of the icosa faces are congruent with the octa
faces. It requires 24 S Quanta Modules to fill in the
void between the octa and the icosa.

Readers of [Synergetics](http://www.rwgrayprojects.com/synergetics/findex/fx0900.html) already know of the volume 20 VE, which contracts to a volume 18.51 Icosa [by Jitterbugging](http://controlroom.blogspot.com/2015/02/a-tale-of-two-logos.html).  That's our s-Factor at work i.e. (Svol / Evol) to the -1 i.e. Evol / Svol.

20 * (1  / sFactor) = 18.51...

As seen from the excerpt below, from a Python program, these two volumes come with "S + s3" and "E + e3" expressions for volumetric decompositions.

In this case-sensitive notation, S:s3 == E:e3 == Phi ** 3 i.e. the linear dimensions of s3 are 1/phi those of the S-module, ditto e3 vis-a-vis the E-module.

The S-module has a tetra-volume of pow(phi, -5)/2.

print("VE:         ", 20,                 420 * Svol + 100 * s3)
print("Icosa:      ", 20 * sFactor ** 1,  420 * Evol + 100 * e3)

With output:

VE:          20 19.99999999999996
Icosa:       18.5122958682192 18.512295868219162

Another Icosa-to-Cubocta relationship involves not Jitterbugging, but keeping the faces flush, eight of them, though only partially overlapping, as shown in the figure below: 

Fig. 988.00 Polyhedral Evolution: S Quanta Module:
Comparisons of skew polyhedra. 

We could call this a "skew" relationship and applying 1/sFactor twice to the 18.51 icosahedron takes use to what Koski affectionately calls the "Small Guy" cubocta, of volume ~15.86065.

What is it's frequency, assuming Icosa edges = 2?  Recalled 20 * F**3 is our formula:

print("Small Guy edge:", 2 * pow(sFactor ** -3, 1/3))

Output:

Small Guy edge: 1.8512295868219202

What's interesting about that number, a linear dimension, is that it's 1/10th the volume of the jitterbugged icosahedron's.  The differences in the ending digits above have merely to do with floating point error margins.

So what is the volume of the Icosa within the volume 4 Octa of Figure 988.12?

Clearly it's 4 - 24 * Svol or 4 - 24 * (pow(phi, -5)/2) = ~2.917961.
In Python again, and using David's decomposition formula:

>>> Svol = pow(phi, -5)/2
>>> s3 = Svol * pow(phi, -3)
>>> 60 * Svol + 20 * s3  # S + s3 form
2.9179606750063085

Applying the reciprocal of the sFactor twice more, to this tiny Octahedron-inscribed icosahedron, nets us the volume of its "skew mate":  the volume 2.5 cuboctahedron, i.e. 1/8 the volume of the cuboctahedron of volume 20, faces flush with the same Octa of volume 4.

>>> baby
2.9179606750063085
>>> baby * (1/sfactor) * (1/sfactor)
2.5000000000000107