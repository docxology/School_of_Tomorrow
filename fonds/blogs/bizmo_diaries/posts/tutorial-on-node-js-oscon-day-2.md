---
title: Tutorial on Node.js (OSCON Day 2)
id: 7898553978200268255
author: Kirby Urner
published: 2014-07-21T16:00:00.000-07:00
updated: 2014-07-21T16:27:32.682-07:00
blog: bizmo_diaries
tags: 
---

Notes on: [Node.js Three Ways](http://www.oscon.com/oscon2014/public/schedule/topic/Emerging%20Languages) by C. Aaron Cois and 

  Tim Palk 

I played hooky in skipping the Python tutorial on meta-programming, which looked interesting.  I hope Patrick will update me.   The presenter for that one was from Brazil.

Instead I'm planning to study Node.js, also work-related in that a revamp of the company guts is expected in this technology.

The tutorial covered the same territory as a Python Django workshop in giving us hands-on use of an MVC (model view controller) web framework.  The Express architecture is remarkably similar to Django in fact:  a standard HTTP request-response pipeline with routing to templates, a modeler for mapping the database and so on.  Meteor, presented in Act 3 is somewhat different.

Important:  we're not talking about client software in a browser.  Django and Express (the node.js framework we're looking at) run on the server, not the client.  One of the breakthroughs for the JavaScript community has been its moving to the server.  We're using [Redis](http://redis.io/) for our localhost webserver.

The idea of a project with an app.js and a packa[](https://www.blogger.com/)ge.json to guide npm (node package manager) in what dependencies to install.

The presenters have an ambitious workout planned wherein workers contend for a lock and talk to reddis, then later, mongodb.  I've installed a lot of open source software in two days at OSCON.

Matthew and Debra of O'Reilly School found me at the i18n table at lunch.  We mapped out some strategy for tomorrow, when we harvest video clips for later promos.

Tonight, the Expo Hall opens and I'll find out where our booth is.  Then:  the big festival / party, always themed.  OSCON is a well-oiled machine in many ways, a working formula.  Why fix what ain't broke?

I got lost in this tutorial thanks to [this minor issue](https://github.com/garann/node-for-frontend-devs/issues/2) involving curl and npm.  However the presenters gave us the means to pick up anywhere by providing snap shots of the projects, with all source code in place.  Useful.  This is the kind of material I go back and study later, with my computer prepped as a learning platform.

Socket.io is an interesting utility.  No need to stick to port 80 and HTTP.  That's for letting servers push to clients, such as updating chat windows with other users' strings.  Meteor is a "reactive framework" for such an environment.  Clients update each other in real time, like in a multi-user game.