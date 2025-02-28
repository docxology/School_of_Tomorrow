---
title: More Curriculum Writing re MVC
id: 7575838307268008040
author: Kirby Urner
published: 2007-09-17T11:44:00.001-07:00
updated: 2008-11-15T02:36:28.870-08:00
blog: control_room
tags: 
---

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivFeP-zveCd6JXRCfg52M2z74YCZ-yWzj93RG-lEwi9DIyOfdCYXNFO9nzyUZdvJzHKcWu3Zw7KqAuCZ71zSzMk78sksftGVIEfNp9oaMgaImxHF1-GQ8Yj5LeCcuWe7crGSvl/s1600-h/mvc_user.png)(click pic for larger view)The innovation here is putting an end user in the picture, both "for real" and as a figment in the model, i.e. as the "[modelled](http://www.answers.com/modelled&r=67) end user" (or users as the case may well be).Modeling its users is part of what a model should be doing, as a part of its job of persisting state.  And no, I'm not just talking about delegate avatars per Second Life and Active Worlds.  A user model might be quite primitive, as low level as "logged in" versus not.By this way of thinking, a user-controlled change in view needn't involve the view subscribing to the controller directly, as the model itself is made aware of some end user's change in preference (through the controller), so that next time the viewer polls, or otherwise gets notified of state changes, the view is refreshed accordingly.Adding the end user, in other words, turns this MVC picture into a classic feedback loop of cybernetics fame.The end user steers and fine tunes the model in response to what the model is showing (or maybe how it smells? -- this user has a big nose and the viewer looks like a funnel).Of course this diagram makes no judgment as to the suitability of the model for the task at hand, i.e. some closed loops like this become dead ends -- which is why it's important to get your head out of your model from time to time (which is your freedom, as a human being).