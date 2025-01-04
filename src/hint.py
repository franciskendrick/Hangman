from functions import palette_swap
from ui import Font, Interactable
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


class Hint(Interactable, Font):
    def __init__(self):
        Interactable.__init__(self)
        Font.__init__(self)

        self.init_button()
        self.init_bookmarks()

    def init_button(self):
        # Images
        btn_img, used_img = self.spritesets["hint"]
        hover_palette = {
            (218, 134, 62): (190, 119, 43),
            (222, 158, 65): (218, 134, 62),
            (232, 193, 112): (222, 158, 65),
            (231, 213, 179): (232, 193, 112),
            (32, 46, 55): (21, 29, 40)
        }
        hover_img = palette_swap(btn_img.convert(), hover_palette)
        self.btn_images = [btn_img, hover_img, used_img]

        # Buttons
        x, y, wd, ht = (1, 1, 11, 11)
        rect = pygame.Rect(x, y, wd, ht)
        hitbox = pygame.Rect(
            x * window.enlarge, y * window.enlarge, 
            wd * window.enlarge, ht * window.enlarge)
        self.button = [0, rect, hitbox]

    def init_bookmarks(self):
        self.bookmark_image = self.spritesets["bookmark"]
        self.bookmark_rects = [
            pygame.Rect(0, 13, 8, 7),
            pygame.Rect(0, 21, 8, 7)
        ]

    def draw(self, display):
        # Draw button
        status, rect, _ = self.button
        display.blit(self.btn_images[status], rect)

        # Draw bookmarks
        for rect in self.bookmark_rects:
            display.blit(self.bookmark_image, rect)
