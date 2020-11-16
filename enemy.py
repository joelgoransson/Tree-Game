import pygame
from gui import HealthBar
from random import choice, randint
class EnemyController:
	def __init__(self, player, trees, camera):
		self.trees = trees
		self.player = player
		self.camera = camera
		self.map_start, self.map_end = None, None
		for tree in trees:
			if self.map_start == None or self.map_start == None:
				self.map_start = tree.x
				self.map_end = tree.y
			else:
				if abs(tree.x) < abs(self.map_start):
					self.map_start = tree.x
				if abs(tree.x) > abs(self.map_end):
					self.map_end = tree.x
		self.map_start -= 1000
		self.map_end += 500
		self.enemies = [] 
		self.spawn_enemy(trees)

	def spawn_enemy(self, trees):
		if randint(0, 2):
			spawn_co = self.map_start
		else:
			spawn_co = self.map_end
		self.enemies.append(Enemy(spawn_co, trees))  


	def update(self, dt, event):
		for enemy in self.enemies:
			enemy.update(dt, event)
			if enemy.sad and enemy.x > 1280 + self.camera.x:
				del self.enemies[self.enemies.index(enemy)]
		self.birdpoop_collision()
		if len(self.enemies) == 1 and len(self.trees) == 1:
			self.spawn_enemy(self.trees)

	def render(self, surface, camera_x):
		for enemy in self.enemies:
			enemy.render(surface, camera_x)

	def birdpoop_collision(self):
		birdpoops = []
		for birdpoop in self.player.birdpoops:
			birdpoops.append(pygame.Rect(birdpoop.x, birdpoop.y, birdpoop.width, birdpoop.height))

		found = False
		for enemy in self.enemies:
			hits = [enemy.rect_head.collidelistall(birdpoops), enemy.rect_body.collidelistall(birdpoops)]
			for index, hit in enumerate(hits):
				if hit:
					del self.player.birdpoops[birdpoops.index(birdpoops[hit[0]])]
					if index == 0:
						enemy.health -= 4
					else:
						enemy.health -= 2
					if enemy.health <= 0:
						if enemy.sad == False:
							self.spawn_enemy(self.trees)
						enemy.make_sad()
					found = True
					break
			if found:
				break

class Enemy:
	def __init__(self, x, trees):
		self.trees = trees
		self.sprite = pygame.image.load("sprites/enemy.png")
		self.width, self.height = self.sprite.get_size()
		self.y = 696 - self.height
		self.x = x
		self.speed = 200
		self.search_for_tree()
		self.health_bar = HealthBar()
		self.health = 10
		self.total_health = 10
		self.rect_head = pygame.Rect(self.x + 32, self.y, 36, self.height)
		self.rect_body = pygame.Rect(self.x, self.y + 51, self.width, self.height)
		self.sad = False
		self.chainsaw = Chainsaw()

	def search_for_tree(self):
		self.nearest_tree = None
		if self.trees:
			for tree in self.trees:
				if self.nearest_tree == None:
					self.nearest_tree = tree
				else:
					if abs(tree.x - self.x) < abs(self.nearest_tree.x - self.x):
						self.nearest_tree = tree
		else:
			return None
	
	def make_sad(self):
		self.health = 0
		self.sad = True
		self.sprite = pygame.image.load('sprites/enemy_sad.png')
		self.health_bar.health = 0


	def render(self, surface, camera_x):
		surface.blit(self.sprite, (self.x - camera_x,self.y))
		self.health_bar.render(surface, self.x - camera_x, self.y - 30, self.width)
		self.chainsaw.render(surface, self.x - camera_x + 92, self.y + 130)

	def update(self, dt, event):
		if self.sad:
			self.x += 350 * dt
			return

		if self.nearest_tree != None:
			if self.nearest_tree.x < self.x:
				self.x -= self.speed * dt
			elif self.nearest_tree.x > self.x:
				self.x += self.speed * dt
			if abs(self.x - self.nearest_tree.x) < self.speed * dt:
				self.x = self.nearest_tree.x
				self.nearest_tree.health -= 2 * dt
				if self.nearest_tree.health < 0:
					self.nearest_tree = None
		else:
			self.search_for_tree()
		self.health_bar.health = self.health/self.total_health

		self.rect_head = pygame.Rect(self.x + 32, self.y, 36, self.height)
		self.rect_body = pygame.Rect(self.x, self.y + 51, self.width, self.height)

class Chainsaw:
	def __init__(self):
		self.sprite = pygame.image.load('sprites/chainsaw.png')

	def render(self, surface, x,y):
		surface.blit(self.sprite, (x,y))