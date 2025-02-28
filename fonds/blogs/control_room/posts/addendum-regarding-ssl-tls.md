---
title: Addendum Regarding SSL / TLS
id: 1807156575403188079
author: Kirby Urner
published: 2016-08-19T09:36:00.003-07:00
updated: 2016-08-25T00:40:56.177-07:00
blog: control_room
tags: 
---

I enjoyed this talk by Cristina Formaini at Cal Poly. Good entry point into cyber-security. [https://t.co/qPDAeQNUaO](https://t.co/qPDAeQNUaO) [#CodeCastle](https://twitter.com/hashtag/CodeCastle?src=hash)
— Kirby Urner (@4DsolutionsPDX) [August 19, 2016](https://twitter.com/4DsolutionsPDX/status/766456982475722752)

My previous post in this blog is about a world readable tiny web application I'm using for work, to teach the basics of web dev in Python.

The specific micro-framework solution I'm using is named Flask, [a free and open source project](http://flask.pocoo.org/), BSD licensed.

How long I'll keep my teaching demo going in it's present form I don't know; that's a business decision depending on more businesses than mine.  For example, I'm using the PythonAnywhere service as my host.

Flask is a WSGI application, which is like the DB API for talking to SQL databases, except in this case to web servers.

The Flask application is imported and renamed from "app" to "application" in the auto-generated script below, which also provides a path to my codebase, here added to sys.path if need be:

[](https://www.flickr.com/photos/kirbyurner/28468063434/in/dateposted-public/)

Anyway, notice I'm using HTTP and not HTTPS when serving from [my PythonAnywhere account.](http://thekirbster.pythonanywhere.com/)

The added "S" is for "secure" and the difference will likely be signified graphically with a little picture, an icon, of a say a padlock, next to the URL (web page address) in question.

The "secure icon" appears once handshaking has established a mutual understanding about what encryption algorithm to use, a multi-step process carried out automatically between the client and server.

Otherwise, if plain old HTTP is used, the browser may show an "I" for "FYI" and that well tell you "not secure" i.e. not using HTTPS.

Different browsers have different ways of graphically signifying whether or not encryption is being used.

Talking over the wire in HTTP or HTTPS does not actually require a "browser" on the client end, as many web API calls are possibly coming from simple scripts.

My API models talking with both types of clients, in JSON to the latter, in HTML to the former.

My goal in the forty hours (or less in some cases) is more to establish a strong reading knowledge of Python in particular, and this Flask app marks our foray into that territory.

In my discussion of the application, I'd likely take this opportunity to dive back into encryption as again relevant to our "API economy".

I say "again relevant" because more than likely we'll have already waded through the code of something more like my "Permutation class".

[My Permutation class](https://github.com/4dsolutions/Python5/blob/master/px_class.py) is Python class designed to show off operator overloading capabilities while introducing the Group Theory notion of a "permutation", a "scramble" of objects mapped to themselves in some different order.  I used a Python dictionary wrapped in a class.

"A 'scramble' of objects" sounds like encryption already, right? :-D  [Or shuffling a deck of cards](http://wikieducator.org/Casino_Math).

If the purpose of a website is simply to sit there like a book on the shelf in a public library, pretty much put there for the purposes of public inspection, then I'm not concerned if it's using HTTP and not HTTPS.

What's more important than "which protocol" is that we keep in mind that there's a difference.  Driving the unencrypted APIs into an underground API economy would be ironic, no? 

On the other hand, in a presentation taking us more deeply into web dev in particular, less focused on generic Python, one might dive more deeply into the specifics of TLS, as Cristina Formaini does in the linked presentation above, in my "tweet".

My focus in sharing Python in forty hours is somewhat like [Amit Saha's](https://youtu.be/XJOt4QQgx0A) in that my audience might be high school math teachers seeking to integrate more coding skills into their chosen field.

Amit is demonstrating what our Python subculture in particular has to offer the high school / college math teachers. [https://t.co/LTnSwjcXE0](https://t.co/LTnSwjcXE0)
— Kirby Urner (@4DsolutionsPDX) [August 19, 2016](https://twitter.com/4DsolutionsPDX/status/766676729263824896)