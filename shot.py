from constants import SHOT_RADIUS
from circleshape import CircleShape
import pygame

class Shot(CircleShape, pygame.sprite.Sprite):
	containers = ()
	def __init__(self, x, y):
		CircleShape.__init__(self, x, y, SHOT_RADIUS)
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.velocity = pygame.Vector2(0, 0)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 0)

	def update(self, dt):
		self.position += self.velocity * dt
