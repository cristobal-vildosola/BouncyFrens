import os

import pygame

from Blocks import Block, Platform
from CharactersBase import GravityChar, CustomGroup
from Text import Text

# centrar ventana
os.environ['SDL_VIDEO_CENTERED'] = '1'


def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60

    screen_width, screen_height = 600, 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Bouncy Frens")

    # personajes
    char_size = 50

    player1 = GravityChar(char_size, char_size, 150, 100, img='img/Pina.png', jumpspeed=8)
    player2 = GravityChar(char_size, char_size, 450, 600, img='img/Tomimi.png', jumpspeed=8)

    chars = CustomGroup([player1, player2])

    # bloques
    blocks = CustomGroup()
    border_color = (40, 20, 0)

    blocks.add(Block(30, screen_height, -30, 0, color=border_color))  # izquierda
    blocks.add(Block(30, screen_height, screen_width, 0, color=border_color))  # derecha
    blocks.add(Block(screen_width, 30, 0, screen_height, color=border_color))  # abajo

    block1 = Block(30, screen_height, screen_width / 2, 0)  # bloque invisible en la mitad para player1
    block2 = Block(30, screen_height, screen_width / 2 - 30, 0)  # bloque invisible en la mitad para player2

    # plataformas
    platform_color = (100, 50, 0)

    plat1 = Platform(300, 5, 0, 650,
                     color=platform_color)
    plat2 = Platform(300, 5, 300, 650,
                     color=platform_color)
    plat3 = Platform(200, 5, 0, 150,
                     color=platform_color)
    plat4 = Platform(200, 5, 400, 150,
                     color=platform_color)

    bottom_platforms = CustomGroup(plat1, plat2)
    top_platforms = CustomGroup(plat3, plat4)
    jump = False

    running = True
    while running:

        # eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player1.jump()
                    jump = True
                if event.key == pygame.K_w:
                    player2.jump()
                    jump = True

        # teclas apretadas
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            player1.move(dx=-5)
        if pressed[pygame.K_RIGHT]:
            player1.move(dx=5)

        if pressed[pygame.K_a]:
            player2.move(dx=-5)
        if pressed[pygame.K_d]:
            player2.move(dx=5)

        # mov automático
        chars.update()

        # colisiones
        chars.detect_collisions(blocks)
        chars.detect_collisions(bottom_platforms)
        if not jump:
            chars.detect_collisions(top_platforms)

        player1.detect_collisions([block1])
        player2.detect_collisions([block2])

        # para asegurarse de que no hayan problemas con las colisiones entre objetos que se mueven,
        # hay que detectar las colisiones n veces (debido a que al resolver una colisión pueden
        # aparecer nuevas colisiones en cadena)
        for _ in chars:
            chars.detect_collisions(chars)

        # dibujar
        screen.fill((25, 115, 200))  # rellenar fondo
        blocks.draw(screen)
        bottom_platforms.draw(screen)
        top_platforms.draw(screen)
        chars.draw(screen)

        # actualizar y esperar un tick
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
    return


if __name__ == "__main__":
    main()
