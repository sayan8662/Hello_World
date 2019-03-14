import pygame
import random
import sys

pygame.init()

width = 500
height = 500
RED= (251,13,72)													# color with it's R G B value
GREEN = (70,251,147)												# color with it's R G B value
BLACK = (0,0,0)														# color with it's R G B value
YELLOW = (255, 255, 0)												# color with it's R G B value

player_size = 25													# can change PLAYER SIZE later
player_pos = [width/2, height-1.5*player_size]

obstacle_size = 25													# can change the  OBSTACLE SIZE  later
obstacle_pos = [random.randint(0, width - obstacle_size), 0]
obstacle_list = [obstacle_pos]

SPEED = 20

screen = pygame.display.set_mode((width,height))

game_over = False

score = 0

clock = pygame.time.Clock()

background_image = pygame.image.load("square.jpg").convert()				# adding BACKGROUND IMAGE in GAME

myFont = pygame.font.SysFont("monospace", 20)						# creating font for the SCORE

def set_level(score, SPEED):										# addition of LEVEL
	if score < 50:
		SPEED = 20

	elif score < 100 :
		SPEED = 25

	elif score < 150 :
		SPEED = 30

	elif score < 200 :
		SPEED = 35 

	elif score < 250 :
		SPEED = 40

	elif score < 300 :
		SPEED = 45

	elif score < 350 :
		SPEED = 48

	else:
		SPEED = 53

	return SPEED

def drop_obstacles(obstacle_list):
	delay = random.random()

	if len(obstacle_list) < 30 and delay < 0.3 :					# can CHANGE the falling SPEED and OBSTACLE NUMBERS manually
		x_pos = random.randint(0, width - obstacle_size)
		y_pos = 0
		obstacle_list.append([x_pos, y_pos])

def draw_obstacles(obstacle_list):
	for obstacle_pos in obstacle_list:
		pygame.draw.rect(screen, GREEN, (obstacle_pos[0], obstacle_pos[1], obstacle_size, obstacle_size ))	#  can create any SHAPE latter

def update_obstacle_positions(obstacle_list, score):
	for idx, obstacle_pos in enumerate(obstacle_list):				# UPDATING the OBSTACLE position
		if obstacle_pos[1] >= 0 and obstacle_pos[1] < height :
			obstacle_pos[1] += SPEED
		
		else:
			obstacle_list.pop(idx)
			score += 1 
	return score

def collision_check(obstacle_list, player_pos):						# checks the COLLISION with the enemy in the game
	for obstacle_pos in obstacle_list:
		if detect_collision(obstacle_pos, player_pos):
			return True
	return False		


def detect_collision(player_pos, obstacle_pos):						# detects the COLLISION with the enemy in the game 
	p_x = player_pos[0]
	p_y = player_pos[1]

	obstacle_x = obstacle_pos[0]
	obstacle_y = obstacle_pos[1]

	if (obstacle_x >= p_x and obstacle_x < (p_x + player_size)) or (p_x >= obstacle_x and p_x < (obstacle_x + player_size)) :
															# ( LOGIC for COLLISION in X axis )

		if(obstacle_y >= p_y and obstacle_y < (p_y + player_size)) or (p_y >= obstacle_y and p_y < (obstacle_y + player_size)) :
															# ( LOGIC for COLLISION in Y axis )
			return True

	return False		


game_over = False											#  initializing GAME OVER condition


#------------- MAIN PROGRAM LOOP ----------------
while not game_over:

	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:						#  can create any SHAPE latter
			sys.exit()
		if event.type == pygame.KEYDOWN :
			
			x = player_pos[0]
			y = player_pos[1]

			if event.key == pygame.K_LEFT :					#  will try to make the player move by holding the ARROW KEY 
				x -= player_size                        

			elif event.key == pygame.K_RIGHT :				#							"
				x += player_size						

			#elif event.key == pygame.K_UP :				#							"
			#	y -= player_size

			#elif event.key == pygame.K_DOWN :				#							"
			#	y += player_size
 
			player_pos = [x,y]		

	#screen.fill(BLACK)

	screen.blit(background_image, [0, 0])
		
	drop_obstacles(obstacle_list)								# calling of the DROP_OBSTACLE function
	score = update_obstacle_positions(obstacle_list, score)		# calling of the UPDATE_OBSTACLE_POSITIONS functions
	SPEED = set_level(score, SPEED)								# calling of the SET_LEVEL function
	
	text = "Score :" + str(score)
	label = myFont.render(text, 1 , YELLOW)
	screen.blit(label, (width-150, height-40))					# can CHANGE the SCORE msg LATER

	if collision_check(obstacle_list, player_pos):
		game_over = True
		
		

	draw_obstacles(obstacle_list)
	pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size)) 	
																# can create any SHAPE of the PLAYER latter

	clock.tick(10)

	pygame.display.update()


	#............................. THANK YOU ..................................
	#		...........................................................
	#				.....................................powered by SAYAN KUMAR NANDI :)