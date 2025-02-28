---
title: Retro Coding
id: 3012700852859568573
author: Kirby Urner
published: 2017-07-01T20:14:00.001-07:00
updated: 2017-07-02T11:52:09.906-07:00
blog: bizmo_diaries
tags: 
---

:: talks about CGI in the client / server context ::

Retro Coding is where one deliberately dials back to an earlier point in time and uses tools at that time considered cutting edge, but since abandoned.

A case in point:  "Common Gateway Interface" or "CGI" programming. "Computer-generated Imagery" is the more common decoding; a name collision (just get clear on the namespace, for less cognitive dissonance).

In Python, we import the cgi module primarily for access to FieldStorage, an object that plays the role of sys.argv in some ways, the latter being a list object intermediary between "__main__" (the running namespace) and the shell command used to start a script.

For example:  
$ ./get_chem.py Au  

passes Au as a string string element to the running get_chem.py, which finds it in sys.argv[1].  'get_chem.py' itself, the name of the running script, is what's in sys.argv[0].

Here's an example lookup operating, running the above lookup about gold ("Au"):

[ ](https://www.flickr.com/photos/kirbyurner/35660955965/in/dateposted-public/) 

That's Python's standard library CGI server in the background, plain vanilla.  The going rate is not included. This pared down database lists he abbreviation and longer name, number of protons, and atomic mass.  The long integer and KTU track when a user last touched the record, me in this case.

>>> num1493462392>>> datetime.datetime.fromtimestamp(num)datetime.datetime(2017, 4, 29, 3, 39, 52)

The invocation in the foreground triggers a little script to send an HTTP request to said server, with a chemical element symbol (e.g. Au for Gold), which, if all goes well, returns a JSON string which the little script converts, to a list.  Print to console.  We're done:

[](https://www.flickr.com/photos/kirbyurner/35273815140/in/dateposted-public/)

Taking a look at that script, we see the Python DBI in action. That could have been Oracle we were talking to, like in the good old days (mythological allusion).

[](https://www.flickr.com/photos/kirbyurner/35273860470/in/dateposted-public/)

I've changed the shebang line to /usr/bin/env python, which is fine if you're running Python3 or greater, and shared the two scripts [via Github](https://github.com/4dsolutions/Python5/), for educational use.  Thanks to [WorkingIt](http://workingit.com/)!

The database table, periodic_table.db, is likewise available.  I'm continuing to evolve this little project, adding AJAX to the mix.