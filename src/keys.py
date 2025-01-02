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


class Keys(Interactable, Font):
    def __init__(self):
        super().__init__()

        # Images
        btn_img, used_attachment = self.spritesets["keys"]
        hover_palette = {
            (23, 32, 56): (1, 1, 5),
            (37, 58, 94): (12, 16, 31),
            (115, 190, 211): (60, 94, 139),
            (164, 221, 219): (79, 143, 186)}
        hover_img = palette_swap(btn_img.convert(), hover_palette)
        self.images = [btn_img, hover_img, used_attachment]

        # Buttons
        self.buttons = {}

        order = [
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M'
        ]
        idx = 0

        wd, ht = (9, 9)
        x_ranges  = [range(2, 100, 10), range(7, 95, 10), range(17, 85, 10)]
        for y_idx, y in enumerate(range(48, 78, 11)):
            for x in x_ranges[y_idx]:
                rect = pygame.Rect(x, y, wd, ht)
                hitbox = pygame.Rect(
                    x * window.enlarge, y * window.enlarge, 
                    wd * window.enlarge, ht * window.enlarge)
                self.buttons[order[idx]] = [0, rect, hitbox]  # status, rect, hitbox

                idx += 1

    def draw(self, display):
        for button in self.buttons.values():
            status, rect, _ = button
            if status == 2:
                img = self.images[1]
                attachment = self.images[2]

                display.blit(img, rect)
                display.blit(attachment, (rect.x - 1, rect.y - 1))
            else:
                img = self.images[status]

                display.blit(img, rect)

    def handle_mousemotion(self):
        for button in self.buttons.values():
            status, _, hitbox = button
            if status != 2:
                button[0] = 1 if self.mouse_ishover(hitbox) else 0

    def handle_mousebuttondown(self):
        mouse_pos = pygame.mouse.get_pos()

        for letter, button in self.buttons.items():
            status, _, hitbox = button
            if status != 2 and hitbox.collidepoint(mouse_pos):
                button[0] = 2
                return letter

    def restart(self):
        for button in self.buttons.values():
            button[0] = 0
