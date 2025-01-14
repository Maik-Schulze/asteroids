import pygame
from constants import *

def main():
	# Initialize the pygame module
	pygame.init()

	# Create a clock object to manage the frame rate
	clock = pygame.time.Clock()
	dt = 0

	# Set up the display window with the specified width and height
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	while True: #game loop
		# Handle events in the event queue
		for event in pygame.event.get():
			# Exit the game loop if the quit event is triggered
			if event.type == pygame.QUIT:
				return
		
		# Fill the screen with black color
		pygame.Surface.fill(screen, (0, 0, 0))
		# Update the full display surface to the screen
		pygame.display.flip()
		
		# Cap the frame rate and calculate the time delta
		dt = clock.tick(MAX_FPS) / 1000

# Run the main function if this script is executed
if __name__ == "__main__":
	main()
