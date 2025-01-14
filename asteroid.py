from circleshape import *

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