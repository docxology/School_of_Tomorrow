---
title: Abducted!
id: 1958646203829387795
author: Kirby Urner
published: 2017-08-23T13:35:00.002-07:00
updated: 2017-08-23T13:38:13.441-07:00
blog: bizmo_diaries
tags: 
---

stage.set_background("summer")

nyc_girl = codesters.Sprite("person10", -100, -100)
girl2 = codesters.Sprite("person7", 50, -100)

ufo = codesters.Sprite("ufo")
ufo.glide_to(100, 200)

nyc_girl.say("OMG! What's that???")
stage.wait(2)
girl2.say("I think it's a flying saucer!!!")
stage.wait(2)

nyc_girl.say("")
girl2.say("")

ufo.glide_to(-400, 200)

def click():
    x = stage.click_x()
    y = stage.click_y()
    ufo.glide_to(x, y)
    # add other actions...

stage.event_click(click)

def space_bar():
    nyc_girl.jump(1)
    # add other actions...

stage.event_key("space", space_bar)

def enter_key():
    nyc_girl.hide()
    # add other actions...

stage.event_key("enter", enter_key)

def up_key():
    girl2.jump(1)

stage.event_key("up", up_key)

def down_key():
    girl2.hide()
    # add other actions...

stage.event_key("down", down_key)

def a_key():
    # add other actions...
    stage.set_background("moon")
    ufo.glide_to(0,0)
    ufo.glide_to(0,100)
    girl2.show()
    nyc_girl.show()
    nyc_girl.glide_to(-100, -100)
    girl2.glide_to(50, -100)
    nyc_girl.say("OK, so now what?")

stage.event_key("n", a_key)