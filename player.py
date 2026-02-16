import pygame
import circleshape
from constants import (
    PLAYER_RADIUS,
    LINE_WIDTH,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
)
from shot import Shot


class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = (
            pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        )
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        points = self.triangle()
        color = "white"
        pygame.draw.polygon(screen, color, points, LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    # if the cooldown timer is greater than 0, do nothing
    # otherwise, set the cooldown timer to the CONSTANT and then draw bullet
    def shoot(self):
        if self.cooldown_timer > 0:
            return

        self.cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        bullet = Shot(self.position.x, self.position.y)
        shot_vector = pygame.Vector2(0, 1)
        rotated_shot = shot_vector.rotate(self.rotation)
        rotated_with_speed_shot = rotated_shot * PLAYER_SHOOT_SPEED
        bullet.velocity += rotated_with_speed_shot

    # note that the cooldown timer can go below 0, but it doesn't matter
    # because we always set it to the PLAYER_SHOOT_COOLDOWN_SECONDS constant
    # if the timer is < 0, we can still shoot
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cooldown_timer -= dt

        # movement forward and backward
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        # rotation left and right
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # fire!
        if keys[pygame.K_SPACE]:
            self.shoot()
