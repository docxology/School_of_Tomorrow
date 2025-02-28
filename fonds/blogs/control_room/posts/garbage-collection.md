---
title: Garbage Collection
id: 115316939776367115
author: Kirby Urner
published: 2006-07-17T13:50:00.000-07:00
updated: 2006-11-15T11:44:21.293-08:00
blog: control_room
tags: 
---

In part, that's to answer the question "what does Python bring us?".A little history is in order here:  runtime memory has been expensive and scarce, and one of the worst crimes was to write resource hog programs that took more memory than necessary.Now, some applications unavoidably require gobs of memory, but the least you can do, as a programmer, is explicitly deallocate what you've allocated.  Free up the resources you're not using when you're done with them.  Don't make other processes do all the work to clean up and  reclaim.Put simply:  clean up your own messes.What garbage collection supplies, is an automated bookkeeping service for determining what bits of memory are ready for recycling.  The coder doesn't have to worry so much about being a memory hog, as the virtual machine on which the coder's code executes, is already quite resource aware.  When it allocates from the heap, it does so with strings.In Python, when a list, tuple or dictionary is no longer referenced, it simply goes away.  The garbage collector comes along (exactly when usually isn't your concern) and cleans house.Clever programmers will now insist that garbage collection is for sissies.  If you want lean and mean code, do your own allocating and deallocating.But the truth is, we don't always want our code lean and mean.  Sometimes we like comfortably fat Python, well fed.  Maybe it just ate a goat.Anyway, it's easier for us to be lazy a lot of the time.   Hackers, meet Slackers.  Slackers, Hackers.  Shaking hands all around.Python fills a niche, is not all things to all people.  Use it when it's smart to use it, but always be open to using something else if/when the situation demands it.