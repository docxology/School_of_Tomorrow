---
title: DS US
id: 4727808501521005042
author: Kirby Urner
published: 2024-10-15T21:48:00.000-07:00
updated: 2024-10-16T04:02:26.722-07:00
blog: bizmo_diaries
tags: 
---

[](https://www.flickr.com/photos/kirbyurner/54045808780/in/album-72177720296706479)

US track, Data Science

Tonight I was engaged in torch passing. No, not PyTorch (you know of it?) but moving in that direction. I told my students they were on like the Trans-Siberian railroad, from London to Beijing. I would be their tour guide from London to Berlin. Then I’d hand them off to a next instructor. They’re wending their way towards ML (Machine Learning) the domain of PyTorch, although from the slides I see it’s TensorFlow they get into, which makes sense too. Keras…

The part of the ML pipeline I have them look at is analogous to what I did in outcomes research, when David Lansky and company (MDRC to be precise) were harvesting data from heart procedures, diagnostic and interventional, and getting it statistically analyzed. David and Gary knew statistics. I was the computer guy who knew how to harvest on the front end, design a GUI for data entry and cleaning, while feeding a growing repository on the backend, what would, over time, become Big Data — provided PATS could handle the load.

Harvesting, merging and cleaning data: that was my bread and butter in that this hospital system became my biggest client. That I wasn’t an employee was to their advantage but also put limits on how long this particular configuration could last. Microsoft would end up pulling the plug on Visual FoxPro in 2015. Bigger players would be moving in, replacing my applications. We managed to launch a few careers. Outcomes research took off.

Merging is often overlooked but that’s where pandas in a Jupyter Notebook may prove its metal, pure gold for some company. Do you know about pandas? That’s like Excel in terms of providing tabular frameworks. Tabular data has to be as old as data gets. Rows and columns. Arrays. In the Python world, we have a stack for that, a suite of 3rd party packages. Download and import and you’re in business.

I’d get data from here and there (scannable forms played a role — forms I got to design) and it all needed to get neatly shuffled and interpolated, and placed in relational tables. You only want a specific patient detailed once, but then with multiple episodes, admits and discharges, with procedures in between. That’s one to many. 

Every patient has their own arteries (one to many), but they each have the same coronary suite, so many to one. Which of these arteries have become occluded if any? What cath and what stent were used, or was this a graft, a bypass? 

I had CLAIR for the cath labs and CORIS for the ORs. The doctor practice supporting my efforts, in addition to the hospital system itself, thought my applications were prototypical enough to be worth sharing with bigger companies. "See this stuff Kirby is doing? That's what we need. Why not learn something?" They learned, to a degree anyway. I was in a position to assess.

But I wasn’t using pandas or Jupyter Notebooks or any of that stuff back then. We were a Microsoft shop and I was using FoxPro for the intermediary holding tanks and the GUI. 

I’d learned to parse through cath lab text files coming from time-stamped chronologs made by Quintons, the cath lab machines, where techs chronicled all the details of a procedure. Patient goes under, doctor arrives… procedure over, another success (the success rate was high). Parse the logs, populate tables, let a data pro audit and revise.

Another workflow that gets overlooked, in addition to merging, is anonymizing. Creating these amazing data sets is only allowed if there’s HIPAA compliance. 

We were eager to amass heart procedure and long term outcomes data and to pool it with other hospitals, but not in such a way as to violate confidentiality in medical record keeping. 

My institution (a client) was pretty meticulous along those lines and a big part of my job was to help my coworkers keep all the sensitive identifying fields behind a security wall within the hospital. We suffered no data breaches on my watch, that I know of.

I make it sound like I was doing all this by myself, however the final repository of all this data was PATS, owned by a different company. Once the data my systems harvested was merged and cleaned through my FoxPro GUIs, it got batch imported into PATS, by people trained in that work especially, along with their other tasks.

As I was telling students tonight over Zoom, I had a long career before Python popped up on my radar and even then, it wasn’t as a replacement for the FoxPro applications development toolset. All seems more clear with hindsight.

What drew me to Python was computer graphics and my curriculum development work, more an outgrowth of the McGraw-Hill chapter, which had come before my moving back to Portland and diving in with the FoxPro. 

Graphics and animation. VPython. Hypertoons. 

But then I could backfill by leveraging the data science work just described, and become a guru of data pipelining the way that’s taught now. FoxPro was very SQL-savvy. Learning the Python DB API was not that big a deal. I could use SQL for my Polyhedrons.