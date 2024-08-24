import pygame
from constants import *
from player import *


def main():
    numpass, numfail = pygame.init()
    clk = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Initialize with black color
        screen.fill(pygame.color.Color(0, 0, 0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        time_passed = clk.tick(60)
        dt = time_passed / 1000


if __name__ == '__main__':
    main()
