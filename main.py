import pygame
import sys
from objects import *

pygame.init()

BLACK = (0, 0, 0)
WIDTH, HEIGHT = 1000, 700
SIDE = (WIDTH, HEIGHT)

# ventana
ventana = pygame.display.set_mode(SIDE)
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
Font=pygame.font.Font(None, 35)
# nave villano
villano=Villano()
nave_list = pygame.sprite.Group()
villano_list=pygame.sprite.Group()
villainSpawned = False
# laser
laser_list = pygame.sprite.Group()

def crear_naves():
    for i in range(50, 900, 100):
        for j in range(50, 300, 100):
            nave = Nave(j, i)
            sprite_list.add(nave)
            nave_list.add(nave)


crear_naves()
def decrement(lista,objeto):
    for i in lista:
        objeto-=1

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
    villano_list_collision=[]

    decrement(collision_list, player.vidas)
    # nave final
    if len(nave_list) == 0 and not villainSpawned:        
        villainSpawned = True
        villano_list.add(villano)
        sprite_list.add(villano)
        villano.rect.x=500
        villano.rect.y=20
        crear_naves()

    for laser in laser_list:
        nave_list_collsiion=pygame.sprite.spritecollide(laser, nave_list, True)
        villano_list_collision.append(pygame.sprite.spritecollide(laser, villano_list, False))
        if laser.rect.y<0:
            laser_list.remove(laser)            
    
    decrement(villano_list_collision, villano.vidas)

    if villano.vidas<0:
        villano_list_collision.dokill(True)
        sprite_list.remove(villano)
        vida_villano.remove(villano) 
        
    ventana.fill(BLACK)
    # pintando texto de vida
    text=Font.render(f'life: {player.vidas}/7', False, (255, 255, 255))
    text2=Font.render(f'life: {villano.vidas}/5', False, (255, 255, 255))
    ventana.blit(text, (700, 20))
    ventana.blit(text2, (20, 20))
    sprite_list.update()
    sprite_list.draw(ventana)
    pygame.display.flip()
    CLOCK.tick(80)