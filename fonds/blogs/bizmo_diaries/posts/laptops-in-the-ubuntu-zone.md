---
title: Laptops in the Ubuntu Zone
id: 8143803747857243001
author: Kirby Urner
published: 2007-07-23T11:39:00.000-07:00
updated: 2007-08-08T12:51:56.178-07:00
blog: bizmo_diaries
tags: 
---

I'm still suffering [some embarrassment](http://controlroom.blogspot.com/2007/07/idiomatic-python.html) for having lugged the Toshiba, a Windows machine, after breaking in an Ubuntu laptop by lugging it half way around the world, just for such an occasion as this:  a session on [supporting laptops](http://www.linuxinsider.com/story/57747.html) in Ubuntu.  Our speaker is Matthew Garrett.CPUs, graphics cards, and SATA chipsets are the three main areas of divergence with desktop PCs.  Laptops still have a somewhat broader range of graphic chip, but it's what's unique to laptops that makes them harder to support:  hotkeys, webcams, sound codecs, suspend/resume quirks, flash readers, rotating screens, hard drive protection and a huge variety of wireless chipsets.Manufacturers with smarts define new scan codes for hotkeys, whereas the more retarded ones (Toshiba included) insist on special magic in the ACPI, even special hardware.  Webcams still need proprietary drivers.  Every manufacturer has a different way of protecting the hard drives.  Intel is good at releasing Linux drivers for its wireless solutions.  Broadcom, Atheros, pretty much anyone else:  a nightmare.Ubuntu is making steady progress and already sets the standard for running a single Linux distro on many models of laptop.  The Dell I left at home came in for some praise, in terms of having solved many of the integration issues.