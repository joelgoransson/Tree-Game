import pygame 
from controller import GameController, GameState
pygame.init()
class Game:
	def __init__(self):
		self.screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
		self.event_handler = EventHandler() 
		self.game_running = True
		self.clock = pygame.time.Clock()
		self.game_state = GameState(self, self)
		self.game_state.goto_menu()
		pygame.display.set_caption("Woodcutters Gaiden: Nature Strikes Back")
  
	def run(self):
		while self.game_running: 
			dt = self.clock.tick(30)/1000
			self.event()
			self.update(dt, self.event_handler)
			self.render(self.screen)
			pygame.display.update()

	def event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.game_running = False
			else:
				self.event_handler.handle_event(event)
				if self.event_handler.key_down(pygame.K_ESCAPE):
					self.game_state.goto_menu()


	def render(self, surface):
		surface.fill((0,0,0))
		self.game_state.render(surface)

	def update(self, dt, event):
		self.game_state.update(dt, event)

class EventHandler:
	def __init__(self):
		self.keys = []
		self.mouse = (0,0,0)
		self.press = []
		self.mouse_pressed = [0,0,0]

	def handle_event(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key not in self.keys:
				self.press.append(event.key)
			self.keys.append(event.key)
		elif event.type == pygame.KEYUP:
			while event.key in self.keys:
				del self.keys[self.keys.index(event.key)]
		elif event.type == pygame.MOUSEBUTTONDOWN:		
			self.mouse = pygame.mouse.get_pressed()
			self.mouse_pressed = self.mouse
		elif event.type == pygame.MOUSEBUTTONUP:
			self.mouse = pygame.mouse.get_pressed()

	def key_press(self, key):
		if key in self.press:
			del self.press[self.press.index(key)]
			return True
		return False

	def key_down(self, key):
		return key in self.keys

	def any_key(self):	
		return self.keys
	
	def mouse_down(self, button):
		return self.mouse[button]

	def mouse_press(self, button):
		mouse_pressed = self.mouse_pressed
		self.mouse_pressed = (0,0,0)
		return mouse_pressed[button]

game = Game()
game.run()
