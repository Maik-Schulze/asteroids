from circleshape import *
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        # Initialize the Shot object with position (x, y) and a predefined radius
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        # Draw the shot as a circle on the given screen with white color and a border width of 2
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    def update(self, dt):
        # Update the position of the shot based on its velocity and the time delta
        self.position += self.velocity * dt