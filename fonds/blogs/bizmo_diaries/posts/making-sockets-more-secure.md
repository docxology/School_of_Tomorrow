---
title: Making Sockets More Secure
id: 2961991561930011109
author: Kirby Urner
published: 2023-01-03T17:37:00.009-08:00
updated: 2023-01-03T17:47:53.933-08:00
blog: bizmo_diaries
tags: 
---

An issue CJ and I would argue about, was whether browsers were amiss in relegating unencrypted websites to second class status.  Chrome seemed especially heavy-handed.

I'd taken up the position that sticking with HTTP was no sin, any more than not wearing a mask, or wearing one.  In principle, we don't have enough info to talk about who's being "too unforgiving".  The bare fact of using HTTP does not warrant any kind of moral or aesthetic judgement.

I had a dog in the fight: through 2022, my Grunch.net, host of Synergetics on the Web, and hosted at GoDaddy, was serving plain old HTTP, with no encryption, no security certificate.  Perhaps for this reason, although I'm not clear on the mechanics, my ability to connect to my own website was degrading.

I cannot quite imagine what whitelist or blacklist would be frustrating traffic through my two routers, one behind the other, when neither registered any explicit blocking.  Was CenturyLink getting involved up line from me?  I'd reboot the routers, and at least temporarily regain access to the site -- or not (even that stopped fixing the issue).  

We could still ping and traceroute the grunch.net domain, just not get through to the server, netting a timeout instead.  Yet that very same website, viewed through Verizon, on a phone, was still quite responsive.  "What's up with that?" was the thinking.

Anyway, in the midst of all this confusion I decided it was time to bite the bullet and tackle the HTTP issue more directly, by upgrading Grunch.net to an HTTPS site.  

GoDaddy had a solution waiting.  I was able to follow the steps myself, although not without some confusing chat sessions (by voice and by text) with disgruntled tech support humans.

I'd point out to CJ that many of our treasured websites no longer had active administrators behind them.  Webmasters pass away.  Getting them converted over to HTTPS would require someone taking active measures and assuming administrative responsibility.  Is that even possible in all cases?  Given our rough and tumble Global U reality, we have no right to assume such faculty will be available.