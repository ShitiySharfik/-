import pygame
from pygame import Rect
from effects import draw_key_effect

NOTE_NAMES = [
    "A4",
    "Bb4",
    "C5",
    "D5",
    "Eb4",
    "F5",
    "G4"
]

KEY_NAMES = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G"
]


def draw_keys(screen, keys_rects, pressed_keys):
    note_font = pygame.font.SysFont("Arial", 24, bold=True)
    key_font = pygame.font.SysFont("Arial", 20, bold=True)

    for i, rect in enumerate(keys_rects):
        is_pressed = i in pressed_keys

        draw_key_effect(screen, rect, is_pressed)

        if is_pressed:
            note_color = (255, 255, 255)
            key_color = (200, 200, 200)
        else:
            note_color = (0, 0, 0)
            key_color = (80, 80, 80)

        note_text = note_font.render(
            NOTE_NAMES[i],
            True,
            note_color
        )

        note_rect = note_text.get_rect(
            center=(rect.centerx, rect.centery - 25)
        )

        screen.blit(note_text, note_rect)

        key_text = key_font.render(
            KEY_NAMES[i],
            True,
            key_color
        )

        key_rect = key_text.get_rect(
            center=(rect.centerx, rect.centery + 25)
        )

        screen.blit(key_text, key_rect)


def create_key_rects(
num_keys,
window_width=800,
start_y=100,
key_width=90,
key_height=250,
gap=5
):
    rects = []

    total_width = (
    num_keys * key_width
    + (num_keys - 1) * gap
)

    start_x = (window_width - total_width) // 2

    for i in range(num_keys):
        x = start_x + i * (key_width + gap)

        rects.append(
            Rect(
                x,
                start_y,
                key_width,
                key_height
            )
        )

    return rects