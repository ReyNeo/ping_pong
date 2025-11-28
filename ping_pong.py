from pygame import *
from helper import GameRectangle
from pygame.sprite import collide_rect
font.init()
					#x   y
window_resolution = (1000,500)
FPS = 60
speed = 5
window = display.set_mode(window_resolution)
display.set_caption("ping pong")
clock = time.Clock()
player_1_counter = 0
player_2_counter = 0
pong_y_speed = speed
pong_x_speed = speed

background = GameRectangle (0,0,window_resolution[0],window_resolution[1],(0,0,0))
player_1 = GameRectangle(40,100,10,100,(255,255,255))
player_2 = GameRectangle(window_resolution[0]-50,100,10,100,(255,255,255))
pong = GameRectangle(400,300,10,10,(255,255,255))
counter_font = font.Font(None,36)

MAINGAMELOOP = True
while MAINGAMELOOP:
	background.update(window)
	player_1.update(window)
	player_2.update(window)
	txt_player_1_counter = counter_font.render(str(player_1_counter),1,(255,255,255))
	window.blit(txt_player_1_counter,(window_resolution[0]//2 -30,5))
	txt_player_2_counter = counter_font.render(str(player_2_counter),1,(255,255,255))
	window.blit(txt_player_2_counter,(window_resolution[0]//2 +30,5))
	pong.y += pong_y_speed
	pong.x += pong_x_speed
	if pong.y < 0: pong_y_speed = speed
	elif pong.y > window_resolution[1]-pong.height: pong_y_speed = -speed

	pong.update(window)
	
	if collide_rect(pong,player_1) and pong_x_speed < 0:
		pong_x_speed = speed
	if collide_rect(pong,player_2) and pong_x_speed > 0:
		pong_x_speed = -speed

	if pong.x < 0 or pong.x > window_resolution[0]:
		if pong.x < 0: player_1_counter +=1 
		elif pong.x > window_resolution[0]: player_2_counter += 1
		pong.x = window_resolution[0] // 2
		pong.y = window_resolution[1] // 2
		pong_x_speed = -pong_x_speed


	for e in event.get():
		if e.type == QUIT:
			MAINGAMELOOP = False
	keys_pressed = key.get_pressed()
	if keys_pressed[K_w] and player_1.y > 0: player_1.y -= speed
	elif keys_pressed[K_s] and player_1.y < window_resolution[1]-player_1.height: player_1.y += speed
	elif keys_pressed[K_UP] and player_2.y > 0: player_2.y -= speed
	elif keys_pressed[K_DOWN] and player_2.y < window_resolution[1]-player_2.height: player_2.y += speed 

	display.update()
	clock.tick(FPS)