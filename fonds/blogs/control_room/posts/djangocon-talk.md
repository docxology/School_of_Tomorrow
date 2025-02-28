---
title: DjangoCon Talk
id: 2766003834091773787
author: Kirby Urner
published: 2014-09-04T15:08:00.002-07:00
updated: 2014-09-05T19:33:08.660-07:00
blog: control_room
tags: 
---

I'm in a talk being presented by a team from National Geographic.  Justin Quick, Ben Fonarov and Farhan Syed are the speakers.

Django is a part of their website ecosystem.  Their talk is based on their Django module [activitysteams](https://github.com/natgeo/activitystreams) on Github, the open source repository.

An Activity Stream is like a series of comments, likes, or game actions on a target.

A semantics like "You favorited a photo" pertains, with an "actor / verb / target" grammar.

What's exciting to me is the Neo4j graph database being used by the Horizon service.

Horizon is their Node.js web socket service that takes snippets (like "likes") and stores them using Neo4j.

I've been thinking of [a Quaker meeting management API](http://worldgame.blogspot.com/2014/09/djangocon-2014.html) based on activity streams, not realizing what wheels might not need reinventing.

"Make [actor] [position] vis-a-vis [committee] for [term]" would be the kind of semantics we need.  Example:  "Make Joe Shmoe clerk of Oversight for three years starting June, 2015."

Also:  "Show [actor] and [actor] are married under the care of [meeting] as of [date]." As I've pointed out on math-teach, said marriage might or might not be recognized by the state in which the meeting is situated (Quakers define marriage their own way, independently of their surroundings sometimes).

The team made the good point that browsers prefer interactivity to read-only web pages.  Given how I generally have comments turned off in these blogs, I'm going against the grain on that score.  These are on-line journals more than conventional blogs.

However, it's fairly easy to post a link to a blog post and frame it for comments elsewhere, such as on Facebook.