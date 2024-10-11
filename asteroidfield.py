
import pygame
import random
from asteroid import Asteroid
from constants import (
    ASTEROID_MAX_RADIUS,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    ASTEROID_SPAWN_RATE,
    ASTEROID_KINDS,
    ASTEROID_MIN_RADIUS,
)


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius: int, position: pygame.Vector2, velocity: pygame.Vector2):
        """
        Spawns a new asteroid with the specified radius, position, and velocity.

        Args:
            radius (int): The radius of the asteroid.
            position (pygame.Vector2): The position of the asteroid.
            velocity (pygame.Vector2): The velocity of the asteroid.

        Returns:
            None
        """
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity
        
    def update(self, dt: float) -> None:
        """
        Updates the asteroid field by incrementing the spawn timer and spawning a new asteroid if the timer exceeds the spawn rate.

        Args:
            dt (float): The time elapsed since the last update.

        Returns:
            None
        """
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
