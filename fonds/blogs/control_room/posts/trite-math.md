---
title: Trite Math
id: 2024604939234251179
author: Kirby Urner
published: 2015-04-16T14:33:00.004-07:00
updated: 2017-08-10T23:03:22.954-07:00
blog: control_room
tags: 
---

Держись!

According to the [Bridges](http://bridgesmathart.org/) trolls, i.e. the [kick-and-punch reviewers](https://mail.python.org/pipermail/edu-sig/2015-April/011229.html) who come out from under the bridge when someone proposes to cross it, the relationship VE:Icosa :: S:E is of no conceivable import, cultural, artistic or otherwise.  So be it.  Lets call it Trite Math (Koski's coin).

VE is a remote vocabulary word in [the Synergetics namespace](http://wikieducator.org/Synergetics), pioneered by the ever-lonely Bucky Fuller.  VE stands for Vector Equilibrium.

Rational ancient Greek speakers know it as the "cuboctahedron" although that suggests a solid shape, not the skeletal version with doubled radials, eight hinge-bonded unit-volume tetrahedrons, per [Concentric Hierarchy lore](http://mybizmo.blogspot.com/2006/09/focal-points.html).

That's twenty-four radial versus twenty-four circumferential vectors in Bucky's accounting system and vocabulary, hence the name "vector equilibrium" ([twenty-four](http://mybizmo.blogspot.com/2015/04/kirbacademy.html) of each).

The shape is barely stable however, only fleetingly itself.  [It Jitterbugs](http://controlroom.blogspot.com/2015/02/a-tale-of-two-logos.html) into an Icosahedron of equal edge lengths, the Icosa in the ratio above.  In so doing, the volume decreases from 20 (the eight tetrahedrons are volume one, six half octahedrons volume two, so 8 + 6*2 = 20) to about 18.512... (more digits).

S & E are both slivers, splinters.

The topologically minimum container in ordinary space and ordinary language, is the tetrahedron.  You don't have a volumetric "cage" with less than six edges, if constrained to constructing with sticks.  Fuller accounts volume using aggregates of these slivers, which he names:  A, B, T, E and S.

You can [look them up](http://www.rwgrayprojects.com/synergetics/findex/fx0900.html). They have plane nets and everything. A, B and T all have the same volume (1/24).  E outweighs T by a tad, has the same shape.  S is for Skew.

So VE:Icosa :: S:E is a volume thing.  David Koski has been [playing with these blocks](http://www.4dsolutions.net/synergetica/synergetica5.html) and making lots of discoveries.  Low hanging fruit (i.e. trite fruit) is plentiful in this [4D domain](http://4dsolutions.net/).

Lets do it in Python:

e3 is simply Evol shrunk by 1/[phi](http://coffeeshopsnet.blogspot.com/2014/12/freaking-about-phi.html) i.e. all edges are .618... of what they were, with volume decreasing as 3rd power of that amount.  Edges:Area:Volume grow and shrink in a 1, 2, 3 powering relationship when a shape changes size (duh).

I agree this is [all pretty easy and accessible](http://controlroom.blogspot.com/2015/06/math-avoidance.html), which in some circles is a mark of inferiority, of triteness.

[ The fact that floating point numbers have noise digits on the end owing to base conversions etc. may be off-putting to "[real numbers](http://mathforum.org/kb/message.jspa?messageID=9742355)" fans. ]

Cliché Math we could call it.  Cut and Paste Math.

Speaking of which, the source code for studying the above modules is [available here](https://mail.python.org/pipermail/edu-sig/2014-May/011026.html) on [edu-sig](https://www.python.org/community/sigs/current/edu-sig/). 

The source to render the above graphic is [also available](https://mail.python.org/pipermail/edu-sig/2015-March/011203.html), but you'll need the free / open source [POV-Ray](http://povray.org/) ray tracing engine to get the final result.

Rejected, too-trite and/or [incomprehensible](http://worldgame.blogspot.com/2005/12/incomprehensible.html) papers: 
[Bridging XYZ and IVM Volumetric Accounting Systems with the Square Root of 9/8](http://4dsolutions.net/synergetica/bridges_paper_final.pdf) by Kirby Urner
[Revisiting R.B. Fuller's S & E Modules](http://coffeeshopsnet.blogspot.com/2017/06/koski-paper.html) by David Koski