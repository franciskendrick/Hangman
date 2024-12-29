import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..", "..", "resources"
    )
)


class Font:
    def __init__(self):
        fontset = pygame.image.load(
            f"{resources_path}/font.png")
