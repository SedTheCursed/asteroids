# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame

from classes.asteroid.asteroid import Asteroid
from classes.asteroid.asteroidfield import AsteroidField
from classes.player.shot import Shot
from constants import *
from classes.player.player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, drawable,  updatable)
    Shot.containers = (shots, drawable, updatable)
    AsteroidField.containers = updatable
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for item in updatable: item.update(dt)
        for item in drawable: item.draw(screen)
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()
            if asteroid.check_collision(player):
                print("Game over!")
                exit(0)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()