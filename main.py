import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

class Game:
    def __init__(self):
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        AsteroidField.containers = (self.updatable, )
        Asteroid.containers = (self.updatable, self.drawable, self.asteroids)
        Player.containers = (self.updatable, self.drawable)
        self.screen = None
        self.player = None
        self.asteroidfield = None
        self.clock = None

    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.asteroidfield = AsteroidField()
        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def update(self, dt):
        for updatable_element in self.updatable:
            updatable_element.update(dt)

        # Check for collisions between the player and the asteroids
        for asteroid in self.asteroids:
            if self.player.collision_check(asteroid):
                return False

        return True

    def draw(self):
        self.screen.fill(pygame.color.Color(0, 0, 0))
        for drawable_element in self.drawable:
            drawable_element.draw(self.screen)
        pygame.display.flip()

    def run(self):
        self.initialize()
        dt = 0
        while True:
            if not self.handle_events():
                break
            if not self.update(dt):
                print("Game Over!")
                break
            self.draw()
            time_passed = self.clock.tick(60)
            dt = time_passed / 1000

        pygame.quit()

def main():
    game = Game()
    game.run()

if __name__ == '__main__':
    main()