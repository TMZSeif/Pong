import pygame
import os

WIDTH, HEIGHT = 600, 400

WIN = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)

def main():
	run = True
	
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

	pygame.quit()

if __name__ == "__main__":
	main()