import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.x = self.position.x
        self.y = self.position.y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255, 255, 255), (self.position.x, self.position.y), self.radius, SHOT_RADIUS)

    def update(self, dt):
        self.position += (self.velocity * dt)
