import pygame
import os

WIDTH, HEIGHT = 900, 600

WHITE = (255, 255, 255)

WIN = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)
PLAYER1 = pygame.Rect(50, HEIGHT/2 - 50, 10, 100)
PLAYER2 = pygame.Rect(WIDTH - 50, HEIGHT/2 - 50, 10, 100)

def draw_window():
	pygame.draw.rect(WIN, WHITE, PLAYER1)
	pygame.draw.rect(WIN, WHITE, PLAYER2)
	pygame.display.update()

def main():
	run = True
	
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		draw_window()

	pygame.quit()

if __name__ == "__main__":
	main()