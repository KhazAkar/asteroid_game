import pygame
from constants import *


def main():
    numpass, numfail = pygame.init()
    clk = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Initialize with black color
        screen.fill(pygame.color.Color(0, 0, 0))
        pygame.display.flip()
        time_passed = clk.tick(60)
        dt = time_passed / 1000

if __name__ == '__main__':
    main()
