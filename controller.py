import pygame
from environment import Environment
from gui import HealthBar, Text
from player import Player
from enemy import EnemyController
from menu import MainMenu, Options, Exit
from losescreen import LoseScreen
class GameState:
	def __init__(self, game_state, game):
		self.game_state = game_state
		self.game = game
		
	def goto_menu(self):
		self.game_state = MainMenu(self)

	def goto_options(self):
		self.game_state = Options(self)

	def goto_game(self):
		self.game_state = GameController(self)

	def exit_game(self):
		self.game.game_running = False

	def lose(self, score):
		self.game_state = LoseScreen(self, score)

	def render(self, surface):
		self.game_state.render(surface)
	
	def update(self, dt, event):
		self.game_state.update(dt, event)

class GameController:
	def __init__(self, game):
		self.game = game
		self.camera = Camera()
		self.environment = Environment(self.game)
		self.player = Player(10)
		self.enemy_controller = EnemyController(self.player, self.environment.trees, self.camera)
		self.camera.object = self.player
		self.health_bar = HealthBar()
		self.background = pygame.image.load('sprites/background.png')

	def render(self, surface):
		surface.blit(self.background, (0,0))
		self.environment.render(surface, self.camera.x)
		self.player.render(surface, self.camera.x)
		self.enemy_controller.render(surface, self.camera.x)
		self.health_bar.render(surface, 10, 10)

	def update(self, dt, event):
		self.environment.update(dt, self.player.timer.time)
		self.player.update(dt, event)
		self.enemy_controller.update(dt,event)
		self.camera.update(dt, event) 
		self.health_bar.health = self.environment.tree_health


class Camera:
	def __init__(self):
		self.x = 0
		self.object = None

	def update(self, dt, event):
		self.x = self.object.x - 1280/2 + self.object.width/2
