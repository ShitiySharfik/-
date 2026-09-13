import pygame
from pygame import display, event
from pygame.constants import QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP

from settings import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE, KEYS, BLACK
from keys import create_key_rects, draw_keys
from slider import Slider
from sounds import sounds
import random
from effects import draw_symbol


pressed = set()

keys_list = list(KEYS.keys())

key_rects = create_key_rects(
    len(keys_list),
    window_width=WINDOW_WIDTH
)

symbols = []
wingdings_symbols = [
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P"
]



volume_slider = Slider(20, 20, 200, 0, 100, 1)
secret_sequence = [
"g",
"a",
"a",
"g",
"a",
"a",
"g",
"a"
]

played_sequence = []

theme_started = False

volume_slider = Slider(20, 20, 200, 0, 100, 1)

def set_volume(value):
    volume = value / 100.0

    for sound in sounds.values():
        sound.set_volume(volume)

# Меняем громкость фоновой темы тоже
    pygame.mixer.music.set_volume(volume * 0.3)

def set_volume(value):
    volume = value / 100.0

    for sound in sounds.values():
        sound.set_volume(volume)


volume_slider.set_on_change(set_volume)


pygame.init()

screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True

while running:
    for e in event.get():

        if e.type == QUIT:
            running = False

        elif e.type == KEYDOWN:

            k = pygame.key.name(e.key)

            if k in sounds:

                i = keys_list.index(k)

                # Проигрываем ноту
                sounds[k].play()

                # Добавляем клавишу в последовательность
                played_sequence.append(k)

                # Оставляем только последние 8 нажатий
                if len(played_sequence) > len(secret_sequence):
                    played_sequence.pop(0)

                print("Нажатия:", played_sequence)

                # Проверяем комбинацию
                if played_sequence == secret_sequence:

                    print("ТЕМА ЗАПУСКАЕТСЯ!")

                    if not theme_started:
                        pygame.mixer.music.load(
                            "sounds/mus_st_him.ogg"
                        )

                        pygame.mixer.music.set_volume(0.3)

                        pygame.mixer.music.play(-1)

                        theme_started = True

                # Создаём символ
                symbols.append({
                    "symbol": wingdings_symbols[i],
                    "x": key_rects[i].centerx,
                    "y": key_rects[i].top,
                    "alpha": 255,
                    "speed": random.uniform(0.3, 0.6)
                })

            if k in keys_list:
                pressed.add(
                    keys_list.index(k)
                )

        elif e.type == KEYUP:

            k = pygame.key.name(e.key)

            if k in keys_list:
                pressed.discard(
                    keys_list.index(k)
                )

        elif e.type == MOUSEBUTTONDOWN:

            for i, r in enumerate(key_rects):

                if r.collidepoint(e.pos):

                    key = keys_list[i]

                    # Проигрываем ноту
                    sounds[key].play()

                    pressed.add(i)

                    # Добавляем клавишу
                    played_sequence.append(key)

                    if len(played_sequence) > len(secret_sequence):
                        played_sequence.pop(0)

                    print("Нажатия:", played_sequence)

                    # Проверяем комбинацию
                    if played_sequence == secret_sequence:

                        print("ТЕМА ЗАПУСКАЕТСЯ!")

                        if not theme_started:
                            pygame.mixer.music.load(
                                "sounds/mus_st_him.ogg"
                            )

                            pygame.mixer.music.set_volume(0.3)

                            pygame.mixer.music.play(-1)

                            theme_started = True

                    # Создаём символ
                    symbols.append({
                        "symbol": wingdings_symbols[i],
                        "x": key_rects[i].centerx,
                        "y": key_rects[i].top,
                        "alpha": 255,
                        "speed": random.uniform(0.3, 0.6)
                    })

        elif e.type == MOUSEBUTTONUP:

            for i, r in enumerate(key_rects):

                if i in pressed and r.collidepoint(e.pos):
                    pressed.remove(i)

    screen.fill(BLACK)

    draw_keys(
        screen,
        key_rects,
        pressed
    )

    # Анимация символов
    for symbol in symbols[:]:

        symbol["y"] -= symbol["speed"]

        symbol["alpha"] -= 1

        draw_symbol(
            screen,
            symbol["symbol"],
            symbol["x"],
            symbol["y"],
            max(
                0,
                int(symbol["alpha"])
            )
        )

        if symbol["alpha"] <= 0:
            symbols.remove(symbol)

    display.flip()
