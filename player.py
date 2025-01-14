import pygame
from circleshape import *
from shot import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0   # Initialize the player's rotation angle
        self.timer = 0      # Initialize the player's shot timer
    
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

    def move(self, dt):
        # Move the player based on the elapsed time and move speed
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0: return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        # Create a new shot object at the player's current position
        shot = Shot(self.position[0], self.position[1])
        # Set the shot's velocity based on the player's current rotation and shoot speed
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN


    def update(self, dt):
        # Update the player's state based on keyboard input
        keys = pygame.key.get_pressed()

        # Decrease the player's shot timer by the elapsed time 
        self.timer -= dt

        if keys[pygame.K_w]:
            self.move(dt)       # Move forwards
        if keys[pygame.K_s]:
            self.move(-dt)      # Move backwards
        if keys[pygame.K_a]:
            self.rotate(-dt)    # Rotate left
        if keys[pygame.K_d]:
            self.rotate(dt)     # Rotate right
        if keys[pygame.K_SPACE]:
            self.shoot()