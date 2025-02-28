---
title: Please Explain...
id: 382482332312839328
author: Kirby Urner
published: 2009-05-30T12:37:00.000-07:00
updated: 2014-11-29T20:34:50.957-08:00
blog: control_room
tags: 
---

Cursory readers get a lot of question marks going off as they read the computer stuff these days, as the technical writing has only gotten more technical, but that doesn't always mean less comprehensible.

Engineering is about making sense.

When you work on a web page, staging for purchase, that's private information until you hit a submit button, or should be.  Then a little suitcase gets stuffed full of data and sent through a portal, [watch Warriors of the Net](http://controlroom.blogspot.com/2006/07/back-to-work.html) if confused about how our truck fleet does business (a packet delivery service).

What goes with that suitcase, like an airline baggage tag, is a URL.  In a modern framework, that might be filtered, like through charcoal (no, I'm not drinking [Jack Daniels](http://worldgame.blogspot.com/2006/03/returning-to-pdx.html) at the moment), to a "view builder" (like in Django), which will fish in the database per instructions, then prepare the fish (perhaps smoking it), for sending back down the pipe, an HttpResponse object, another suitcase.

Yes, these are all metaphors.  We're talking bits and bytes, as usual, but something more colorful is more likely to stick, n'est pas?

"Preparing the fish" (or "dressing it") is what templating is all about (using a template language, lots of boilerplate HTML, CSS, scripting).  You should imagine yourself sharing this service with random anonymous others, all hoping for a responsive web service.

A web framework is a lot like short order cook, taking tickets on a big wheel, a public display of our queue (customers like the transparency, though once on the other side of the counter, it gets more parallel with the orders, plus who knows which staff are out sick or whatever -- thank you for your patience).

No, I haven't talked about SQL yet, nor MapReduce.  That's all about the "go fishing" instructions, which may get processed through an ORM.

An ORM is an Object Relational Mapper, takes the scattered data from "the bone yard" (related tables) and reconstitutes a real case history, a once living and breathing human being, leaving valuable clinical data to medical researchers.  An ORM is also a two-way street in mapping new patient data back to these registries.

That's one application of Postgres or Oracle or DB2 or any other reliable SQL engine you may have heard about and/or used.
[These engines](http://mybizmo.blogspot.com/2008/07/open-source-database.html) may not be considered especially sexy or glamorous to work on perhaps, but they're still important work horses of our way of life, on so many levels.

We should teach more about the SQL ecosystem in the high schools, with the MVC math that goes with it (also group theory, along with the J notion of "rank" or "dimension" -- a bridge to polytopes down the road).

I've got this "how it works" explanation storyboarded with more Monty Python like visuals ([castle, knights](http://worldgame.blogspot.com/2009/04/mapping-gnu-math.html)) in other chapters, with less focus on the suitcases and/or [TCP/IP](http://worldgame.blogspot.com/2008/09/responding-to-critics.html).

Also, I so far haven't explained how your hit against some server might unleash quite [the JavaScript controller](http://mybizmo.blogspot.com/2009/01/admiring-javascript.html) (like a puppet master, dominates the DOM), ready to take over client-side, we hope in a nice way.

If you've ever fought tooth and nail with your browser, and lost, chances are you were up against malware.  More dangerous yet is to download actual executables masquerading as "just in time" helpers, after delivering bad news (e.g. "you've been infected, download this now!").

[Spam and scam artists](http://worldgame.blogspot.com/2009/05/cyber-attack.html) know their psychology, so take care, study up on file permissions, learn how to scan for open ports and so forth.  We touched on some of this with [HPD](http://controlroom.blogspot.com/2009/04/pybiz.html) (a class we taught), hoping the schools would take notice.

Is it that too few CTOs have a mandate [to share their knowledge](http://controlroom.blogspot.com/2009/02/science-and-public-policy.html)?

As town-gown relations improve, so too will our level of security against all of these malicious cyber-threats.  The Internet is a fun place to play, but you need some real training.  Join us on the new digital math track maybe, in overlap with gym.

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMSDLhKm4vQvWtTFaIRAk6oDcbbumq1UaxxbBUp2owoYoFG1y2WZx1zPcbD-BZp6OcSLz3Ij_N8b9klpAYSGdc_eZnzzahgYkNPCm5yPzv8B-8wu2pKIrIO5lRqKHG0mNltnPq/s1600-h/00013.jpg)