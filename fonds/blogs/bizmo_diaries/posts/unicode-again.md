---
title: Unicode Again
id: 1085409393016688703
author: Kirby Urner
published: 2015-08-14T16:08:00.001-07:00
updated: 2015-08-14T18:28:36.063-07:00
blog: bizmo_diaries
tags: 
---

[](https://www.flickr.com/photos/kirbyurner/20570670622/in/dateposted-public/)

I just discovered some bogus information I'd been purveying, which is that UTF-8, a way of encoding [Unicode characters](https://en.wikipedia.org/wiki/Unicode) (actually code points), may include up to six bytes per character.

In fact, that used to be the standard, but per [RFC3629](http://tools.ietf.org/html/rfc3629), when Unicode merged with an ISO standard, the cut off was set to 4, covering hexadecimal numbers U+0000..U+10FFFF.

The Python docs themselves give a clear, if abbreviated, introduction to the history:

There’s a related ISO standard, ISO 10646.  Unicode and ISO 10646 were
originally separate efforts, but the specifications were merged with the 1.1
revision of Unicode. 
This [featured chronology](http://www.unicode.org/history/versionone.html) at the Unicode.org website seems to stop in 1992 and doesn't talk about the 1.1 revision.