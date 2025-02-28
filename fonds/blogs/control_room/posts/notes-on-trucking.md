---
title: Notes on Trucking
id: 6682752228411088907
author: Kirby Urner
published: 2010-08-27T17:22:00.000-07:00
updated: 2015-10-12T11:49:52.989-07:00
blog: control_room
tags: 
---

I've often exulted how knowing something about computers gains one entre to any number of disciplines, given they all have a need for computer services.  Case in point:  I've worked in transportation, summer camp registration, even in the cardiac operating room (after hours) testing my heart operations data collection application ([CORIS](http://worldgame.blogspot.com/2007/05/more-basement-archeology.html)).

These days, I'm learning more about trucking.  Transportation Management Systems will help dispatchers organize shipments and hand them off to trucking companies.  LTL stands for Less Than Load, meaning only part of the truck gets filled.  Does one book a direct LTL delivery, a multi-stop, pass on to a pool?  The experienced dispatcher needs a head full of geography and lots of experience.  But what if that level of experience is unobtainable?  Enter software assistants, the equivalent of part- and/or full-time employees.

Microsoft's Visual FoxPro (VFP) was a highly capable product but has [fallen on hard times](http://mybizmo.blogspot.com/2010/08/lurching-ahead.html).  VFP coders are being herded into .NET solutions, but feel their productivity dropping off.  Although not a TMS, [the trucking software I'm looking at](http://www.flickr.com/photos/17157315@N00/4940402278/) is in VFP and the question is how to migrate it to something else eventually.  The program is already running live, in production, with paying clients, so the mentality is one of gradually swapping in Python components, swapping out VFP components.

The hybrid (VFP + Python) might look pretty convoluted though.  Imagine FoxPro accessing its own native tables through a Python COM server that in turn uses ODBC for its back end.  Could this be ungainly?  Will I be swallowed up in the trucking world and Earthling Math?