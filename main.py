import pygame
import sys
import constants
from logger import log_event, log_state
from player import Player
from asteroidfield import AsteroidField
from shot import Shot
from asteroid import Asteroid
from powerup import Powerup
from powerupfield import PowerupField


def main():
    print("Starting Asteroids with pygame version: VERSION")
    print("Screen width: 1280")
    print("Screen height: 720")

    pygame.init()
    font = pygame.font.SysFont(None, 36)
    score = 0
    lives = 4
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerups = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Powerup.containers = (powerups, updatable, drawable)
    PowerupField.containers = (updatable,)

    asteroid_field = AsteroidField()
    player = Player(x, y)
    powerup_field = PowerupField(powerups)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                lives -= 1
                if lives == 0:
                    log_event("player_hit")
                    print("Game over!")
                    print(f"Final score: {score}")
                    sys.exit()
                else:
                    player.position.update(x, y)
                    player.power_level = max(player.power_level - 1, 0)
                break
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    score += 10
                    break

        for powerup in powerups:
               if powerup.collides_with(player):
                    log_event("powerup_gained")
                    powerup.kill()
                    player.power_level = min(player.power_level + 1, 2)

        for obj in drawable:
            obj.draw(screen)

        # tracking score, lives    
        hud_text = f"Score: {score}     Lives: {lives}"
        hud_surface = font.render(hud_text, True, (0, 191, 147))
        screen_width = screen.get_width()
        hud_width = hud_surface.get_width()
        hud_x = (screen_width - hud_width) // 2
        hud_y = 10
        screen.blit(hud_surface, (hud_x, hud_y))


        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()

# to launch the venv: `source .venv/bin/activate`
