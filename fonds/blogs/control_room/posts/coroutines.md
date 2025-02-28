---
title: Coroutines
id: 6320669117114527749
author: Kirby Urner
published: 2017-05-23T09:44:00.002-07:00
updated: 2017-05-23T09:59:38.136-07:00
blog: control_room
tags: 
---

I see refugees from Chef World (aka "the kitchen") trying their hand at coding, and thinking they're making a big leap. Yes, they are, in a way, but in other ways a short order cook is a study in workflows, and an algorithm is a semi-numerical recipe.

The key to cooperative concurrency is the wisely chosen yield keyword in Python, which is two way, and a way of handing back control to the caller, voluntarily we might say, before all business is completed.  Queue up a number of such yielding tasks, as promising to deliver in the future, and roll through them, round robin or when the timer dings (ready!) and you've got yourself an event loop.

In a seeming change of subject, I had the C6XTY "buckyball" made of six units, screwed together with eight disks, as a "booth magnet" conversation piece.

Even after understanding our proposal, for a smart router that keeps students on task, schools approved by model families, a Pythonista maybe wanted to linger, chat on other topics.  Hexapents for everyone (HP4E) meets CP4E (Guido himself sauntered by, but chose neither to engage nor inhibit, per Pycon's code).

The connection is this concept of "payload" or "something valuable inside".  When a Python generator returns, raising a StopIteration, a payload might go inside at that point.  Likewise a Future, or class of Task, this this "cooking" or "baking" internal state, which the event loop keeps checking, not blocking for more than a moment if the task is clearly undone.

Once an egg "hatches" and releases the payload, then other design patterns kick in.  Cooked meals get delivered to tables. A waiter / waitress is optimizing in many ways too.

The chef or chefs may be amazing in their seeming ability to multi-task, but lets not forget:  the whole restaurant is made from coroutines.

Nor is such an ecosystem incompatible with the pre-emptive multitasking going on at a deeper level.  The OS knows the CPU is a resource to share.

There's nothing wrong with running "blocking code" or "being a CPU hog" when you've been scheduled for useful work, and when the OS retains the channel changer (the "remote").

That's how CERN and Hubble both work, with a jobs queue.  It's up to the researchers to manage a workflow once their fun in the sun comes around.