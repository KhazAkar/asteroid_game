from abc import ABC, abstractmethod
import pygame


class CircleShape(ABC, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collision_check(self, other: 'CircleShape') -> bool:
        if not isinstance(other, CircleShape):
            raise ValueError("Variable 'other' must be an instance of CircleShape class")
        return self.position.distance_to(other.position) <= self.radius + other.radius

    @abstractmethod
    def draw(self, screen) -> bool:
        # sub-classes must override
        pass

    @abstractmethod
    def update(self, dt):
        # sub-classes must override
        pass
