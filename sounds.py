import pygame

pygame.mixer.pre_init(
    frequency=44100,
    size=-16,
    channels=2,
    buffer=256
)

pygame.init()

pygame.mixer.set_num_channels(32)


sounds = {
    "a": pygame.mixer.Sound("sounds/A4(1).mp3"),
    "b": pygame.mixer.Sound("sounds/B4 Flat(1).mp3"),
    "c": pygame.mixer.Sound("sounds/C5(1).mp3"),
    "d": pygame.mixer.Sound("sounds/D5.mp3"),
    "e": pygame.mixer.Sound("sounds/E4 Flat(1).mp3"),
    "f": pygame.mixer.Sound("sounds/F5(1).mp3"),
    "g": pygame.mixer.Sound("sounds/G4(1).mp3")
}

