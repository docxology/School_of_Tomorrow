---
title: Study Hall
id: 3204136081960058478
author: Kirby Urner
published: 2012-08-25T19:23:00.002-07:00
updated: 2012-08-25T19:34:31.921-07:00
blog: control_room
tags: 
---

Even in Windows XP I was able to get VPython working on Python 3.2 in a virtualenv, editing through PyCharm.  Then I pip installed redis just to prove I could do it, having spent much of the morning reading up on that.  Looks like interprocess JSON with persistence.  I didn't understand about messaging as my client seemed to block on listening, so how was that gonna help?  WinXP has both server and client, though not recommended for production use.

A blooming buzzing garden of such tools and toys, running in ensemble, with simple demo code, pared down, for teaching purposes, is what Free Geek might help staff, if not host.  OSDL?  There needs to be something more contemporary than a museum, although there's no rule against museums being contemporary, so maybe that's not right.  Portland Knowledge Lab was how I used to refer to it, copying London's (where I'd given a presentation on my way to a meeting), but I let that go out of focus when the Active Space experiment ended, in disillusionment with Metro Wifi.

My audience or client base, updating from CUE days, are still those do-gooder nonprofits and idealists.  But we're not in Kansas anymore, using WordPerfect + dBase (my "good old days").  Today, it's more about mod_wsgi (still) and Tornado and noSQL.  The clay, the source, is all out there.  "Use the source Luke" is the new commandment.  But are we getting anywhere?  Is STEM gaining in traction?

Redis has you talking through a port, I gather through sockets.  Surely those aren't HTTP requests.  No, it has its own protocol.  Like JSON in that respect.  The guarantee is transactions are atomic, as this is one thread (each redis instance).  You could probably sell seats with this thing, and not promise the same one to any more than one.

Before that, I was boning up on gevent + gunicorn, a hot new way to serve processes.  I couldn't tell if I'd use Celery in addition to or in lieu of, but I get the idea:  lots of event loops running in user space, context switching there, rather than kernel space (the mod_wsgi solution).  I watched a talk on Blip.TV comparing that dynamic duo with more traditional solutions.  Where high availability is concerned, gevent + gunicorn is looking pretty good, a plus for Python.

I've got DjangoCon on my radar.  Should I duplicate this WinXP configuration on Lion?  Yes, that would seem prudent.  The PyCharm product is something I might get an academic discount on, once we've completed a work process, but for now I'm just using on free 30 day trial.  Will it use Akbar font if I like, is a next question.  I'll get back to y'all when I figure that out.