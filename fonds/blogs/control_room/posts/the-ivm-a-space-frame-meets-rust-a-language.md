---
title: The IVM (a space frame) Meets Rust (a language)
id: 7675317201069593681
author: Kirby Urner
published: 2019-11-20T14:09:00.001-08:00
updated: 2019-11-20T22:07:45.980-08:00
blog: control_room
tags: 
---

Harkening back to [OSCON 2019](https://worldgame.blogspot.com/2019/07/oscon-2019-begins.html), I'm diving into Rust again, a new fast-growing state of the art computer language.  Or rather, the community of Rust-fluent is fast-growing, whereas Rust is showing signs of stabilizing, much as Python has.  I'm told it inherits from ML, a favorite in the compsci crowd.

I grew up doing non-commercial programming for nonprofits, mostly, though the doctor practice took some initiative in sharing our work with commercial developers.  A real heart surgeon, working closely with a talented programmer (ahem), using Visual FoxPro, could fly around the country showing something battle-tested in CVOR.  No one had anything like it.  People thought I might be standing to make a lot of money, but I was just a consultant for Sisters of Providence, one of Oregon's biggest employers.

This was all before Python even existed, at least in my consciousness, nor did Python come bundled with a core developer supported GUI toolkit.  Guido got some DARPA funding to make Tk/tcl the GUI default, thanks to the tkinter module.  Later DARPA funded the Anaconda team to mainstream Spyder, built not on tcl ("tickle") but Qt ("cute").

Anyway, Rust is coming over the horizon and I have a golden application in the form of quadrays, an alternative vector class that uses the same traits for an interface, in terms of addition, subtraction, scalar multiplication and so on as ordinary XYZ vectors.  You could think of (4, 3, 1, 0) as simply an alternative representation of a corresponding set of XYZ coordinates.  That's what I'm using Rust to figure out.

(base) Kirbys-MacBook-Pro:quadrays mac$ cargo run

   Compiling quadrays v0.1.0 (/Users/mac/rust/projects/quadrays)

    Finished dev [unoptimized + debuginfo] target(s) in 10.22s

     Running `target/debug/quadrays`

q_a.a = 1

q_a.b = 0

q_sum.c = 1

q_sum.b = 1

xyz coords = [0.0, 0.0, 0.7071067811865475]

xyz coords for (4, 3, 1, 0)  = [0.0, 0.7071067811865475, 2.1213203435596424]