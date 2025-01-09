from window import window
from ui import Font
import pygame

pygame.init()


class Word(Font):
    def __init__(self, word):
        super().__init__()

        self.word = word
        self.pos = self.get_pos()

    def draw(self, display):
        self.render_font(display, self.word, self.pos)

    def get_pos(self):
        wd, _ = self.get_size(self.word)
        x = (window.rect.width - wd) / 2

        return (x, 40)