import pygame as py
import time

while game :
    
    clock.tick(60)
    for event in py.event.get():
        if event.type == py.QUIT:
            game = False

    screen_group.draw(window)

    pontodpl()
    checabreja()

    group_mbp.draw(window)
    capy_group.draw(window)
    group_brj.draw(window)
    group_mbp.update()
    capy_group.update()
    group_brj.update()
    screen_group.update()
    

    py.display.update()
py.quit()