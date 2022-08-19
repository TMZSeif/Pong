import pygame
import os
import random

WIDTH, HEIGHT = 900, 600
VEL = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PONG_DIRECTION_X = random.choice(["right", "left"])
PONG_DIRECTION_Y = random.randint(-HEIGHT, HEIGHT)

WIN = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)
PLAYER1 = pygame.Rect(50, HEIGHT/2 - 50, 10, 100)
PLAYER2 = pygame.Rect(WIDTH - 50, HEIGHT/2 - 50, 10, 100)
PONG_COORDS = [WIDTH/2, HEIGHT/2]

def draw_window():
	WIN.fill(BLACK)
	pygame.draw.rect(WIN, WHITE, PLAYER1)
	pygame.draw.rect(WIN, WHITE, PLAYER2)
	pong = pygame.draw.circle(WIN, WHITE, PONG_COORDS, 10)
	pygame.display.update()
	
def handle_pong_movement():
	if PONG_DIRECTION_X == "right":
		PONG_COORDS[0] += 3
		PONG_COORDS[1] +=  PONG_DIRECTION_Y / 200
	else:
		PONG_COORDS[0] -= 3
		PONG_COORDS[1] +=  PONG_DIRECTION_Y / 200

def handle_player1_movement(player1):
	keys_pressed = pygame.key.get_pressed()

	if keys_pressed[pygame.K_w] and player1.y - VEL >= 0:
		player1.y -= VEL
	if keys_pressed[pygame.K_s] and (player1.y + player1.height) + VEL <= HEIGHT:
		player1.y += VEL

def handle_player2_movement(player2):
	keys_pressed = pygame.key.get_pressed()

	if keys_pressed[pygame.K_UP] and player2.y - VEL >= 0:
		player2.y -= VEL
	if (keys_pressed[pygame.K_KP_2] or keys_pressed[pygame.K_DOWN]) and (player2.y + player2.height) + VEL <= HEIGHT:
		player2.y += VEL

def main():
	run = True
	clock = pygame.time.Clock()
	while run:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		handle_player1_movement(PLAYER1)
		handle_player2_movement(PLAYER2)
		handle_pong_movement()
		draw_window()

	pygame.quit()

if __name__ == "__main__":
	main()