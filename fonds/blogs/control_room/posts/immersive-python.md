---
title: Immersive Python
id: 427182406790223458
author: Kirby Urner
published: 2010-04-22T14:24:00.000-07:00
updated: 2010-07-31T18:01:48.615-07:00
blog: control_room
tags: 
---

[We blitzed through a lot of Python](http://mybizmo.blogspot.com/2010/04/hb2h-hb2m.html) in three days. I knew STScI was deeply into NumPy but didn't really get it about Pyfits [until I got here](http://worldgame.blogspot.com/2010/04/python-gig.html). FITS is a file format used by astronomers around the world. These files contain a lot of the imagery from Hubble, which dumps data to New Mexico, from whence it bounces off another satellite to the Goddard Space Center, thence it feeds into STScI here in Baltimore for archiving and analysis.Various data processing pipelines then take the data through transformations to enhance the information and accommodate for idiosyncrasies, anomalies, other factors. The delicate instruments are in perpetual need of fine tuning and recalibration.Clients will often get both the raw data heading into the pipeline, as well as the processed results coming out the far end.The Hubble is always repointing this way and that as it circles Earth every 96 minutes. It uses gyroscopes to do this, not retro rockets. Astronomers compete for precious time on this always busy, tightly scheduled space telescope.