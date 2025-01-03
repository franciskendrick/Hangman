from functions import clip_font_to_dict, palette_swap
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
        self.characters = {}
        self.order = [
            'A', 'B', 'C', 'D', 'E',
            'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y',
            'Z', '0', '1', '2', '3',
            '4', '5', '6', '7', '8',
            '9', '-', "'", ':', '_']
        fontset = pygame.image.load(f"{resources_path}/font.png")
        colors = {
            "red": (165, 48, 48),
            "green": (70, 130, 50),
        }

        # Color swap characters
        for color_name, color_rgb in colors.items():
            colorswapped_fontset = palette_swap(
                fontset.convert(), {(9, 10, 20): color_rgb})
            self.characters[color_name] = clip_font_to_dict(
                colorswapped_fontset, self.order)
        else:
            self.characters["black"] = clip_font_to_dict(
                fontset, self.order)

        # Spacing
        self.character_spacing = 1
        self.space = 3

    def render_font(self, display, text, pos, enlarge=1, color="black"):
        text = text.upper()
        display_handle = pygame.Surface(
            display.get_size(), pygame.SRCALPHA)
        x, y = pos
        x_offset = 0

        # Get Characters Color
        characters = self.characters[color]

        # Loop Over Every Character in Text
        for char in text:
            if char != " ":  # character
                # Get Character Image
                character = characters[char]

                # Resize Character Image
                wd, ht = character.get_size()
                resized_character = pygame.transform.scale(
                    character, (wd * enlarge, ht * enlarge))

                # Blit to Handle Display
                display_handle.blit(resized_character, (x + x_offset, y))

                # Add to Offset Width of Resized Character + Spacing
                x_offset += resized_character.get_width() + self.character_spacing
            else:  # space
                # Add to Offset Space Width + Spacing
                x_offset += self.space + self.character_spacing

        # Blit to Screen
        display.blit(display_handle, (0, 0))
