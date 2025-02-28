---
title: Spy Stories
id: 7537762300413131749
author: Kirby Urner
published: 2020-12-25T12:30:00.001-08:00
updated: 2020-12-25T12:33:21.668-08:00
blog: control_room
tags: 
---

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhWrw92q4B5AHAZKbuFThlv_r1U1C8OSPCqXczd77zMw3PfOO8Inod_9R-s35kY3NnWEj5Y1XQooVNvCuHar_R5Vu88bGz4543Pp4xm_DPN2qJDnUKjanuFSOOoSG97_qWzfnFU/s473/50751672167_e24336003f_o.jpg)
The Navalny story has gotten cringe-worthy, what with the underwear-borne novichok, ew. The tabloids have their readership, expanded immensely by cable television. Hearst was just the beginning.
The SolarWinds story is more interesting. I'm dubbing it Solaris (Солярис), since everyone has their clever "burst of sunlight" metaphor, and Solaris has the Russian angle, although the original author was Polish. 
Will Self got me watching it again recently.

The story stays shallow around the most interesting part, which we can leave to "made for DVD" movies. That's where a basement test lab will imitate one of the Fortune 500. Call it Project 501. 

This is where an elite core of Russian hackers, working for the Russian government, set up SolarWinds Onion (a subtle clone, but with a lethal difference) on a supposedly secure platform.  Get ready to infiltrate.

But don't we have to exfiltrate first, to get the new Cozy Bear payload inside the DLL? Rolling a DLL requires source code tobacco.  Microsoft:  almost 4000 lines.

A dynamically linked library that still does its regular job, if triggered, or at least looks like it will.  

If it's seriously bloated with all these fancy new features, you won't need a SHA sig to see it's been tampered with.  Apparently the cybersecurity whiz team doesn't notice when a DLL suddenly bloats. Nothing goes blip on the radar. Makes sense: that's why the digitally signed certs.
I'm looking forward to some side by side comparisons, of:SolarWinds.Orion.Core.businessLayer.dll as usual, next to the one with the payload. The museum of clever hacks is readying a display case even now I bet.  Actually, Microsoft is providing some of that.
Indeed, I'm "advising all my clients" to preserve their businesslayer.dll (just make a copy) if they find out they're using Onion (vs Orion), and many would likely be doing that, even if not my clients. 

The compromised configuration is valuable and any Fortune 500 company worth its salt is going to snag a working version of the hacked product for its people to train on, and for its lawyers to write suits about. Actually, without the source code, the raw binary ain't that useful.  Still... a souvenir. 

We're hoping SolarWinds coughs up the source soon (it has, we're seeing some of it), or is the story it was black bagged in a perfume bottle?
[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8Z7caLtkhM3cKvmr1gT7IpWacpPZKayJoAbvrl0TysIEzZ2G2gWQ8oc_alL8BP2Hb5rhF1XjWtEOIVsJk_1u-W3Xjf5U8lPxSFo-IrNc0wQ-2S-mNNt9LDFqipMSvAOZ20mPf/s1642/novichek.jpg)