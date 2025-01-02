from functions import separate_sets_from_xaxis, clip_set_to_list_on_xaxis
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..", "resources"
    )
)


class Gallows:
    def __init__(self):
        self.init_gallows()
        self.init_man()

    def init_gallows(self):
        gallows_img = pygame.image.load(f"{resources_path}/gallows.png")
        gallows_rect = pygame.Rect(47, 0, 56, 38)
        self.gallows = [gallows_img, gallows_rect]

    def init_man(self):
        # The order determines the drawing sequence
        self.order = ["head", "body", "left_arm", "right_arm", "left_leg", "right_leg", "frown", "smile"]
        man_spritesets = separate_sets_from_xaxis(
            pygame.image.load(f"{resources_path}/man.png"), (255, 0, 0))
        coordinates = [
            (63, 8),
            (67, 17),
            (64, 19),
            (68, 19),
            (63, 26),
            (68, 26),
            (63, 8),
            (65, 10)
        ]

        self.man = {}
        for name, man_spriteset, coords in zip(self.order, man_spritesets, coordinates):
            spriteset = clip_set_to_list_on_xaxis(man_spriteset)
            wd, ht = spriteset[0].get_size()
            self.man[name] = [spriteset, pygame.Rect(*coords, wd, ht)]

        self.life = -1
        self.idx = 0

    def draw(self, display):
        # Draw gallows
        display.blit(*self.gallows)

        # Draw visible parts of the man
        for i in range(self.life):
            part_name = self.order[i]
            spriteset, rect = self.man[part_name]
            display.blit(spriteset[-1], rect)
        
        if self.life >= 0:
            part_name = self.order[self.life]
            spriteset, rect = self.man[part_name]

            display.blit(spriteset[self.idx // 4], rect)

            limit = (len(spriteset) - 1) * 4
            if self.idx >= limit:
                self.idx = limit
            else:
                self.idx += 1

    def add_part(self, num=1):
        if self.life < len(self.order):
            self.life += num
            self.idx = 0

    def restart(self):
        self.life = -1
