import pygame
from pygame import *
import random as randit
window_size = 1200,800
window = pygame.display.set_mode(window_size)
player_rect = Rect(50, 500, 100, 100)
keys = pygame.key.get_pressed()
import pygame

pygame.init()
window_size = (1200, 800)
window = pygame.display.set_mode(window_size)

player_rect = pygame.Rect(50, 500, 100, 100)
#PIPE_BASE = image.load("pipe.png")
#PIPE_W, PIPE_H = 120, 440
#PIPE_BOTTOM = transform.scale(PIPE_BASE, (PIPE_W, PIPE_H))
#PIPE_TOP = transform.flip(PIPE_BOTTOM, False, True)
def generate_pipes(count, pipe_width=140, gap=280, min_heigt=50,max_heigt=440,distance=600):
    pipes = []
    start_x = window_size[0]
    for i in range(count):
        height = randit.randint(min_heigt, max_heigt)
        top_pipe = Rect(start_x, 0 , pipe_width, height)
        bottom_pipe = Rect(
            start_x,
            height + gap,
            pipe_width,
            window_size[1] - (height + gap)
        )

        pipes.extend([top_pipe,bottom_pipe])
        start_x += distance
    return pipes
pipes = generate_pipes(150)
if len(pipes) < 8:
    pipes += generate_pipes(150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_rect.y -= 5

    if keys[pygame.K_s]:
        player_rect.y += 5

    window.fill("aqua")

    for pipe in pipes[:]:
        pipe.x -= 3

        pygame.draw.rect(window, "green", pipe)

        if pipe.x <= 100:
            pipes.remove(pipe)

        if player_rect.colliderect(pipe):
            lose = True

    pygame.draw.rect(window, "yellow", player_rect)

    pygame.display.flip()



    pygame.display.flip()