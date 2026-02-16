import pygame
import circleshape
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        new_angle = random.uniform(20, 50)
        asteroid1_vector = self.velocity.rotate(new_angle)
        asteroid2_vector = self.velocity.rotate(-new_angle)
        self.new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, self.new_radius)
        asteroid1.velocity = asteroid1_vector * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, self.new_radius)
        asteroid2.velocity = asteroid2_vector * 1.2

    def draw(self, screen):
        color = "white"
        pygame.draw.circle(
            screen, color, self.position, self.radius, LINE_WIDTH
        )

    def update(self, dt):
        self.position += self.velocity * dt
