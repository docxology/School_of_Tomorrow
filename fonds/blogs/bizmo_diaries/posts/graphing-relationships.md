---
title: Graphing Relationships
id: 5203077814875949756
author: Kirby Urner
published: 2014-10-11T21:00:00.001-07:00
updated: 2014-11-29T21:59:41.857-08:00
blog: bizmo_diaries
tags: 
---

[](https://www.flickr.com/photos/kirbyurner/15511050085)

Those of you who've done most your bookkeeping or other record keeping with SQL, may have heard of NoSQL or "not only" SQL, but your mind flashes to something like Mongo or CouchDB, not to a graph database with a language like Cypher.  That's still forgivable as graph databases are still relatively new players in the record keeping ecosystem.

Neo4j depends on Java and gives you a web browser mashup that's a combination IDE / REPL and visualization portal.  For those of you not decoding:  IDE = interactive development environment; REPL = read / evaluate / print loop (interactive prompt); SQL = structured query language.  You'll see that above:  the $ is the interactive prompt and the box beneath, listing movie names, is what a MATCH query in the Cypher language came back with.

Getting some [basic / primitive Python API](https://twitter.com/neonige) might be a next step, or maybe not.  I should probably just work out in native Neo for a couple weeks and build up my Cypher skills.  The command language [front end](http://controlroom.blogspot.com/2014/09/djangocon-talk.html) would be like:  "Make Ahmed clerk of Peace and Social Concerns for two years starting in 2014".  The Cypher would happen behind the scenes.  Something like WikiWords might come in handy, to keep the parsing part easy.  If you prefer to write Cypher directly, more power to you.

Then a clerk could query using syntax like:  "show all previous members of Peace and Social Concerns with the percent of regular meetings they attended".  This might be a Nominating clerk query.  One wants reliable attenders usually, though some people have pre-agreements that could also be encoded e.g. members who live in another city half the year, the case with Carol.