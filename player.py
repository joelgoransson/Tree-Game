import pygame
from environment import Tree
from random import choice
class Player:
	def __init__(self, x):
		self.sprites = [pygame.image.load('sprites/player_1.png'), pygame.image.load('sprites/player_2.png')]
		self.rotation = 1
		self.image_index = 0
		self.width, self.height = self.sprites[0].get_size()
		self.x = x
		self.walking_speed = 300
		self.y = 696 - self.height
		self.vy = 0
		self.jump_speed = 1000
		self.birdpoops = []
		self.timer = Timer()

	def render(self, surface, camera_x):
		surface.blit(self.sprites[round(self.image_index)], (self.x - camera_x,self.y))
		for birdpoop in self.birdpoops:
			birdpoop.render(surface, camera_x)
		self.timer.render(surface)


	def update(self, dt, event):
		if event.key_down(pygame.K_d):
			self.x += self.walking_speed * dt
			if self.rotation != 0:
				self.rotation = 0
				for index, sprite in enumerate(self.sprites):
					self.sprites[index] = pygame.transform.flip(sprite, -1, 0)

		if event.key_down(pygame.K_a):
			self.x -= self.walking_speed * dt
			if self.rotation != 1:
				self.rotation = 1
				for index, sprite in enumerate(self.sprites):
					self.sprites[index] = pygame.transform.flip(sprite, -1, 0)

		if event.key_down(pygame.K_SPACE):
			self.vy = -500
		if event.key_press(pygame.K_f):
			self.birdpoops.append(Birdpoop(self.x + self.width * self.rotation, self.y + self.height/2))

		self.vy += self.jump_speed * dt
		self.y += self.vy * dt 
		self.image_index += 5 * dt
		if self.image_index > 1:
			self.image_index = 0
		if self.y >= 696 - self.height:
			self.vy = 0
			self.y = 696 - self.height
			self.image_index = 0

		for birdpoop in self.birdpoops:
			birdpoop.update(dt)
		self.timer.update(dt, event)

class Birdpoop:
	def __init__(self, x, y):
		self.x = x 
		self.y = y
		self.sprite = pygame.image.load('sprites/birdpoop.png')
		self.width, self.height = self.sprite.get_size()

	def update(self, dt):
		self.y += 200 * dt

	def render(self, surface, camera_x):
		surface.blit(self.sprite, (self.x - camera_x, self.y))

class Timer:
	def __init__(self):
		self.font = pygame.font.Font('fonts/JewliScript1.ttf', 40)
		self.time = 0

	def render(self, surface):
		text = self.font.render(str(round(self.time)), 0, (0,0,0))
		surface.blit(text, (1280/2 - text.get_size()[0]/2, 10))		

	def update(self, dt, event):
		self.time += 1 * dt