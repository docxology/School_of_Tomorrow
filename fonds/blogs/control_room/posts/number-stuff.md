---
title: Number Stuff
id: 5492048310278184056
author: Kirby Urner
published: 2018-01-27T21:28:00.001-08:00
updated: 2018-01-27T21:50:17.580-08:00
blog: control_room
tags: 
---

Wow, or "wuf" ("woof"?) as Arnie would say (that's Dr. Arnold Mindell, PWI PDX) regarding the fast turnaround between David's and my experience, between asking a question and David's finding just the right Youtube, only recently published (like two days ago).

The question was this: we know regarding Phi, the Golden Ratio of 1.1618..., that its reciprocal is equal to itself minus 1.  So: for what other numbers is it the case that |1/N - N| == {1, 2, 3...} i.e. some integer.

Did I get that right?  Yeah that seems so: check 3.16 above.

David had stumbled on √10±3.  Switch to Python:>>> from math import sqrt>>> N = sqrt(10) + 3>>> N6.16227766016838>>> 1/N0.16227766016837933>>> N-60.16227766016837997

You'll see some floating point inaccuracies here, but the idea is clear.  Looking at the other number:

>>> N = sqrt(10) - 3>>> N0.16227766016837952>>> 1/N6.162277660168372

Again, the absolute distance on some number line, between N and its reciprocal 1/N, is precisely 6.  We're calling these the Metallic Ratios, punning of Golden.  

Each sigma (Metallic Number) is equal to the negative of its own reciprocal. That's true if we go with 3±√10, as -(3-√10) = √10 - 3.

>>> from decimal import Decimal>>> Decimal(10).sqrt() + Decimal('3')Decimal('6.162277660168379331998893544')>>> N = Decimal(10).sqrt() + Decimal('3')>>> NDecimal('6.162277660168379331998893544')>>> 1/NDecimal('0.1622776601683793319988935444')>>> 1/N - NDecimal('-6.000000000000000000000000000')  

Here I'm showing off the option to use a standard library decimal type instead.  There's a [gmpy2](https://pypi.python.org/pypi/gmpy2/2.0.8) out there as well, that will perform similarly, in terms of extending the realm of precision using base 10 representations.

How many decimal points you need is something you can specify, the default being 28, quite a bit more precision than faster floating point provides.