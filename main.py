import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

class Game:
    def __init__(self) -> None:
        """
        Initializes a new instance of the Game class, setting up the necessary groups for updatable and drawable game elements, 
        and initializing the game's screen, player, asteroid field, and clock.
        """
        self.updatable: pygame.sprite.Group = pygame.sprite.Group()
        self.drawable: pygame.sprite.Group = pygame.sprite.Group()
        self.asteroids: pygame.sprite.Group = pygame.sprite.Group()
        AsteroidField.containers = (self.updatable, )
        Asteroid.containers = (self.updatable, self.drawable, self.asteroids)
        Player.containers = (self.updatable, self.drawable)
        self.screen: pygame.Surface = None
        self.player: Player = None
        self.asteroidfield: AsteroidField = None
        self.clock: pygame.time.Clock = None

    def initialize(self) -> None:
        """
        Initializes the game by setting up the Pygame environment, creating a game screen, 
        spawning a player at the center of the screen, creating an asteroid field, and 
        initializing a clock to control the game's framerate.

        Args:
            None

        Returns:
            None
        """
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.asteroidfield = AsteroidField()
        self.clock = pygame.time.Clock()

    def handle_events(self) -> bool:
        """
        Handles the game's events, including the QUIT event.

        Args:
            None

        Returns:
            bool: False if the QUIT event is detected, True otherwise.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def update(self, dt: float) -> bool:
        """
        Updates the game state by updating all updatable elements and checking for collisions between the player and asteroids.

        Args:
            dt (float): The time elapsed since the last update.

        Returns:
            bool: False if a collision is detected, True otherwise.
        """
        for updatable_element in self.updatable:
            updatable_element.update(dt)

        # Check for collisions between the player and the asteroids
        for asteroid in self.asteroids:
            if self.player.collision_check(asteroid):
                return False

        return True

    def draw(self) -> None:
        """
        Draws the current game state by filling the screen with a black color, 
        drawing all drawable elements, and updating the display.

        Args:
            None

        Returns:
            None
        """
        self.screen.fill(pygame.color.Color(0, 0, 0))
        for drawable_element in self.drawable:
            drawable_element.draw(self.screen)
        pygame.display.flip()

    def run(self) -> None:
        """
        Runs the main game loop, initializing the game, handling events, updating the game state, and drawing the game screen.
        
        This function continues to run until the game is quit or a game over condition is met.
        
        Args:
            None
        
        Returns:
            None
        """
        self.initialize()
        dt = 0.0
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

def main() -> None:
    game = Game()
    game.run()

if __name__ == '__main__':
    main()