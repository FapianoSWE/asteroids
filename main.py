import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    dt = 0
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    AsteroidField.containers = (updatable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    Player.containers = (updatable_group, drawable_group)
    Shot.containers = (updatable_group, drawable_group, shot_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(pygame.Color(0, 0, 0, 255))
        for updatable in updatable_group:
            updatable.update(dt)
        for asteroid in asteroid_group:
            if(asteroid.is_colliding(player)):
                print("Game over!")
                return
            for shot in shot_group:
                if(shot.is_colliding(asteroid)):
                    shot.kill()
                    asteroid.split()
        for drawable in drawable_group:
            drawable.draw(screen)
        pygame.display.flip()
        dt = timer.tick(60) / 1000


if __name__ == "__main__":
    main()
