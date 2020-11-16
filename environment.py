import pygame
from random import choice
from gui import HealthBar
class Environment:
	def __init__(self, game):
		self.total_trees = 4
		self.trees = []
		tree_co = -(self.total_trees/2) * 350
		for tree in range(self.total_trees):
			ye = choice([300, 350, 400])
			tree_co += ye
			self.trees.append(Tree(tree_co))
		self.tree_health = 1
		self.game = game

	def calculate_health(self):
		value = 0
		for tree in self.trees:
			value += tree.health
		self.tree_health = value / self.total_trees / 10

	def render(self, surface, camera_x):
		for tree in self.trees:
			tree.render(surface, camera_x)

	def update(self, dt, score):
		delete = []
		for tree in self.trees:
			tree.update(dt)
			if tree.health < 0:
				delete.append(tree)
		for tree in delete:
			del self.trees[self.trees.index(tree)]
		self.calculate_health()
		if self.tree_health <= 0:
			self.game.lose(score)

class Tree:
	def __init__(self, x):
		self.x = x
		self.image = pygame.image.load('sprites/tree.png')
		self.sprite = self.image
		self.width, self.height = self.sprite.get_size()
		self.y = 696 - self.height
		self.destroy = 0
		self.health_bar = HealthBar()
		self.health = 10
		self.total_health = 10

	def render(self, surface, camera_x):
		surface.blit(self.sprite, (self.x - camera_x, self.y))
		self.health_bar.render(surface, self.x - camera_x + 25, self.y - 30, self.width - 50)

	def update(self, dt):
		self.health_bar.health = self.health/self.total_health