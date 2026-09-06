from mimetypes import init
import pygame
from pygame import display, event
from pygame.constants import QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE, KEYS
from keys import create_key_rects, draw_keys
from slider import Slider
pressed = set()
key_rects = create_key_rects(7)
volume_slider = Slider(20, 20, 200, 0, 100, 1)
def set_volume(value):
    global singing, sound_play
    for s in singing:
        s.stop_singing()
        s.volume = value / 100.0
    play_btn.img = PLAY_BUTTON_IMG
    singing, sound_play = False, False
volume_slider.set_on_change(set_volume)

init()
screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    screen.fill(WHITE)
    display.flip()
    draw_keys(screen, key_rects, pressed)
    if e.type == KEYDOWN:
        k = key.name(e.key)
        if k in sounds:
            sounds[k].play()
            pressed.add(key_list.index(k))
    if e.type == KEYUP:
        k = key.name(e.key)
        if k in KEYS:
            pressed.discard(key_list.index(k))
    if e.type == MOUSEBUTTONDOWN:
        for i, r in enumerate(key_rects):
            if r.collidepoint(e.pos):
                sounds[keys_list[i]].play()
                pressed.add(i)
    if e.type == MOUSEBUTTONUP:
        for i, r in enumerate(key_rects):
            if i in pressed and r.collidepoint(e.pos):
                pressed.remove(i)