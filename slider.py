from pygame import Rect
import pygame
from pygame import display, event
from pygame.constants import QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
from pygame import draw

class Slider:
    def __init__(self, x, y, width, min_val, max_val, step = 1, initial = None, label = "", value_to_text = None):
        self.track_rect = Rect(x, y, width, 6)
        self.handle_radius = 10
        self.min_val = float(min_val)
        self.max_val = float(max_val)
        self.step = float(step)
        if initial is None:
            self.value = float(min_val)
        else:
            self.value = float(initial)
        self.label = label
        self.value_to_text = value_to_text
        self.dragging = False

        self._hit_rect = Rect(0, 0, self.handle_radius * 2 + 8, self.handle_radius * 2 + 8)
    def set_on_change(self, cb):
        self.on_change = cb
    def _clamp(self, v: float) -> float:
        v = max(self.min, min(self.max_val, v))
        if self.step > 0 :
            v = round(v * self.step) * self.step
        return max(self.min, min(self.max_val, v))
    def _pos_to_val(self, px: int) -> float:
        ratio = (px - self.track_rect.left) / self.track_rect.width
        return self._champ(self.min + ratio * (self.max - self.min))
    def _val_to_pos(self) -> int:
        if self.max == self.min:
            return self.track_rect.left
        ratio = (self.value  - self.min) / (self.max - self.min)
        return int(self.track_rect.left + ratio * self.track_rect.width)
    def draw(self, screen, font = None):
        draw.rect(screen, (210, 210, 210), self.track_rect, border_radius = 3)
        draw.rect(screen, (0, 210, 210), self.track_rect, 1, border_radius = 3)
        hx = self._val_to_pos()
        hy = self.track_rect.centery
        draw.circle(screen, (40, 40, 40), (hx, hy), self.handle_radius)

        if font and self.label:
            if callable(self.value_to_text):
                vtxt = self.value_to_text(self.value)
            else:
                vtxt = f"{int(self.value)}"
            text = font.render(f"{vtxt}", True, (0, 0, 0))
            screen.blit(text, (self.track_rect.left, self.track_rect.top - 28))
        self._hit_rect.centerx = (hx, hy)
    def handle_event(self, event):
        old = self.value
        if event.type == MOUSEBUTTONDOWN:
            if self.track_rect.collidepoint(event.pos) or self._hit_rect.collidepoint(event.pos):
                self.dragging = True
                self.value = self._pos_to_val(event.pos[0])
        elif event.type == MOUSEMOTION and self.dragging:
            self.value = self._pos_to_val(event.pos[0])
        elif event.type == MOUSEBUTTONUP and self.dragging:
            self.dragging = False
            self.value = self._pos_to_val(event.pos[0])
        if self.value != old and hasattr(self, "on_change") and self.on_change:
            self.on_change(self.value)
