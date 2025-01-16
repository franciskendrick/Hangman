from functions import palette_swap
from ui import Interactable
from window import window
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..", "resources"
    )
)


class Restart(Interactable):
    def __init__(self):
        super().__init__()

        # Images
        btn_img = self.spritesets["restart"]
        hover_palette = {
            (218, 134, 62): (190, 119, 43),
            (222, 158, 65): (218, 134, 62)}
        hover_img = palette_swap(btn_img.convert(), hover_palette)
        self.images = [btn_img, hover_img]

        # Rectangles
        x, y = (14, 1)
        wd, ht = (11, 11)
        rect = pygame.Rect(x, y, wd, ht)
        hitbox = pygame.Rect(
            x * window.enlarge, y * window.enlarge, 
            wd * window.enlarge, ht * window.enlarge)

        # Button
        self.button = [0, rect, hitbox]  # status, rect, hitbox

    def draw(self, display):
        status, rect, _ = self.button
        img = self.images[status]
        display.blit(img, rect)

    def handle_mousemotion(self):
        status, _, hitbox = self.button
        if status != 2:
            self.button[0] = 1 if self.mouse_ishover(hitbox) else 0

    def handle_mousebuttondown(self, mouse_pos):
        _, _, hitbox = self.button
        if hitbox.collidepoint(mouse_pos):
            return True
