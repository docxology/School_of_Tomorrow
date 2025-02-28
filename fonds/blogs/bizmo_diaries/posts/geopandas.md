---
title: Geopandas
id: 3454363275380619204
author: Kirby Urner
published: 2018-05-26T22:13:00.001-07:00
updated: 2018-05-31T13:13:33.573-07:00
blog: bizmo_diaries
tags: 
---

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj3lV_Rf2E0BCKLtWj6J1ei2pE1DuBH8bXIbusxXFer5OByxTmrSqS9vSzZPegMKBmJ0crztnOiLl5Viz-46MMAqKGeK8UZhuH1BTD9_SEPcfixM1V_Nr8NbPUD41RtZUvolSk1/s1600/geopandas_success.tiff)

:: success! ::

I discovered the hard way today that blithely installing [geopandas](http://geopandas.readthedocs.io/en/latest/) from the conda-forge repo, atop a default repo version, is not a tastey recipe. I had to toss my original default Anaconda out the window and do a clean install, good exercise, but not how I'd anticipated events flowing.

Following best practice, I'm now installing a geopandas in its own environment.  But do I have the repo issue sorted out?  After this fresh install from the Anaconda website, I went [Warning:  don't do this, read on!]:

$ conda create --name geopandas python=3.6 geopandas

leaving it entirely up to conda to decide which repo I meant.  Even I don't know, but there's Fiona and all the rest, so I know I'm getting some gigabytes.

Upgrading the Anaconda navigator (in process) will give it a chance to see the new environment I just created.  Will geopandas import successfully this time, or crap out in Fiona?  That is the question.

We're going from Anaconda 1.7.0 to 1.8.5 -- OK, done, lets see if we have a new environment, yes I do, and I don't even have Spyder 3.2.8 yet, in the new one.  I'll go out to the command line, activate the new environment, boot python, and see if the import works, take a screenshot...

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2SrBE1JhMpLE2gzF_A3iu2OUnPXbeJeMsPTOfKd59tdT9cvfPNvvRdkK7SOp5VCHX0giBLR0CffukgkPOcUsv75ahAX8PX6s1zyn8vIUJ2KSI1z20fGntBtIJ0YIKKKXVJMcc/s1600/conda_activate_oops.tiff)
Not so fast, say the conda gods. I still have PATH issues.  Fight, fight, fight!  "Fighting Quakers" is a meme, cite Earlham College, also Franklin High School here in Portland, just blocks away.

[](https://www.flickr.com/photos/kirbyurner/27153082297/in/photolist-HnqDnk-F7Udph-pxkvi7-axj4op/)

However Franklin High School recently [dropped the Fighting Quaker mascot](http://www.sacbee.com/news/nation-world/national/article211108734.html) recently using the rationale of not wanting to offend Friends.

Friends I know were forgiving as it's true Ben Franklin never overtly tied himself through membership to any Meeting, that we're able to find the record of.

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhoQm7feCJrl-wxNKihZkNacxD27nUk28VtiYR-0VHkROLoa7Bcad4XRwUnM5TJfOsT1kyRqTVEk-wyJTfbewILmwsdTcis8UryBP6fuKttwJ6i3dGjg-3GBPgArTY8ohma_Owh/s1600/geopandas_waste_of_time_2018.jpg)

So no, even with a clean environment, without a force to conda-forge as the repo, don't expect a working geopandas.  Fortunately, there's a one liner to wipe an Environment.  I'll do that, after some coffee (looks like a late nighter), then do a conda install of geopandas with conda-forge the forced repo.  Can one set a default repo [per each Environment](https://conda.io/docs/user-guide/tasks/manage-channels.html)?

Skipped the coffee, [bashed on](https://conda.io/docs/commands/env/conda-env-remove.html).  Then took a break.

Good thing I did as the pinto beans were done, just in time to turn off the crockpot.  Reheat some coffee in the microwave.  So where are we?

Navigator sees its environment is gone.  I'll recreate geopandas and then install with a -c conda-forge, meaning I specify the channel and don't leave it up to conda to decide.  Will that go any better?  Lets find out:

conda create -n geopandas python=3.6 geopandas -c conda-forge

That gets me:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj48Na9drlJOPBZ44cGT1ICsHnhl6GtmaCYQoscIurQGCcc7IdY_fK97mnveuRjB-mwAjY9xPdgYvgX5ATPY3MtLCMqbbwjCmKVZYNl15pevUk0GCHQDGlcre91U4LBZPSgkNfe/s1600/conda-forge-install-geopandas.tiff)

That's looking promising.  Will fiona slay me again?  Lets proceed.

Thanks to the way operating systems facilitate multitasking, I'm able to turn my attention to other matters.

Earlier today, the FBI was asking small business owners in the USSA ([inside joke](http://controlroom.blogspot.com/2017/02/rabble-babble.html)) to at least reboot their routers if not install actual firmware.  The Disney Parental Circle option has been added for the Netgear R7000, I discovered, upon fully complying.

Don't question Big Brother, right?  I'm sure many Russians will be equally interested in obeying, as no one wants malware on their routers, whatever the source.  Here's a screen shot.

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzEwFhZuZ5ni9fNJ7v8xiQm0LT0VDc-w7JCoxoolMCRIvjxXgq6wEwAMwoSOWAxhSOpdI_mz67UaJD6DMVJOr_drVYFtATQWhe3mY6gj_6jJQS2TVZkTmQ1LhiLOqjp79hxLbj/s1600/netgear_parental_circle.tiff)

That's after hacking in to the Netgear on 192.168.0.1 I think it was, which is actually the router behind the router facing the public internet.

This all came after my exploring the geopandas possibility earlier this Saturday.  Yes I often work on the weekends, entrepreneur that I am.  Do I keep the sabbath?  I'd welcome a conversation with rabbis about that sometime.  Netiquette has a lot in common with Jewish law?  I'm not the authority.

I'm still installing in another process.  We've put a lot of hours into spatial data management today, what with the summit meeting in Cedarhurst.  I should update the CTO.  Damn, too much on my plate!

I'm gonna get another bowl of beans and salsa and write to the NetDispenser group.  That's open source and uses the Raspberry Pi as a router, which is what I want to ask about.  I'll check on my geopandas experiment in awhile.

All right!  I document my success with the top screen shot.  A -c conda-forge on the end kept the Environment integral.  Compatibility was achieved!