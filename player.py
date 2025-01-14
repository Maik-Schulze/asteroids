import pygame
from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Initialize the player's rotation angle
    
    def triangle(self):
        # Calculate the vertices of the player's triangular shape
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # Draw the player's triangular shape on the screen
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)
    
    def rotate(self, dt):
        # Rotate the player based on the elapsed time and turn speed
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        # Update the player's state based on keyboard input
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate left
        if keys[pygame.K_d]:
            self.rotate(dt)  # Rotate right