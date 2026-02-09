import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_RADIUS, PLAYER_MOVE_SPEED, PLAYER_TURN_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
        self.power_level = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
            
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_MOVE_SPEED * dt
        self.position += rotated_with_speed_vector
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.cooldown -= dt

    def shoot(self):
        if self.cooldown > 0:
            return
        if self.power_level == 2:
            self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS / 2
        else:
            self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

        if self.power_level == 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

        elif self.power_level == 1:
            angles = [-15, 0, 15]
            for a in angles:
                shot = Shot(self.position.x, self.position.y)
                shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation + a) * PLAYER_SHOOT_SPEED
                
        elif self.power_level == 2:
            # this is where the cooldown rate changes
            angles = [-15, 0, 15]
            for a in angles:
                shot = Shot(self.position.x, self.position.y)
                shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation + a) * PLAYER_SHOOT_SPEED