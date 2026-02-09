import pygame
import random
from powerup import Powerup
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, POWERUP_SPAWN_RATE_SECONDS

class PowerupField(pygame.sprite.Sprite):
	def __init__(self, powerups_group):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.spawn_timer = 0.0
		self.powerups = powerups_group

	def spawn(self, position):
		Powerup(position.x, position.y)

	def update(self, dt):
		self.spawn_timer += dt
		if self.spawn_timer > POWERUP_SPAWN_RATE_SECONDS:
			self.spawn_timer = 0
			if len(self.powerups) > 0:
				return
			x = random.uniform(0, SCREEN_WIDTH)
			y = random.uniform(0, SCREEN_HEIGHT)
			position = pygame.Vector2(x, y)
			self.spawn(position)
