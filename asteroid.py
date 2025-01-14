from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Initialize the asteroid with position (x, y) and radius
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        # Draw the asteroid as a white circle on the given screen
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    def update(self, dt):
        # Update the position of the asteroid based on its velocity and the time delta
        self.position += self.velocity * dt
    
    def split(self):
        # Remove the current asteroid
        self.kill()
        
        # If the asteroid is too small, do not split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Calculate the angle for splitting and the radius of the new asteroids
        angle = random.uniform(20, 50)
        radius = self.radius - ASTEROID_MIN_RADIUS

        # Create the left asteroid with adjusted velocity
        left_asteroid = Asteroid(self.position[0], self.position[1], radius)
        left_asteroid.velocity = self.velocity.rotate(-angle) * 1.2

        # Create the right asteroid with adjusted velocity
        right_asteroid = Asteroid(self.position[0], self.position[1], radius)
        right_asteroid.velocity = self.velocity.rotate(angle) * 1.2