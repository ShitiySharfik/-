import pygame
from pygame import draw
from settings import BLACK

def draw_key_effect(screen, rect, is_pressed=False):
    if not is_pressed:
        base_color = (220, 220, 220)
    else:
        base_color = (50, 50, 50)

    border_color = BLACK

    draw.rect(screen, base_color, rect, border_radius=8)
    draw.rect(screen, border_color, rect, 2, border_radius=8)


def draw_symbol(screen, symbol, x, y, alpha):
    font = pygame.font.SysFont("Wingdings", 32)

    text = font.render(symbol, True, (255, 255, 255))
    text.set_alpha(alpha)

    text_rect = text.get_rect(center=(x, y))

    screen.blit(text, text_rect)