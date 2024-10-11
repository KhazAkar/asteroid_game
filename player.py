import pygame
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    SHOT_RADIUS,
    PLAYER_SHOOT_SPEED,
)
from bullet import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen) -> bool:
        if pygame.draw.polygon(screen, pygame.Color(255, 255, 255), self.triangle(), 2):
            return True
        return False

    def rotate(self, dt: float):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float):
        """
        Update the player's position and orientation based on key inputs.

        Parameters:
            dt (float): Time elapsed since the last update in seconds.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if self.cooldown > 0.0:
            self.cooldown -= dt

    def move(self, dt: float):
        """
        Updates the player's position based on their rotation and speed.

        Parameters:
        - dt (float): The time delta between frames in seconds.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        bullet_position = self.position + pygame.Vector2(0, 1).rotate(self.rotation) * (
            self.radius + (2 * SHOT_RADIUS)
        )
        bullet = Shot(bullet_position.x, bullet_position.y, SHOT_RADIUS)
        bullet.velocity = (
            pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        )
        return bullet
