import pygame
import time
import sys

import character


FPS = 30
clock = pygame.time.Clock()


def quit():
    sys.exit(0)


def game():
    screen = pygame.display.set_mode((720, 420))
    screen_rect = screen.get_rect()
    hero = character.Character('images/hero.png', screen_rect.center)
    actors_group = pygame.sprite.RenderPlain(hero)

    while 1:
        delta_time = clock.tick(FPS)
        for event in pygame.event.get():

            # All keys pressed
            if hasattr(event, 'key'):
                if event.key == pygame.K_q:
                    quit()

                elif event.key == pygame.K_LEFT:
                    hero.x -= 10

                elif event.key == pygame.K_RIGHT:
                    hero.x += 10

                elif event.key == pygame.K_UP:
                    hero.y -= 10

                elif event.key == pygame.K_DOWN:
                    hero.y += 10

        screen.fill((0,0,0))
        actors_group.update(delta_time)
        actors_group.draw(screen)
        pygame.display.flip()


def main():
    game()

if __name__ == '__main__':
    main()
