import pygame

pygame.init()

BLACK=(0, 0, 0)
WIDTH=950

# jugador
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image=pygame.image.load('img/player.png')
		self.image.set_colorkey(BLACK)
		self.rect=self.image.get_rect()
		self.velocidad=0
		
	def update(self):
		self.rect.x+=self.velocidad
		if self.rect.x>WIDTH or self.rect.x<0:
			self.velocidad*=-1

class Nave(pygame.sprite.Sprite):
	def __init__(self, y, x):
		super().__init__()
		self.image=pygame.image.load('img/nave.png')
		self.image.set_colorkey(BLACK)
		self.rect=self.image.get_rect()
		self.rect.y=y
		self.rect.x=x
		self.velocidad=1

	def update(self):
		self.rect.y+=1
		self.rect.x+=self.velocidad
		
		if self.rect.x >WIDTH or self.rect.x<0:
			self.velocidad*=-1

		if self.rect.y>700:
			for i in range(100, 300, 100):
				self.rect.y=i

class Laser(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image=pygame.image.load('img/laser.png')
		self.image.set_colorkey(BLACK)
		self.rect=self.image.get_rect()
		self.sound=pygame.mixer.Sound('laser.ogg')
		self.sound.play()

	def update(self):
		self.rect.y-=3

class Villano(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image=pygame.image.load('img/villano.png')
		self.image.set_colorkey(BLACK)
		self.rect=self.image.get_rect()
		self.velocidad=3

	def update(self):
		self.rect.x+=self.velocidad
		if self.rect.x<0 or self.rect.x>WIDTH:
			self.velocidad*=-1