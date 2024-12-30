from functions import separate_sets_from_xaxis, clip_set_to_list_on_xaxis
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..", "..", "resources"
    )
)


class Interactable:
    def __init__(self):
        spritesets = pygame.image.load(
            f"{resources_path}/interactables.png")
        
        order = ["hint", "bookmark", "restart", "keys"]
        self.spritesets = {
            name:clip_set_to_list_on_xaxis(spriteset) for (name, spriteset) in zip(order, separate_sets_from_xaxis(spritesets, (255, 0, 0)))}

    def mouse_ishover(self, hitbox):
        return True if hitbox.collidepoint(pygame.mouse.get_pos()) else False
