---
title: RSA using Pythonic Notation
id: 114827231083958702
author: Kirby Urner
published: 2006-05-21T21:24:00.000-07:00
updated: 2007-11-25T09:38:19.196-08:00
blog: control_room
tags: 
---

Euler's Theorem:if gcd(b, N) == 1: assert pow(b, totient(N), N) == 1Also, if public key N = p*q with p,q being big probable primes per [Miller-Rabin](http://en.wikipedia.org/wiki/Miller-Rabin_primality_test), then the totient(N) is simply (p-1) * (q-1).Using the [Extended Euclidean Algorithm](http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm) (EEA), we compute:  d = inverse(e, totient(N)) such that (e*d) % totient(N) == 1.So now d is the secret complement of public key N, presumably not derivable minus knowledge of factors p and q, and presumably N can't be factored in any reasonable amount of time ([win big bucks](http://www.rsasecurity.com/rsalabs/node.asp?id=2093) if you're able to crack these large Ns).Then [RSA](http://en.wikipedia.org/wiki/RSA) works essentially as follows:ciphertext = pow( plaintext, e, N)plaintext = pow( ciphertext, d, N)I've got more discussion of all this at the Math Forum under the heading of [Gnu Math](http://mathforum.org/kb/thread.jspa?threadID=1380445).