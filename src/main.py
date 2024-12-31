from window import window
from gallows import Gallows
from keys import Keys
from hint import Hint
import pygame
import sys


def redraw_game():
    display.fill((235, 237, 233))

    gallows.draw(display)
    keys.draw(display)
    hint.draw(display)

    # Blit to screen
    resized_display = pygame.transform.scale(display, win_size)
    win.blit(resized_display, (0, 0))

    pygame.display.update()


def game_loop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # TEMPORARY !!!
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    gallows.add_part()

            keys.handle_mouse(event)

        redraw_game()
        clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    pygame.init()

    # Initialize window
    win_size = (
        int(window.rect.width * window.enlarge),
        int(window.rect.height * window.enlarge))
    win = pygame.display.set_mode(win_size)
    display = pygame.Surface(window.rect.size)
    pygame.display.set_caption("Hangman")
    clock = pygame.time.Clock()

    # Initialize objects
    gallows = Gallows()
    keys = Keys()
    hint = Hint()

    game_loop()
