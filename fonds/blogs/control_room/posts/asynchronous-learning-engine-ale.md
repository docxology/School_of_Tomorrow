---
title: Asynchronous Learning Engine (ALE)
id: 6541091069398204595
author: Kirby Urner
published: 2015-08-02T10:46:00.000-07:00
updated: 2015-08-22T10:55:03.322-07:00
blog: control_room
tags: 
---

[](https://www.flickr.com/photos/kirbyurner/17304692495/in/album-72157654417641521/)

I created a stub outline of an Asynchronous Learning Engine on GitHub today (link below).  That may sound impressive however all the classes are abstract stubs, with an underlying metaphor.  The implementation is left as an exercise.

The metaphor (living at the base class level) centers on picturing airplane flights as courses of study, with a beginning, middle and end.  One could do ships and cruises -- hey, they're just metaphors, feel free to mix 'em.  "Geek cruises"are a reality already, including of the non-metaphoric kind.

Names like Student, Course, Mentor make up the foreground, but without leaving our extended metaphors behind.  The course fills to a minimum, gets start and stop dates, but in many models students manage their own time (talking months) and finish anytime before deadline.

Some are in a hurry, some not.  Some have time to study hard, others have only tiny windows in their day, to inch ahead.  Few if any synchronized events are required therefore.  It's not about all moving in lockstep, even if in the same course.  That doesn't preclude some exercises involving a stop watch or timer.

The Flight Recorder (built in to the Course or Airplane class) saves the transactions, meaning submitted and handed back work, communications to and from a mentor. Quality Assurance (QA) is about going over these records and learning from them.

[](https://www.flickr.com/photos/kirbyurner/20014016398/in/album-72157654417641521/)

Feedback loops are the name of the game.  Mentors improve by learning from each turn in the cockpit, perhaps we have co-pilots (like co-clerks, of committees).  One might be the apprentice of the other in one course, the senior pilot in another.  Mentors are students themselves as there's never a shortage of new stuff to learn, new skills to pick up.

Some designs encourage chatter amongst the passengers however more typical is the private one-on-one experience, with the mentor interacting individually with everyone and anyone in the course (or courses -- in this world a mentor may fly several airplanes simultaneously, called "multi-tasking", just as a student may take more than one course at a time, just like in college).

What I envision as a typical use case are EC2 / AWS (Amazon) type implementations of the Personal Studio or Personal Workspace (PWS) model, such that learners remote in to their personal Ubuntu or whatever, the instance pre-configured per whatever course design.

Are we doing [2D & 3D graphics](http://mybizmo.blogspot.com/2015/08/stem-carbon-as-theme.html)?  Is [VPython](http://vpython.org/) installed?  That all depends on the course, although presumably there are many parts of the Ux (user experience) that are common to all courses, giving a branded and perhaps eventually familiar, look and feel.  A student might work on more than one course within a given PWS instance.

Containerized services at the other end of a student dashboard given [the "traveler"](http://mybizmo.blogspot.com/2010/02/learning-on-line.html) (wanderer, browser, tourist, visitor, guest... scout) a way to "book flights" including with "connecting flights".

The mentor dashboard shows the task queues (see source outline below).

Student and mentor are connected asynchronously through the ALE.  That's it's primary job, to glue together all the components required to run an airline (or railroad, if you prefer).

For example:  { Ruby
                        ↣ Rails 
                        ↣ JavaScript in the Browser (including JQuery) 
                        ↣ JS on the Server } would earn a merit badge or certificate in our "learning by doing" space (hiking trail metaphors apply also -- [as in scouting](http://mathforum.org/kb/message.jspa?messageID=9748346)).

I've been looking at { Python ↣ Java ↣ Clojure }  as a set of connecting flights, perhaps spanning [grades 10 to 16](https://mail.python.org/pipermail/edu-sig/2015-August/011290.html).  The ALE does not nail down curriculum content per se.  Its job is to organize students into courses, assign them mentors, and keep things moving forward towards completion.  Course designers have a known framework to work with -- whatever version of ALE the client / school uses.  

Mentors, like students, have different availability, different schedules, as well as areas of expertise.  That's where Air Traffic Controlling (Dispatching) comes in.  We need admin to help us with load balancing such that no one mentor burns out under the caseload.  

"Adding to the fleet" where demand is high is easy with ALE (our in-house system, not Open Source, isn't called that).  Smaller more esoteric courses may have higher marginal costs, but add to a school's luster in other ways (guest mentors may be celebs in their fields).

Colleges and universities may be set in their ways and may as yet have no internal 
"dog food" they might eat and/or modify, nothing Open Source to share and partake in.  

Sometimes upstart companies, 
including not-for-profits, NGOs, are better positioned to try new 
things.  ALE is not just another Moodle or Banner.  

For further reading:
[ALE Use Case](http://worldgame.blogspot.com/2015/07/pws-personal-workspace.html)
[GitHub Repo](https://github.com/4dsolutions/async_learning_engine)
[clojure-python](https://clojars.org/clojure-python)