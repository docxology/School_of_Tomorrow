---
title: A Pseudonymizer
id: 5152878577108758392
author: Kirby Urner
published: 2008-07-07T20:07:00.000-07:00
updated: 2008-07-07T20:28:57.305-07:00
blog: bizmo_diaries
tags: 
---

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhEC1ePtLN3MYmARVdpbJ8qv15xxH5LaD_9bGVH1AX1B6x4Mhti-IA3_aJEZNvanUJNO0IjgToUBtmGpQTIXi6G2KEwZ6Rcp-GCVpE0hOivZsx-JxXZ6V-emPplGnf8OKv8V5D/s1600-h/amtrak_centralia.jpg)Since I was through Centralia today, I got to thinking of last year's [BarCamp](http://barcamp.org/) (alpha version) twixt medical and geek participants (very prototypical, no press releases).When working for a local clinic through [Free Geek](http://www.freegeek.org/), our very security conscious staff wanted to obey HIPAA to the letter, meaning no confidential patient info should leak off premises.On the other hand, we needed realistic test data with which to develop our application (an upgrade of [SQL Clinic](http://www.sqlclinic.net/), migrating it to more object-oriented Perl, [Naked Ape](http://nakedape.cc/) the lead contractor).Likewise, doctors need to swap case histories in vast numbers, but without compromising patient anonymity.Enter the pseudonymizer: a program able to synthesize fake identities on a massive scale, in order to give thousands of cases legitimate cover within microseconds.The case info remains intact, as statisticians need to know actual age, sex, body weight, risk factors and so on.  But if someone left a laptop on the train, with all this valuable outcomes research info, it'd be untraceable to real individuals.I've looked through some literature and see modest use of this term "pseudonymizer" for roughly similar purposes, although not with reference to [HIPAA](http://worldgame.blogspot.com/2004/09/usa-os.html) in particular.