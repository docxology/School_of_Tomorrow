---
title: OSCON 2015 Continues!
id: 3651587931831061374
author: Kirby Urner
published: 2015-07-23T12:21:00.001-07:00
updated: 2015-07-26T15:18:24.277-07:00
blog: control_room
tags: 
---

Tim O'Reilly held court in the Expo Hall during the break (sponsored by New Relic), after the UK's counterpart, the head of a US version of Digital Services, had given a keynote.

[PayPal with InnerSource](http://www.oscon.com/open-source-2015/public/schedule/detail/45365) is on the same page as other big enterprises:  the open source way of working, with tools that are open source, builds a better enterprise.  The shorter tag line:  Apache Inside (as in Apache Foundation projects; still a hotbed of open license technologies).  Walmart Labs has likewise standardized on the Open Source way inhouse, both using and contributing to the ecosystem, with a stack based on Node, Cassandra and Mongo in large degree, and moving to Trusty for a standard OS (Trusty is in the Ubuntu series).

[](https://www.flickr.com/photos/kirbyurner/19385056683/in/dateposted-public/)

Tim talked a lot about Technology to solve social ills by augmenting people power, not oppressing us. "Where's the Uber for eldercare?" he wondered, echoing ideas I learned about [from CareWheels](http://worldgame.blogspot.com/2005/07/wanderers-meeting-200575.html), a project to let people stay longer in their own homes with light monitoring and community support over the Web, in addition to in-home visits and services.

Uber does seem [a lot like Transporation Reaching People](http://mybizmo.blogspot.com/2006/07/deq.html) (TRP), originally administered by Clackamas County, software by me, in an age before smartphones.  "What about Technology for refugee camps?" asked Tim.  Indeed.  Any instant city needs ephemeral organs of self government, feedback loops mainly.  That's what journalism helps with, in the context of bigger picture framing viewpoints (oft referred to as "bias" but also "leaning" or even "leading" if using esoteric Quaker parlance).

Technology has the ability to create wealth (life support) by augmenting our powers.  As Amber Case pointed out in her later talk, with augmentation comes fear, including possible estrangement between those who "have" and those who "have not" whatever new powers we're talking about.  Other technologies are more restorative e.g. eyeglasses, used to bring people up to normative speeds. Her theme was [Calm Technology](http://www.ubiq.com/hypertext/weiser/acmfuture2endnote.htm), meaning feedback loops ranging from non-intrusive to subliminal (highly peripheral).  Suggest today's weather with light hues.  Ambient cues.  Atmospherics.

[](https://www.flickr.com/photos/kirbyurner/20011268381/in/dateposted-public/)

Luciano is running something concurrent to search for 192 country flag URLs, using all 676 letter combinations from AA to ZZ.  He's about to talk about Python's [new concurrancy features](https://speakerdeck.com/ramalho/).  He's (virtually) hitting against the CIA Factbook, first sequentially (five minutes) than concurrently, at first with five connections (one minute), then with a hundred connections he gets all the flags (thumbnail gifs) in under five seconds.  He does this all using Python's new native "green thread" capabilities.

I was just at Damian Conway's talk about extending Perl 5's syntax using new packages he's written, to make it a lot more like Perl 6.  One can even add new keywords in that language, by a kind of macro substitution process against the source.  Alex and Anna likewise did a language-centric talk on patterns in Python, calling out specific high level features in the standard library.

Advice to Pythonistas regarding asynchronous programming: start with learning generators thoroughly, and then study coroutines.  The newest Python (3.5 in 2015) has new keywords:  async def replaces the @asyncio.coroutine decorator and await replaces yield from.  An asyncio Task wraps a coroutine, giving an API allowing task cancellation and status checks.  The style suggested is a way of avoiding "callback hell" according to Luciano.

Luciano would later be wandering over to the Urban Airship site on the west side to deliver his talk to our Python User Group.  I hope I get to ask him how that went.

The grand finale talk for me today was co-worker Patrick Barton's presentation, about using some fancy "neo-cortical" algorithms (implemented in Python) to predict short term energy demand based on previous learning.  Then it was off to Amber's talk and the WalMart Labs mixer at Spirit of 77 across the street.

Training a Numenta instance is somewhat like training Dragon speech recognition software.  In this case, the "voice" was the collective energy demand of some 116 households in Austin, TX (the site for next year's OSCON as fate would have it). Paul (co-worker) and I adjourned to Lucky Lab on Hawthorne in his company car (different company -- he has two jobs) for a nightcap with Ben (former co-worker) and a fellow car nut, then I hopped a bus home.

Tomorrow I think I'll start out walking Mt. Tabor again.  It's been quite awhile.  I've been working on [healing the ankle](http://mybizmo.blogspot.com/2015/07/cooling-my-heels.html).  Then I'll watch the opening keynotes [via live streaming](http://oscon.com/live) before trekking over there for closing ceremonies.

[](https://www.flickr.com/photos/kirbyurner/19934859766/in/dateposted-public/)

:: amber case (esri) ::