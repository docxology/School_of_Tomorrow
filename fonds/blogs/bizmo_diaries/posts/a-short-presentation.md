---
title: A Short Presentation
id: 748935678641687324
author: Kirby Urner
published: 2016-09-06T08:40:00.000-07:00
updated: 2016-09-06T10:55:42.594-07:00
blog: bizmo_diaries
tags: 
---

[](https://www.flickr.com/photos/kirbyurner/26381319235/in/album-72157664766721643/)

A student I met in Afghanistan (I was in Portland, we were working together over the Internet), showed up in a "bizmo" of sorts -- if you think para-gliding has a business angle (to me it does) -- and chauffeured me to the code school.  "Bizmo" means "business mobile" in contrast to the "RV" or "recreational vehicle". Will's bizmo is right hand drive, a Mitsubishi built for Japan's roads.

I was the guest host this Labor Day, as the enterprise was otherwise closed and paid staff were catching up on gardening and such. I'd signed up to talk about [my tiny Flask application](http://controlroom.blogspot.com/2016/08/dissecting-flask-app.html), and to introduce the idea of Lightning Talks, which go for no more than five minutes.  My talk was not billed as a lightning talk, however we're encouraging more presentations at Flying Circus and foresee when that might be the best choice of format.  Geeks need opportunities to practice the skill of presenting in five or less minutes.

I probably talked for closer to ten minutes, presenting to an audience where many had deep experience with Angular, React (frameworks), JavaScript, Java and Python (languages).  Ben is writing embedded C these days.

My talk inspired a next geek to jump up and share his [Anagram Finder](http://anagram-finder-app.herokuapp.com/static/index.html), a Flask app deployed in Heroku, likewise open source.  In looking over his routing module, I could see right away where I might want to make some changes to mine.  On the other hand, I'm aiming to stay pretty close to "just out of the box" i.e. Flask with few frills.  I'm glad my talk led to a follow-on talk.

As I was getting things set up, plugging in the HDTV etc., I got a call from David Feinstein, whom I've been thinking about lately, and a film festival invite from a Palestinian-American I know. The ride from Will had also been unexpected (my original plan was to use the bus, holiday schedule).  In other words, events conspired.  I almost succeeded in roping Patrick into the event (he and another consultant were hoofing it to the zoo for exercise).

Speaking of exercise, it's the morning after, wet but not at the moment raining.  Mt. Tabor beckons.

I'll just mention what my Flask application actually does:  it simply connects an API of URLs to GET and POST request handlers, against three databases:  a Periodic Table, a Glossary of Geek Terms, and a Shapes listing (polyhedrons). These are simple SQLlite tables, not even relational in the current version, though the Shapes table has gone deeper, down to specific vertex coordinates, in related projects. [/glossary/AJAX](http://thekirbster.pythonanywhere.com/glossary/AJAX) pulls up a definition in HTML (not that I'm using any AJAX) whereas [/api/glossary?term=AJAX](http://thekirbster.pythonanywhere.com/api/glossary?term=AJAX) would pull up the same fill-in-the-template info in pure JSON.

When you look at the raw JSON info behind the more cosmetically enhanced view (the HTML), you'll see two additional fields I don't share through the template:  some initials and a large (multi-digit) decimal integer.  This models keeping track of whom and when a record was created.  The integer is actually the number of seconds since the start of the "unix epoch" on January 1, 1970.

[](https://www.flickr.com/photos/kirbyurner/28870884923/in/dateposted-public/)

I'm giving a talk on a small Flask application at [@PDXCodeGuild](https://twitter.com/PDXCodeGuild) this evening. [https://t.co/wJvZi52csj](https://t.co/wJvZi52csj) [#Flask](https://twitter.com/hashtag/Flask?src=hash) [#Python](https://twitter.com/hashtag/Python?src=hash) [https://t.co/PGuViNgoWQ](https://t.co/PGuViNgoWQ)
— Kirby Urner (@4DsolutionsPDX) [September 5, 2016](https://twitter.com/4DsolutionsPDX/status/772906166288461824)