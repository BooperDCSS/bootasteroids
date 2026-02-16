import pygame
import circleshape
from constants import SHOT_RADIUS, LINE_WIDTH


class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        color = "white"
        pygame.draw.circle(
            screen, color, self.position, self.radius, LINE_WIDTH
        )

    def update(self, dt):
        self.position += self.velocity * dt
