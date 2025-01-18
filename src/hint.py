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
    def __init__(self, hint1, hint2):
        Interactable.__init__(self)
        Font.__init__(self)

        self.init_button()
        self.init_bookmarks([hint1, hint2])

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

    def init_bookmarks(self, hints):
        ys = [13, 21]

        # Hint
        self.hints = []
        for hint, y in zip(hints, ys):
            wd, ht = self.get_size(hint)
            surf_wd, surf_ht = (wd+1, ht+2)
            hint_display = pygame.Surface((surf_wd, surf_ht))

            hint_display.fill((165, 48, 48))
            self.render_font(hint_display, hint, (2, 1))
            rect = pygame.Rect(-surf_wd, y, surf_wd, surf_ht)

            hint = [False, 0, hint_display, rect]  # is_showed, idx, img, rect
            self.hints.append(hint)

        # Bookmarks
        self.bookmark_image = self.spritesets["bookmark"]
        self.bookmark_rects = []
        for _, _, _, rect in self.hints:
            rect = pygame.Rect(rect.x + rect.w, rect.y, 8, 7)
            self.bookmark_rects.append(rect)

    def draw(self, display):
        # Draw button
        status, rect, _ = self.button
        display.blit(self.btn_images[status], rect)

        # Draw hints and bookmarks
        for i, (hint_data, bookmark_rect) in enumerate(zip(self.hints, self.bookmark_rects)):
            is_showed, idx, hint, rect = hint_data
            
            if is_showed and rect.x < 0:
                # Update hint's x position using ease-out (parabola) equation: f(x) = -0.025x(x-wd)
                rect.x += -(0.025 * idx) * (idx - rect.w)
                rect.x = min(rect.x, 0)  # ensure x doesn't exceed 0
                bookmark_rect.x = rect.x + rect.w

                # Update hint's index
                self.hints[i][1] += 1

            # Draw hint and bookmark
            display.blit(hint, rect)
            display.blit(self.bookmark_image, bookmark_rect)

    def handle_mousemotion(self):
        status, _, hitbox = self.button
        if status != 2:
            self.button[0] = 1 if self.mouse_ishover(hitbox) else 0

    def handle_mousebuttondown(self, mouse_pos):
        _, _, hitbox = self.button
        if hitbox.collidepoint(mouse_pos):
            for i, hint_data in enumerate(self.hints):
                if not hint_data[1]:  # is_showed
                    self.hints[i][0] = True  # idx
                    return
                
    def restart(self, hint1, hint2):
        self.init_bookmarks([hint1, hint2])