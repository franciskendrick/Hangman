from window import window
from gallows import Gallows
from keys import Keys
from hint import Hint
from restart import Restart
import pygame
import sys


def redraw_game():
    display.fill((235, 237, 233))

    gallows.draw(display)
    keys.draw(display)
    hint.draw(display)
    if gallows.life == 6:
        restart.draw(display)

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

            keys.handle_mousemotion(event)

            if gallows.life == 6:
                if restart.handle_mouse(event):
                    gallows.restart()
                    keys.restart()

        if gallows.life < 6:
            key_pressed = keys.handle_mousebuttondown()

            if key_pressed != None:
                if key_pressed in word:
                    pass
                else:
                    gallows.add_part()
                    if gallows.life == 6:
                        print("YOU LOST")
                        # NOTE: restart button will appear

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
    restart = Restart()
    word = "PLUTO"  # TEMPORARY !!!

    game_loop()
