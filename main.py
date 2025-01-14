import sys
import pygame
from player import *
from asteroid import *
from constants import *
from asteroidfield import *
from shot import *

def main():
	# Initialize the pygame module
	pygame.init()

	# Create a clock object to manage the frame rate
	clock = pygame.time.Clock()
	dt = 0

	# Set up the display window with the specified width and height
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	# Create sprite groups for updatable and drawable objects as well as all asteroids and shots
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots,updatable,drawable)

	# Create a player object at the center of the screen
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

	# Create a asteroidfield object
	asteroidfield = AsteroidField()

	while True: # Game loop
		# Handle events in the event queue
		for event in pygame.event.get():
			# Exit the game loop if the quit event is triggered
			if event.type == pygame.QUIT:
				return
		
		# Update the position and state of every object that is updatable
		for obj in updatable:
			obj.update(dt)
		
		for asteroid in asteroids:
			# Check for collisions between the player and the asteroids and exit game if collision is detected
			if asteroid.collides_with(player):
				print("Game over!")
				sys.exit()
			
			# Check for collisions between the shots and the asteroids
			for shot in shots:
				if asteroid.collides_with(shot):
					shot.kill()
					asteroid.kill()

		# Fill the screen with black color
		pygame.Surface.fill(screen, (0, 0, 0))

		# Draw every drawable object on the screen
		for obj in drawable:
			obj.draw(screen)
		
		# Update the full display surface to the screen
		pygame.display.flip()
		
		# Cap the frame rate and calculate the time delta
		dt = clock.tick(MAX_FPS) / 1000

# Run the main function if this script is executed
if __name__ == "__main__":
	main()
