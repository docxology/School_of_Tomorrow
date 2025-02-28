---
title: Dissecting a Flask App
id: 2018206485441280327
author: Kirby Urner
published: 2016-08-17T08:04:00.001-07:00
updated: 2020-10-30T09:26:11.521-07:00
blog: control_room
tags: 
---

[](https://www.flickr.com/photos/kirbyurner/28429351143/in/dateposted-public/)

"How might I share content to the world through some web thing?"

I'll show you how we might do that in Python.

[http://thekirbster.pythonanywhere.com](http://thekirbster.pythonanywhere.com/) is where I'm serving my example.

The source code is [on Github](https://github.com/4dsolutions/tiny_flask).  Also:  [see Addendum](http://controlroom.blogspot.com/2016/08/addendum-regarding-ssl-tls.html) (followup blog post).

The engine sitting behind the [HTTP listening port](http://controlroom.blogspot.com/2006/06/tcpip-for-gnubees.html) is [a WSGI process](https://www.python.org/dev/peps/pep-3333/) named Flask, which is an already [completed project](http://flask.pocoo.org/) that just needs to be hacked on (customized). 

[flask_app.py](https://github.com/4dsolutions/tiny_flask/blob/master/flask_app.py), the custom Flask process (written in pure Python), routes (dispatches) incoming web requests (web addresses, URLs) to Python functions. 

Each function develops an appropriate response, either as HTML (styled for human browsers) or JSON (bare bones data, more for machine readers).  We call this [a web API](http://controlroom.blogspot.com/2016/08/api-economy.html).

HTML or "hypertext markup language" is what your web browser is designed to render into web pages, possibly interactive [thanks to JavaScript](http://worldgame.blogspot.com/2016/04/musings-on-javascript.html), if you have your JavaScript engine turned on.

[JavaScript](http://www.w3schools.com/js/default.asp) is also known as ES (ECMAScript) and is not the same as Java.

Python also talks to [SQLite databases](https://www.sqlite.org/) on the server, to look up and serve the requested information. The application also handles [POST requests](https://github.com/4dsolutions/tiny_flask/blob/master/flask_client.py), with a simple hard-coded string for authentication.

Add chemical elements to the Periodic Table database (Elements table) or new terms to the Glossary database (Glossary table).  No delete or update features have been implemented, as a goal is to keep the application's anatomy fairly simple.

I'm using Python "[context managers](https://github.com/4dsolutions/tiny_flask/blob/master/connectors2.py)" to open and close the database files, as needed.

https://t.co/wJvZi52csj-- a tiny Flask application I'm using to teach code school #CodeCastle
— Kirby Urner (@4DsolutionsPDX) [August 17, 2016](https://twitter.com/4DsolutionsPDX/status/766059704229310464?ref_src=twsrc%5Etfw) 

[In my forty hour Python course](https://mail.python.org/pipermail/edu-sig/2016-August/011514.html), I take you through building a context manager [using contextlib](https://docs.python.org/3.5/library/contextlib.html), from the "batteries included" Standard Library.

[Forty hours](https://www.flickr.com/photos/kirbyurner/albums/72157660337424600) is about right to develop a strong reading knowledge of Python, which in turn provides enough traction to keep improving your own code through practice. 

SQLite is also included in the Standard Library, [as sqlite3](https://docs.python.org/3.5/library/sqlite3.html).

The HTML is developed through a Flask component named [Jinja2](http://jinja.pocoo.org/), which allows Python to pass content from the database into a web page that's being built.

Jinja2 uses templates as raw material, very [like HTML files](https://github.com/4dsolutions/tiny_flask/blob/master/templates/elem_page.html), which in turn link to Cascading Style Sheets ([CSS files](http://www.w3schools.com/css/css_howto.asp)) and any JavaScript (.js files) we might need.

The well-known [Django framework](https://flic.kr/p/DH1PWi), also in Python, is quite similar to Flask in structure, and also includes a templating engine.  [Web2py](http://www.web2py.com/) is another one.

A standard development process for writing these things is to have your localhost serve a developer version, the one you hack on, then practice (A) keeping the Github version up to date and (B) maintaining a world readable cloud instance.

We also do a lot [with Jupyter Notebooks](http://nbviewer.jupyter.org/github/4dsolutions/Python5/blob/master/Atoms%20in%20Python.ipynb) during the forty hours (or less if the course is [accelerated](http://worldgame.blogspot.com/2016/08/accelerated-learning.html)). 

[](https://www.flickr.com/photos/kirbyurner/25090677786/in/album-72157660337424600/)