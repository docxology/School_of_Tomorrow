---
title: ScratchPad
id: 3133537293955734534
author: Kirby Urner
published: 2009-02-10T00:17:00.000-08:00
updated: 2009-02-10T07:10:51.640-08:00
blog: bizmo_diaries
tags: 
---

I've configured a Virtual Host, 4d.kirby as follows:<virtualhost>ServerName 4d.kirbyDocumentRoot /home/kirby/php_studyAddType application/x-httpd-php .php .html</virtualhost>My thanks [to Aimee](http://aimee.mychores.co.uk/about) and her personal journal, A little place of calm for [some advice](http://aimee.mychores.co.uk/2009/01/26/post/400/apache-tricks-on-linux).I've waded in up to my neck with Apache many times, but there's always "beginner mind" to come home to, along with humility and finding new teachers, including much younger ones.  The Internet lets me scour the hinterlands in search of kind souls.  And then of course there's [O'Reilly's Safari](http://controlroom.blogspot.com/2009/01/back-at-cubespace.html).Note to self:  PHP's copy-on-write is not the same as Python's memory management scheme, as assigning a second name to the same list (array) only delays copying.  The moment you update a PHP list through the added name (i.e. variable), a new copy of that array gets created in memory, whereas in Python both names keep pointing to that same list object ([everything is an object in Python](http://worldgame.blogspot.com/2009/02/regarding-objectifying.html)).