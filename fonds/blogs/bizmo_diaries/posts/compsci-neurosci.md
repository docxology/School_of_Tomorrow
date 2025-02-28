---
title: CompSci + NeuroSci
id: 6065732207951206213
author: Kirby Urner
published: 2016-10-16T09:19:00.002-07:00
updated: 2016-10-16T12:52:16.547-07:00
blog: bizmo_diaries
tags: 
---

[](https://www.flickr.com/photos/kirbyurner/30249061422/in/dateposted-public/)

[ originally an email to [Nathaniel Bobbitt](http://mybizmo.blogspot.com/2006/08/adventures-in-toontown.html), Oct 15, 2016 ]

I wonder how annoying it'll be to neuro-science types to hear me teaching compsci and saying such things as "the browser's brain is full of JavaScript whereas the server is thinking in Python."

Of course web browsers don't have "brains" and many [philosophically-minded](http://controlroom.blogspot.com/2016/10/wittgenstein-again.html) would take issue with servers doing any real "thinking" let alone in Python.

I'm not worried about it though.  Language is nothing if not malleable and I'm purposeful in having students empathize with their machines as if these latter were sentient beings. 

Why?  

Not to encourage superstition but to bring an already richly associational matrix of key terms, a well developed namespace, into a relatively alien territory (that of machine learning -- and they need to be taught, by us).

Knowledge has always expanded thusly, i.e. empathy has always played a big role, at least for some people.

The Python language actually uses the word 'self' although it's not a keyword, more a placeholder with a conventional spelling, ditto "God" (not in Python) and like that -- kind of like how "Zero" doesn't really have to be "0" but we do need that placeholder.

When I define a type of thing, such as Airport:

class Airport:

    def __init__(self, three_letter_code):  # birth!

        self.code = three_letter_code

    def __repr__(self):

        return "Airport('{}')".format(self.code)

Interactively then: 

In [148]: portland_or = Airport("PDX")
In [149]: portland_or

Out[149]: Airport('PDX')

I then spawn many "selves" of same, e.g. 

portland_or = Airport("PDX")newark_nj = Airport("EWR") 

and so on, elaborating into a full program.

A standard practice in compsci, when passing the "object oriented" torch, is to talk about "is a" and "has a" relationships e.g. a car "is a" motorized vehicle, and "has" seats for people (maybe the driverless ones don't). 

I've long encouraged a parallel "am a" and "have a" grammar, such that the programmer thinks "I am an Airport, now what do I have?" "I have concourses, and luggage carousels". "OK so now I'm a concourse, what do I have?" and so on.

Changing the subject for a sec, a question I was gonna ask you at Atlas (or Bagdad or...) has to do with "autistic spectrum" -- how people talk, yes?  But doesn't a "spectrum" connote basically two directions: left vs right, up vs down, in vs out (any of those)?

Probably [some author](https://arxiv.org/pdf/1305.2537.pdf) has already suggested a multi-axis (i.e. higher dimensional -- more than one) "phase space" for placing autistic profiles in a taxonomic or diagnostic matrix. "Beware of spectra when phase spaces are better" might be the moral here -- degrees of freedom and all that.