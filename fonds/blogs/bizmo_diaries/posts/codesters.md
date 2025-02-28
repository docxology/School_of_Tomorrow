---
title: Codesters
id: 1766356925226122751
author: Kirby Urner
published: 2019-06-05T12:37:00.002-07:00
updated: 2019-06-05T12:37:19.738-07:00
blog: bizmo_diaries
tags: 
---

sprites = [ ]def select(sel):    for s in sprites:        s.selected = False            for s in sprites:        if s.sprite is sel:            s.selected = Trueclass Triangle:        def __init__(self, x=0,y=0, color='blue'):        self.color = color        self.x = x        self.y = y        self.selected = False        sprites.append(self)        def draw_me(self):        # sprite = codesters.Triangle(x, y, size, "color")        self.sprite = codesters.Triangle(self.x, self.y, 100, self.color)        self.sprite.event_click(select)    def move_me(self):        self.sprite.glide_to(x, y)    tri_one = Triangle()tri_one.draw_me()tri_two = Triangle(-100,100,'red')tri_two.draw_me()tri_three = Triangle(-50, 50, 'yellow')tri_three.draw_me()tri_four = Triangle(100, -100, "orange")tri_four.draw_me()def move_it():    global x, y    x = stage.click_x()    y = stage.click_y()    for s in sprites:        if s.selected:            s.move_me()stage.event_click(move_it)