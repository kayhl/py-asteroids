import pygame
from circleshape import CircleShape
from logger import log_event
import random
from constants import POWERUP_RADIUS, POWERUP_SPAWN_RATE_SECONDS

class Powerup(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, POWERUP_RADIUS)

	def draw(self, screen):
		x, y = self.position
		r = POWERUP_RADIUS
		points = [
			(x, y - r), # top
			(x + r, y), # right
			(x, y + r), # bottom
			(x - r, y), # left
		]
		pygame.draw.polygon(screen, (255, 255, 0), points)
