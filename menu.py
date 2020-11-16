from gui import Text
import pygame
class MainMenu():
	def __init__(self, game):
		self.game = game
		self.objects = {"New Game":self.game.goto_game, "Options": self.game.goto_options, "Exit":self.game.exit_game}
		texts = ["New Game", "Options", "Exit"]
		self.texts = []
		for text in texts:
			self.texts.append(Text(text, 60, (255, 255, 255)))
		self.background = pygame.image.load('sprites/background_menu.png')
		self.game_name = Text("Nature Strikes Back", 100, (0, 255, 0))
		self.game_name2 = Text("Woodcutters Gaiden:", 140, (0, 255, 0))		

	def render(self, surface):
		surface.blit(self.background, (0,0))
		y = 720 - len(self.texts) * 60
		for index, text in enumerate(self.texts):
			text.render(surface, 10, y + 60 * index)
		self.game_name2.render(surface, 1280/2 - self.game_name2.width/2, 100)
		self.game_name.render(surface, 1280/2 - self.game_name.width/2, 200)

	def update(self, dt, event):
		y = 720 - len(self.texts) * 60 
		for index, text in enumerate(self.texts):
			hover = text.mouse_hover(10, y + 60 * index) 
			if text.color == (0, 255, 0) and not hover:
				text.color = (255, 255, 255)
				text.render_text()
			if hover:
				text.color = (0,255,0)
				text.render_text()
				if event.mouse_press(0):
					self.objects[text.text]()
class Options:
	def __init__(self, game):
		self.game = game

	def render(self, surface):
		pass

	def update(self, dt, event):
		pass

class Exit:
	def __init__(self, game):
		game.exit_game()

	def render(self, surface):
		pass

	def update(self, dt, event):
		pass