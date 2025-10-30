import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255, 255, 255, 255), self.position, self.radius, 2)
        pass

    def update(self, dt):
        self.position += self.velocity * dt
        pass

    def split(self):
        self.kill()
        if(self.radius < ASTEROID_MIN_RADIUS):
            return
        spawn_angle = random.uniform(20, 50)
        spawn_vec1 = self.velocity.rotate(spawn_angle)
        spawn_vec2 = self.velocity.rotate(-spawn_angle)
        spawn_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, spawn_radius)
        asteroid1.velocity = spawn_vec1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, spawn_radius)
        asteroid2.velocity = spawn_vec2 * 1.2
        pass