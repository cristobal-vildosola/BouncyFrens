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
    pygame.display.set_caption("tutorial FrenCoins")

    # personajes
    char_size = 50

    player1 = GravityChar(char_size, char_size, 150, 100, img='img/Pina.png', jumpspeed=18)
    player2 = GravityChar(char_size, char_size, 450, 600, img='img/Tomimi.png', jumpspeed=18)

    chars = CustomGroup([player1, player2])

    # bloques
    blocks = CustomGroup()
    border_color = (40, 20, 0)

    blocks.add(Block(30, screen_height, -30, 0, color=border_color))  # izquierda
    blocks.add(Block(30, screen_height, screen_width, 0, color=border_color))  # derecha
    blocks.add(Block(screen_width, 30, 0, screen_height, color=border_color))  # abajo

    # plataformas
    platform_color = (100, 50, 0)

    plat1 = Platform(200, 5,
                     0, 150,
                     color=platform_color)
    plat2 = Platform(200, 5,
                     400, 150,
                     color=platform_color)
    plat3 = Platform(300, 5,
                     0, 650,
                     color=platform_color)
    plat4 = Platform(300, 5,
                     300, 650,
                     color=platform_color)

    platforms = CustomGroup(plat1, plat2, plat3, plat4)

    indicacion = Text("Jugador 1 usa flechas para moverse, jugador 2 usa zsc",
                      screen_width / 2, 17, center=True, color=(200, 200, 200))
    indicacion2 = Text("(de esta manera no se bloquea el input en mi teclado)",
                       screen_width / 2, 37, center=True, color=(200, 200, 200), height=20)

    running = True
    while running:

        # eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player1.jump()
                if event.key == pygame.K_w:
                    player2.jump()

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
        chars.detect_collisions(platforms)

        # para asegurarse de que no hayan problemas con las colisiones entre objetos que se mueven,
        # hay que detectar las colisiones n veces (debido a que al resolver una colisión pueden
        # aparecer nuevas colisiones en cadena)
        for _ in chars:
            chars.detect_collisions(chars)

        # dibujar
        screen.fill((25, 115, 200))  # rellenar fondo
        blocks.draw(screen)
        platforms.draw(screen)
        indicacion.draw(screen)
        indicacion2.draw(screen)
        chars.draw(screen)

        # actualizar y esperar un tick
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
    return


if __name__ == "__main__":
    main()
