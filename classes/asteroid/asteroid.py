import random

import pygame.draw

from classes.circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return
        random_angle = random.uniform(20,50)
        self.__create_asteroid(random_angle)
        self.__create_asteroid(-random_angle)

    def __create_asteroid(self, angle):
        vector = self.velocity.rotate(angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, radius)
        asteroid.velocity = vector * 1.2