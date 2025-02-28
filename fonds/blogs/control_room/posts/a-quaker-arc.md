---
title: A Quaker Arc
id: 5837194597006245641
author: Kirby Urner
published: 2014-10-07T18:07:00.002-07:00
updated: 2024-02-18T05:03:02.041-08:00
blog: control_room
tags: 
---

[](https://www.flickr.com/photos/kirbyurner/15450822716)

Speaking of [Carl Jung's Red Book](http://controlroom.blogspot.com/2014/10/red-book-not-maos.html), I will be suggesting in my Quakernomics talk tonight that branches of [Gnosticism](http://worldgame.blogspot.com/2014/02/valentines-day.html) may have re-awakened within [specific branches](http://controlroom.blogspot.com/2013/10/quakers-in-business.html) of Quakerism, but then I'm using a larger backdrop wherein Quakers, whatever their diverse makeup, had almost peaked around the time Philadelphia was Quakerdom's new capital (well before 1776 in other words).

So it's a bell-shaped curve rising up towards the "total capitalism" phase, when Quakers gave birth to the industrial revolution, and by extension the UK itself, with Friends then starting to experience diminishing power "[until 1756](http://worldgame.blogspot.com/2009/09/catholic-analysis.html), when they refused to vote a tax for war against the Shawnee and Delaware Indians".

Their refusal to [fight the "Indians"](http://mybizmo.blogspot.com/2008/07/some-quaker-pr.html) was somewhat the final straw.  Then their refusal to support slavery was just beyond the pale.

Many a Quaker family fled westward in the build-up to the Civil War, finding themselves unwelcome guests, viewed as outright terrorists, or as disruptive at best, in the pro-slavery South.

However, in the UK, slavery was a less "in your face" phenomenon, and Quakers continued to climb the social ladder with their crowning achievement being this Iron Bridge which opened in 1781.

So let's use 1781 to mark the apogee of Quaker power in Universe so far, with a long sunset phase carrying us through the North American dark ages and near extinction within the derivative Pastoral forms.

I wrote a little program to draw timelines in ASCII, with a few examples:

timelines = {
"Oliver Cromwell":(1599,1658),
"George Fox":(1624,1691),
"Henry VIII":(1491,1547),
"Rene Descartes":(1596,1650),
"Margaret Fell":(1614,1702),
"Mary Dyer":(1611,1660),
"Queen Elizabeth":(1533,1603),
"Ben Franklin":(1706,1790)}

def make_line(person, start = 1490, end = 1800):
    line = (end - start) * ["."]
    born = person[1][0] - start
    died = person[1][1] - start
    line[born:died]= ["@"] * (died - born)
    return "{:>40} {}".format(person, "".join(line))

for person in timelines.items():
    print(make_line(person))

The British Empire peaks when Quakers have already started to wane, not surprisingly as imperialism is incompatible with egalitarianism.

The US empire -- more a flash in the pan by comparison -- takes place against the backdrop of the [New World Order](http://mybizmo.blogspot.com/2011/01/states-in-flux.html) or whatever we wish to call the [Future Unknown](http://worldgame.blogspot.com/2014/10/the-unknown-known-movie-review.html).

Historians and some economists may seize on [Quakernomics](https://controlroom.blogspot.com/2022/04/base-housing.html) as a useful meme. We shall see.

As I posted on Facebook recently: 

 Our Multnomah Meeting spawned a Quaker Economics Group under Joe Havens for awhile, huge
 interest and attendance, but no one thought to coin "Quakernomics" as 
anything special at least that I can recall.  So hats off to these PR 
gurus and their new branch of economics.  May they live long and prosper
 (Spock sign).