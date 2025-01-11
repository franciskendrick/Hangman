from window import window
from ui import Font
import pygame

pygame.init()


class Word(Font):
    def __init__(self, word):
        super().__init__()

        self.word = word
        self.word_displayed = ["_" for _ in self.word]
        self.pos = self.get_pos()

    def draw(self, display):
        self.render_font(display, "".join(self.word_displayed), self.pos)

    def get_pos(self):
        wd, _ = self.get_size("".join(self.word_displayed))
        x = (window.rect.width - wd) / 2

        return (x, 40)

    def add_letter(self, letter):
        indexes = [index for index, char in enumerate(self.word) if char == letter]
        for index in indexes:
            self.word_displayed[index] = self.word[index]
