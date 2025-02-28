---
title: Code School Evening
id: 8566330864345515096
author: Kirby Urner
published: 2016-08-29T23:06:00.000-07:00
updated: 2016-09-09T10:51:12.392-07:00
blog: control_room
tags: 
---

[](https://www.flickr.com/photos/kirbyurner/29251699301/in/dateposted-public/)

minecraft-based demo of on-board GPU

The new bike has a nifty pump, which I used tonight, to get back over Tillikum.  Then I walked it home, slanting through to Palio in Ladd's, up Harrison passed [St. David of Wales](http://worldgame.blogspot.com/2012/04/spring-cleaning.html), and the LDS campus.  Home before 9:30 PM, with a bright red rear light the whole way, even when walking.

Ladd sisters, of the family for which this Addition is named, before my time, used to have [a photography school](http://worldgame.blogspot.com/2009/01/columbia-gorge-recent-history.html) way up the Gorge on a houseboat.  The Columbia Gorge had only recently opened to a new form of tourism involving scenic photography as a hobby. 

At the code school tonight I fired up [the Pi again](http://controlroom.blogspot.com/2016/08/accelerator-project-continued.html), on the HDTV. I had my 4D stills.  Ray traced.  I say 4D as [a kind of branding](http://worldgame.blogspot.com/2016/07/another-introduction-to-tetravolumes.html), not referring to Time.  Ben had a new Pi too, same make and model, and he and another guy helped me catch up on Minecraft a little, at least in create mode.  Peter Farrell is still ahead of me there.

These 4D shapes are ordinary convex polys, generated using [the geodesic program](http://www.antiprism.com/programs/geodesic.html) in Antiprism, a suite of tools by Adrian Rossiter.

I've been working on getting his C++ to compile on the ARM chip in a small [Raspberry Pi 3](http://worldgame.blogspot.com/2016/08/pov-ray-on-pi.html), Model B. The thing boots off its GPU which doubles as a sort of BIOS.  The Pi3D module, imported within Python, seems to be getting full value from said Graphics Processing Unit.  Farrell's [Hacking Math Class](http://controlroom.blogspot.com/2016/06/thirsters-201663.html), uses Pi3D quite a bit, also the turtle module.  Wifi is also built in.

I also compiled Povray, a program I used in Windows a lot, way back in the days of CompuServ.

Now that this tool chain is working, I can do something like this...

geodesic -c 1 -f 6 > output.off
off2pov render_me.pov output.off
povray -Irender_me.pov

That's roughly how it goes, minus some switches. I get a PNG file out the end, suitable for tweeting.  Some of the STEM teachers already have a stack of Pis and are looking for worthy projects.  I've been [filing my reports](https://flic.kr/p/KCeeC8).

I introduced myself quickly as "a lobbyist" as we went around the circle, mentioning my work with the teachers, especially high school math teachers.

I had Peter Farrell's book in my briefcase, strapped to the bicycle.  It sits next to my Pi Station in the CodeCastle as well (I've also used CodeCastle with reference to a certain neighborhood "[ghost church](http://worldgame.blogspot.com/2016/06/ghost-church.html)", but that's still speculative fiction at this point).

Someone brand new to Portland, just moved here, expressed his intent to dive into Natural Language Processing more. We talked about Elisa, Racter (another "convo-bot"), the Tom Sawyer corpus, and setting up a measuring protocol of some kind.  The algorithm could measure negativity in some way, for example.

This wish for a protocol is characteristic of Nat's project as well, relating to motion and profiling autistic features. [Nat](http://mybizmo.blogspot.com/2006/08/adventures-in-toontown.html) and I have followed up a bit since our meeting, regarding the recently proved Kepler Conjecture, seeing as how the proof bridges mathematics and computer science, a theme in [my lobbying for Measure 97](http://controlroom.blogspot.com/2016/07/back-in-lobbyland.html).

(Art + Code + High) * School = 
Art School + Code School + High School

Here's a way [for teachers](http://worldgame.blogspot.com/2016/09/gateway-to-asia.html) to generate more synergy amongst themselves, from which their students might benefit.

I'm back in the world of bicycle tubes and tires, not a bad world to be in.  It got me there just fine, even with the slow leak.  Coming back, I needed the walk anyway.

Regarding Antiprism, I don't currently use antiview, the included highly capable viewer, 
because the flavor of OpenGL used on the Pi was not Antiprism's target 
OpenGL or development platform.  Antiview compiles, just isn't 
displaying content correctly. That's OK.  Having povray working gets me where I want to go.

[](https://www.flickr.com/photos/kirbyurner/29251687341/in/dateposted-public/)

antiprism + povray on a Pi 3

Got the flat tire mentioned in my code school blog fixed. [https://t.co/dp2WwgXTpl](https://t.co/dp2WwgXTpl) Joe's Bike Shop, Chavez & Lincoln [#pdx](https://twitter.com/hashtag/pdx?src=hash) [#4d](https://twitter.com/hashtag/4d?src=hash) [#CodeCastle](https://twitter.com/hashtag/CodeCastle?src=hash)
— Kirby Urner (@4DsolutionsPDX) [August 30, 2016](https://twitter.com/4DsolutionsPDX/status/770711579432103937)