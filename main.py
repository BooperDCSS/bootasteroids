import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    pygame.init()

    # creating a time, dt = delta time

    clock = pygame.time.Clock()
    dt = 0
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player1.update(dt)
        player1.draw(screen)

        pygame.display.flip()

        # setting the refresh rate to 60 fps, divide by 1k to get milliseconds
        # clock.tick(60) doesn't return FPS, but time since last frame in
        # seconds, so divide by 1000 gives us seconds per frame

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
