import pygame
from constants import *
from circleshape import CircleShape
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,'red', self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        
        split_angle = uniform(20,50)

        new_velocity_pos = self.velocity.rotate(split_angle)
        new_velocity_neg = self.velocity.rotate(-split_angle)

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)

        new_asteroid_1.velocity = new_velocity_pos * 1.2
        new_asteroid_2.velocity = new_velocity_neg * 1.2