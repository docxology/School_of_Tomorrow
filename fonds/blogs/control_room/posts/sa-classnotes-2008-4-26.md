---
title: SA: ClassNotes 2008.4.26
id: 4951570579245235910
author: Kirby Urner
published: 2008-04-26T13:37:00.000-07:00
updated: 2013-12-04T12:24:25.003-08:00
blog: control_room
tags: 
---

The parking went more smoothly, plus the weather was good, got Ubuntu Dell and better speakers in harness no problem, with CodeGuardian queued.  However, without support from the home team, I'd've been leaning on staff too hard, having left my logins chart on my desk or someplace.

We worked pretty hard today, through [viztoyz](http://www.4dsolutions.net/cgi-bin/py2html.cgi?script=/ocn/python/viztoyz.py) and [povtoyz](http://www.4dsolutions.net/cgi-bin/py2html.cgi?script=/ocn/python/povtoyz.py), which take the real time versus render time approaches respectively.  The former uses [VPython](http://www.vpython.org/), the latter [POV-Ray](http://www.povray.org/).  The point of showing a movie like [CodeGuardian](http://video.google.com/videoplay?docid=6087974730400799810) is how such a small team now has these powerful tools, but you also need to really sit at the feet of great directors, to pick up on small touches like camera jitter, a way to help viewers join the action.

My Fibonacci generator, designed for phi convergence (which worked eventually), got off on the wrong foot, as 0, 1, 1, 2, 3, 5, 8... yields my sequence 1/0, 1/1, 2/1, 3/2, 5/3, 8/5...  So I got bitten by two gotchas:  divide by zero and default integer division (this is Python 2.5).  Fortunately, easy fixes were at hand.

I was able to show [my I Ching source code](http://osgarden.appspot.com/about.html) in a font that renders the characters readably, back to explaining the ASCII to Unicode migration, also part of this 2.x to 3.x transition.