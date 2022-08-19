import pygame
import os
import random
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 600
VEL = 5
pong_vel = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pong_direction_x = random.choice(["right", "left"])
pong_direction_y = random.randint(-HEIGHT, HEIGHT)

WINNER_FONT = pygame.font.SysFont("aria", 100)
PLAYER1_WINS = pygame.event.Event(pygame.USEREVENT + 1)
PLAYER2_WINS = pygame.event.Event(pygame.USEREVENT + 2)

BOUNCE = pygame.mixer.Sound(os.path.join("Assets", "bounce.wav"))
BACKGROUND_MUSIC = pygame.mixer.Sound(os.path.join("Assets", "music.mp3"))
WIN_MUSIC = pygame.mixer.Sound(os.path.join("Assets", "win.mp3"))

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
	if pong_direction_x == "right":
		PONG_COORDS[0] += pong_vel
		PONG_COORDS[1] +=  pong_direction_y / 200
	else:
		PONG_COORDS[0] -= pong_vel
		PONG_COORDS[1] +=  pong_direction_y / 200

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

def handle_pong_collision(player1, player2):
	global pong_direction_x
	global pong_direction_y
	global pong_vel
	if PONG_COORDS[1] + 5 >= HEIGHT or PONG_COORDS[1] - 5 <= 0:
		pong_direction_y = -pong_direction_y
		pong_vel += pong_vel/10
		BOUNCE.play()
	if player1.collidepoint(PONG_COORDS[0] - 5, PONG_COORDS[1]):
		pong_direction_x = "right"
		pong_vel += pong_vel/10
		BOUNCE.play()
	if player2.collidepoint(PONG_COORDS[0] + 5, PONG_COORDS[1]):
		pong_direction_x = "left"
		pong_vel += pong_vel/10
		BOUNCE.play()

def handle_player2_wins(player1, player2):
	global PONG_COORDS
	if PONG_COORDS[0] + 5 <= 0:
		print("Player 2 Wins!")
		pygame.event.post(PLAYER2_WINS)
		PONG_COORDS = [WIDTH/2, HEIGHT/2]
		player1.x = 50
		player1.y = HEIGHT/2 - player1.height
		player2.x = WIDTH - 50
		player2.y = HEIGHT/2 - player2.height
		print("Player 2 Wins!")
		WIN_MUSIC.play()
		
		BACKGROUND_MUSIC.stop()
		return "player 2"

def handle_player1_wins(player1, player2):
	global PONG_COORDS
	if PONG_COORDS[0] - 5 >= WIDTH:
		print(PONG_COORDS)
		print("Player 1 Wins!")
		pygame.event.post(PLAYER1_WINS)
		PONG_COORDS = [WIDTH/2, HEIGHT/2]
		player1.x = 50
		player1.y = HEIGHT/2 - player1.height
		player2.x = WIDTH - 50
		player2.y = HEIGHT/2 - player2.height
		print("Player 1 Wins!")
		WIN_MUSIC.play()
		pygame.time.delay(700)
		WIN_MUSIC.stop()
		BACKGROUND_MUSIC.stop()
		return "player 1"

def main():
	run = True
	clock = pygame.time.Clock()
	BACKGROUND_MUSIC.play(-1)
	while run:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
			if event.type == PLAYER1_WINS:
				break
			if event.type == PLAYER2_WINS:
				break
		
		winner_text = ""
		
		if handle_player2_wins(PLAYER1, PLAYER2) == "player 2":
			print("Player 2 Wins!")
			winner_text = "Player 2 Wins!"
			winner_text = WINNER_FONT.render(winner_text, 1, WHITE)
			WIN.blit(winner_text, (WIDTH/2 - winner_text.get_width() /
						 2, HEIGHT/2 - winner_text.get_height()/2))
			pygame.display.update()
			pygame.time.delay(5000)
			break
		if handle_player1_wins(PLAYER1, PLAYER2) == "player 1":
			print("Player 1 Wins!")
			winner_text = "Player 1 Wins!"
			winner_text = WINNER_FONT.render(winner_text, 1, WHITE)
			WIN.blit(winner_text, (WIDTH/2 - winner_text.get_width() /
						 2, HEIGHT/2 - winner_text.get_height()/2))
			pygame.display.update()
			pygame.time.delay(5000)
			break

		handle_player1_movement(PLAYER1)
		handle_player2_movement(PLAYER2)
		handle_pong_collision(PLAYER1, PLAYER2)
		handle_pong_movement()
		draw_window()

	main()

if __name__ == "__main__":
	main()