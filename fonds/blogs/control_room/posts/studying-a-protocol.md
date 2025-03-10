---
title: Studying a Protocol
id: 248435871197562018
author: Kirby Urner
published: 2017-12-04T12:16:00.002-08:00
updated: 2017-12-04T12:53:37.228-08:00
blog: control_room
tags: 
---

I'm holed up nursing my knee, treating [my condition](http://worldgame.blogspot.com/2017/12/coco-movie-review.html) more as a sports injury than a sign of encroaching old age. Nothing swollen, just inner joint pain, tender to touch, not stopping me from walking or stairs. I've worked out some physical therapy maneuvers, a kind of dancing, using Galaxy Tablet to pipe in a mix of Goa trance +  [Azan](https://en.wikipedia.org/wiki/Azan), my new fave.

[On Q2](http://www.quakerquaker.org/), a discussion list, I've been making some inroads regarding Sufi-infused Synergetics, a new "metaphysical tea" flavor, not unlike those at Salt 'n Straw, an important Portland institution that pioneers new flavors of ice cream, like Pear Blue Cheese.  Some of them taste better than they sound, you might be surprised.  I was there last night, with my friend Matt and his lady friend.

What protocol?  [RPC](https://en.wikipedia.org/wiki/Remote_procedure_call) it's called, older than [HTTP](http://controlroom.blogspot.com/2016/08/addendum-regarding-ssl-tls.html), but able to use same as a blanket i.e. you may wrap up a remote procedure call inside a request and have the server recognize this is not the usual POST & GET API, meaning we've moved outside the standard web protocol (hypertext transfer) to tap something older.

Flask, the micro-web framework, optionally comes with [RPC extensions](http://json-rpc.readthedocs.io/en/latest/flask_integration.html) and I've got [my Pythonanywhere site](http://thekirbster.pythonanywhere.com/) responsive, both in testing and production, though not doing anything very fancy as yet.

In the case of that particular application, I think redundantly pairing remote procedure calls with the pre-existing calls to return JSON, makes plenty of sense, e.g. you'll be able to get a few details on a chemical element or Geek Glossary term.