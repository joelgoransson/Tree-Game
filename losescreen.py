from gui import Text
import pygame
class LoseScreen:
	def __init__(self, game, score):
		self.background = pygame.image.load("sprites/background_lose.png")
		self.game = game
		self.text = Text("Now these birds dont have anywhere to live!", 70, (0,0,0))
		self.text2 = Text("Think before you kill trees!", 70, (0,0,0))
		self.menu = Text("Menu", 60, (255, 255, 255))
		self.play_again = Text("Play Again", 60, (255, 255, 255))
		self.score = Text("Time: " + str(int(score)), 60, (255, 255, 255))

	def render(self, surface):
		surface.blit(self.background, (0,0))
		self.text.render(surface, 1280/2 - self.text.width/2, 10)
		self.text2.render(surface, 1280/2 - self.text2.width/2, 60)
		self.menu.render(surface, 10, 640)
		self.play_again.render(surface, 1280 - self.play_again.width - 10, 640)
		self.score.render(surface, 850, 720/2 - self.score.height/2)

	def update(self, dt, event):
		if self.menu.mouse_hover(10, 640) and event.mouse_press(0):
			self.game.goto_menu()
		if self.play_again.mouse_hover(1280 - self.play_again.width - 10, 640) and event.mouse_press(0):
			self.game.goto_game()