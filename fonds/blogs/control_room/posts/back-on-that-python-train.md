---
title: Back on that Python Train
id: 5951222464077755425
author: Kirby Urner
published: 2016-12-18T10:31:00.000-08:00
updated: 2016-12-19T17:44:59.668-08:00
blog: control_room
tags: 
---

[](https://www.flickr.com/photos/kirbyurner/31590014101/in/dateposted-public/)

By "Python Train" I mean the succession of versions, fine to come in from the top i.e. no reason to go back and learn older ones, unless you inherit responsibility for older code.  I've got quite a bit of 2.x on the web, [at Oregon Curriculum Network](http://4dsolutions.net/ocn/).

However 3.6 is out, final release candidate, with the first official non-candidate set for release on the 23rd.  I've learned about formatting strings from Chris, [CTO at PDX Code Guild](https://youtu.be/TKhgl38EPPg?t=28s).

But only recently, in coming late to [various debates](https://eev.ee/blog/2016/07/31/python-faq-why-should-i-use-python-3/), did I get a longer run-down of new features, which inevitably include many other less new ones I'd been overlooking.

Since I'm in the teaching biz and like any professional have to keep doing homework, working on updating skills with latest new wrinkles, I'm taking advantage of [snow days](http://worldgame.blogspot.com/2016/12/sampling-python-tutorials.html), with power, to bone up and stay with it.

There's a sense of being on a moving train here.  Time to move along.  Inertia.

We always do a Hanukkah party this time of year, though we're Quakers and all that. Great traditions. good times, great peeps. My family is all spread out.  White Christmas in Portland (actually not yet, this is in the lead up to), snow and ice both.

Of course I'm thinking of Lindsey's "...get on that train" lyrics (and melody).  She later moved it to Spanish.  I caught [a version for Youtube](https://youtu.be/h923W5h3-oM) some years ago.  Merry Christmas Lindsey wherever you are. I hope we cross paths sometime in 2017.

For those of you squinting at the code above (click picture for original, bigger), yes, all "clerks" (what I'm calling them) named "sentinel" or "nigel" or whatever, will file to the same key.

Before you throw up your hands and yell "bug!" or "security risk!" or whatever, remember a use case where we have freeway cams all along the highway.  All cams file to "see it!" and all users of "last_seen" have it in them already, no need to "subscribe" (you did that by naming the clerk as the others did).

The version below assumes we need to keep each value stored with its specific instance, including across types (instances serve as unique keys regardless of type).  What you need from your clerk type varies with use case; Python gives you the "hooks" (the places to fill in the script).  For consenting adults (one of the tag lines).  Batteries included.  Fits your brain.

The takeaway is one does need a clear head, to keep track of what "self" means when several classes have instanced the clerk as a class-level name.

The clerk has a window orthogonal to the type structure, or "the committees" one might say, is privy to what goes on across instances.  Must it keep all those instances straight?  Or is the goal to share information?  Or both?  The language is more about allowing than dictating your designs.

So just remember to document clearly and tell a compelling story to future maintainers, or they'll end up rewriting it just to keep track of what's going on.  Don't just assume the code "will speak for itself" — to you it might, but remember the other people in the room.

[](https://www.flickr.com/photos/kirbyurner/31352623520/in/dateposted-public/)