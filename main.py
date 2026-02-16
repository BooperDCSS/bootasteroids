import sys
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()

    # creating a time, dt = delta time
    clock = pygame.time.Clock()
    dt = 0

    # creating groups for easy update calls
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # adding classes to the groups using the containers language found in the
    # CircleShape module
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (shots, drawable, updatable)

    # creating a Player and AsteroidField instance
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)

        for rock in asteroids:
            if rock.collides_with(player1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        # setting the refresh rate to 60 fps, divide by 1k to get milliseconds
        # clock.tick(60) doesn't return FPS, but time since last frame in
        # seconds, so divide by 1000 gives us seconds per frame

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
