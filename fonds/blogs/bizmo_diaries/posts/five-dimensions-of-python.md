---
title: Five Dimensions of Python
id: 4992761918380102802
author: Kirby Urner
published: 2017-09-26T21:23:00.002-07:00
updated: 2017-10-02T23:28:26.220-07:00
blog: bizmo_diaries
tags: 
---

Understand that I'm using the term "dimension" loosely, perhaps to structure a TED Talk, or TEDx or something similar.

The Roman orator, Cicero a role model, learned to break it down into chunks.  If the chunks were too fine:  a host of problems.  Too big:  problems there too.

The goal of the accomplished orator was to get the chunk size "just right" for the intended audience.

The first dimension is like your utility belt, so close to home base you consider its content basic, and full of "built-ins" as these tools are called.

Here is your basic vocabulary for bootstrapping all the rest.  Any classic Python shell provides them natively.

In __builtins__ you get your "import" (for expanding the vocabulary) and your "open" (for streaming), your several workhorse types: list and range (sequences), some number types (int, float, bool), the string type (str, another sequence), the dictionary (dict) and the set (the not-sequences or mappings).

Functions such as "iter" "next" and "divmod" grace the builtins, with "property" a built-in class (used as a decorator when the time comes).  The large number of built-in exceptions are not "junk DNA" but rather the signalling system used to recover gracefully from inevitable glitches.

Before dimension one though, is dimension zero: the keywords. Forgive me for going out of sequence.  The builtins are actually somewhat easier to grasp, as objects, than these more ephemeral tokens of the Python grammar.  Words like "if" "else" and "lambda".

In any case, I propose we should number our dimensions from zero like Python does.

Dimension Zero are the keywords and related punctuation, such as colon, square brackets, quote marks (single and double, then triple of either).  Dimension Zero provides the original syntax you'll need to structure your programs, to tell a story of what happens among its several players (the objects). 

Only three of the keywords are uppercase: True, False and None.  About 35 in all, for looping, branching, making functions and classes (callables).  No keyword is a callable.  In prehistoric Python, before the great leap, "print" was a keyword, yet today is a built-in function.

By dimension two, we're looking at "special names" (or call them __ribs__), provided by the language, meaning new ones get added from version to version, but they're not for the Python coder to create.

Like the keywords and builtins, we accept them as given.  They have that funny look:  __getitem__, __getattr__, __setitem__, __setattr__ ... __add__, __mul__ and __call__.  With these "puppet strings" we're able to control the behavior of our objects down to the syntactical level.

What should be the effect of using square brackets right up against my objects?  What should it do when "called" with curved parentheses?  How should two objects of my own devising interpret the addition or multiplication operator?

I'm empowered to devise alternative languages, or to approximate existing ones more closely. M1 @ M2 might result in matrix multiplication, while (f * g)(x) might be massaged to mean the same as f(g(x)).

Such sinewy flexibility, built right in to the language, could easily become a justification for the snake motif.  A snake is a subtype of dragon.  Perhaps Python has the connotation of "dragon language" in a more Chinese take on computer science.

Dimension three: the Standard Library.  Here, with "batteries included" we reach a frontier.  Any Python distribution is likely to come with all of the above, after which we reach dimension four.

Dimension four includes anything from simple one-module libraries, to frameworks and distributions.  One might further differentiate between these levels, however keeping it all zero to four has its advantages.

When I teach Python to others, I'll be specific about these dimensions and then begin spiraling in all five over time.

In a given lesson, we'll add a couple more keywords here, a special name there, a built-in, and then a module.

By "add" I mean "add to the student's knowledge base" i.e. to the student's awareness of a complete ecosystem, still evolving. Python is a moving target, but it's never too late to catch up.

Even core Python is evolving, both as a language specification and in terms of its implementations.

Python has been implemented in C, C#, Java (Jython) and in a more simplified version of itself (PyPy).  Python has likely been implemented in languages I don't know about.

Then we have Cython, a superset of Python with more compile time goodness.

We should expect people not that conversant with this variegated geography (territory) to get somewhat lost in it sometimes.

Partly why I offer these simplifying schematics and "[dimension talk](https://github.com/4dsolutions/Python5/blob/master/Dimensions%20of%20Python.ipynb)" is to tame the wilderness or wildness (entropy) and bring some order out of chaos.