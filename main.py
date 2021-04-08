import pygame
import sys
from objects import *

pygame.init()

BLACK = (0, 0, 0)
WIDTH, HEIGHT = 1000, 700
SIDE = (WIDTH, HEIGHT)

# ventana
venatana = pygame.display.set_mode(SIDE)
CLOCK = pygame.time.Clock()

# sprites
sprite_list = pygame.sprite.Group()
# juagdor
player_list = pygame.sprite.Group()
player = Player()
player.rect.y = 600
player.rect.x = 400
player_list.add(player)
sprite_list.add(player)
life_player=7
Font=pygame.font.Font(None, 35)
# nave villano
nave_list = pygame.sprite.Group()

# laser
laser_list = pygame.sprite.Group()

for i in range(50, 900, 100):
	for j in range(50, 300, 100):
		nave = Nave(j, i)
		sprite_list.add(nave)
		nave_list.add(nave)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.velocidad = -3
			if event.key == pygame.K_RIGHT:
				player.velocidad = 3
			if event.key == pygame.K_SPACE:
				laser = Laser()
				sprite_list.add(laser)
				laser_list.add(laser)
				laser.rect.x = player.rect.x+46
				laser.rect.y = player.rect.y

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.velocidad = 0
			if event.key == pygame.K_RIGHT:
				player.velocidad = 0

	collision_list=pygame.sprite.spritecollide(player, nave_list, True)
	for collision in collision_list:
		life_player-=1

	for laser in laser_list:
		nave_list_colicion=pygame.sprite.spritecollide(laser, nave_list, True)
		if laser.rect.y<0:
			laser_list.remove(laser)

	# nave final
	if len(nave_list) == 0:
		villano=Villano()
		sprite_list.add(villano)
		villano.rect.x=500
		villano.rect.y=20

	venatana.fill(BLACK)
	# pintando texto de vida
	text=Font.render(f'life: {life_player}/7', True, (255, 255, 255))
	venatana.blit(text, (700, 20))
	sprite_list.update()
	sprite_list.draw(venatana)
	pygame.display.flip()
	CLOCK.tick(80)