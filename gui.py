import pygame
class HealthBar:
	def __init__(self):
		self.health = 0.80

	def render(self, surface, x,y, width=100):
		pygame.draw.rect(surface, (255,0, 0), (x, y, width, 20))
		if self.health != 0:
			pygame.draw.rect(surface, (0, 255,0 ), (x, y, width * self.health, 20))

class Text:
	def __init__(self, text, size, color):
		self.font = pygame.font.Font('fonts/JewliScript1.ttf', size)
		self.color = color
		self.text = text
		self.render_text()
		self.width, self.height = self.text_rendered.get_size()

	def render(self, surface, x,y):
		surface.blit(self.text_rendered, (x,y))

	def mouse_hover(self, x, y):
		width, height = self.text_rendered.get_size()
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if mouse_x > x and mouse_x < x + width:
			if mouse_y > y and mouse_y < y + height:
				return True
		return False

	def render_text(self):
		self.text_rendered = self.font.render(self.text, 8, (self.color))