---
title: Gnu Math on Synergeo
id: 115142683943248699
author: Kirby Urner
published: 2006-06-27T10:17:00.000-07:00
updated: 2016-06-21T19:16:17.016-07:00
blog: control_room
tags: 
---

So if you don't know about GNU: GNU is Not Unix was created by hackers who wanted free access to their tools, even as pesky administrators were moving in to own and control.

[GNU](http://www.gnu.org/) went for The Hurd, using new theories about kernel design, but Linux, a classic monolithic, beat The Hurd to the punch, for a time almost eclipsing GNU in the free and open source namespace.

GNU is a source of basic programmer tools necessary for kernel and userland development: text editors, parsers, compilers -- a complete workbench. You've probably heard of emacs, extensible in LISP.

What GNU features, above all, is a command line, per Neal Stephenson's classic [In the Beginning Was...](http://www.cryptonomicon.com/beginning.html). So Gnu Math means learning math at a command line, or in a shell (perhaps a more feminine way of saying it).

In the Python shell (Python, like Ruby, being a potential gnu math language), we explore ideas such as Rational Numbers, Numbers Modulo N, Polynomials, Vectors, Polygons, and Polyvertexia ([polyhedra](http://www.4dsolutions.net/ocn/polys.html)). It's a more discrete treatment, given the constraints of IEEE floating point and definitely sized registers. And that's just fine for doing synergetics, which uses discrete math anyway.

You'll have noticed "Polyvertexia" -- from Bucky in Cosmography -- and my Python module [rbf.py](http://www.4dsolutions.net/cgi-bin/py2html.cgi?script=/ocn/python/rbf.py) (optionally [quadray](http://www.grunch.net/synergetics/quadrays.html) based) is indeed the classic concentric hierarchy ala the two Synergetics volumes, products of the 1970s Renaissance.

The war in Southeast Asia was over, people thought a positive future was just around the corner. Then came the backlash: generations of anti-hippie took over, or seemed ostensibly to be so, and it became verbotten to really think Positive Future anymore (utopia), vs. some unending War on Terror (oblivion), which brings us up to date.

Out of this 1970s scenario also came the object oriented paradigm (OOP), in the form of SmallTalk, which Ward Cunningham, inventor of the Wiki, helped promulgate. Ward later infiltrated the Python community (he was more than welcome), as he, like Alan Kay, understood SmallTalk to be a dead language (perhaps resurrected in Ruby, also the spawn of Perl).

Ward joined PORPIG in recent years (Portland's Python Interest Group), which is how I came to have beers with the guy (I've had some beers with Alan too).

OO usually means using dot notation, a syntax where the object comes first (the thing), followed by action verbs with arguments (what Python calls "callables"), or by the names of attributes.

In SmallTalk, these were both varieties of message, and actually all attributes were private, accessible to outer globals only through setters and getters (as the Java people say). Please correct me if I'm wrong about these details.

So in gnu math (math in the shell, and also a pun on "[new math](http://www.math.rochester.edu/people/faculty/rarm/smsg.html)" or SMSG), we import from namespaces, such as RBF's synergetic one, and start playing with its objects, which, in the case of rbf.py, would be Tetrahedron, Octahedron, RhDodecahedron, Cuboctahedron, Icosahedron and RhTriacontahedron. What did I forget? Oh yeah, Cube. They're all inter-sized the proper way, and when you rescale any instance, their area and volume attributes change accordingly (as 2nd & 3rd powerings of the linear scale factor).

The class definitions themselves are [prefrequency](http://www.grunch.net/synergetics/terms.html), in the sense of non-instanced. They're like blueprints for a house. Any real instance (real house) needs to be constructed, meaning the nitty gritty details relating to persistence in time-size need to be defined (work often neglected by those working only with abstractions).

Python uses __init__ for this work, and in rbf.py, the above objects by default appear according to [our Fuller School tables](http://www.grunch.net/synergetics/volumes.html), such that volumes = {"Tetrahedron":1, "Cube":3, "Octahedron":4} and so on (that's an expandable dictionary).

In order to read the source code for rbf.py, gnubees must already understand a little about vectors, which I've developed as [coords.py](http://www.4dsolutions.net/cgi-bin/py2html.cgi?script=/ocn/python/coords.py) -- but there's no reason to just use my particular modules for such things. I'm just showcasing the general idea of gnu math and [CP4E](http://www.python.org/doc/essays/cp4e.html) (computer programming for everybody).

Your job would be to pick a preferred langauge and do your own explorations in this geometry of thinking. Here on Synergeo, and Synergetics-L before it, that's a longstanding tradition (to pick an executable language and go with it), and lots of collaborations have happened as a result notably around the Watermans ([Steve Waterman](http://watermanpolyhedron.com/watermanpolyhedra1.html)) and Elastic Interval Geometry ([Gerald de Jong](http://web.archive.org/web/19990417052812/http://www.beautifulcode.nl/), [Karl Erickson](http://www.applied-synergetics.com/ashp/html/struckvrml.html), [Alan Ferguson](http://www.beautifulcode.nl/cinema/avatars), [Kenneth Snelson](http://worldgame.blogspot.com/2006/05/barrel-tower.html) (off list) and [Russell Chu](https://web.archive.org/web/20040610092311/http://verbchu.com/)).

"Understanding about vectors" in a gnu math context of course includes writing code for them, probably in an OO language like Python. Mathematics is advertised as "an extensible type system" meaning we use the tools we already have to make new, improved ones, using the principle of synergetic advantage.

On the ground, making inroads with these ideas has been an uphill battle. People tend to hold their hands to their ears and holler "I can't hear you!" if you start up with any brand of Positive Futurism. They're all vested and geared to fight some War on Terror forever, and didn't plan to retool any time soon. The design science revolution was never on their agenda, and their presumption was the hippies were losers.

But times change, and hippies become hackers, and gnu math now percolates out and around cyberspace, through the various philosophical coffee shops and student union screening rooms. More people come to learn about the options now facing humanity. "Utopia or oblivion?" Bucky asked.

The twilight zone world power authorities seem hellbent on oblivion a lot of the time, but I think our design science brands are going to rock some boats for the better for a change. More kids will be "getting it" about our ability to succeed within a longer time horizon than the apocalyptics dare dream about.