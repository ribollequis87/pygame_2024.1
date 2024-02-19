import pygame as pg
import numpy as np
from funcoes import *
from constantes import *
import random

def level2():

    tiros = 3

    # Capturar eventos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            rodando = False
        if event.type == pg.MOUSEBUTTONDOWN and tiros >=0 and tela == 2:
            pressed = True

    if s[0]<10 or s[0]>630 or s[1]<10 or s[1]>470 and tela == 2: # Se eu chegar ao limite da tela, reinicio a posição do personagem

        if tiros <= 0:
            tela = 3

        if pressed:
            tiros -= 1
            y = pg.mouse.get_pos()
            v = y - s0
            v = v/np.linalg.norm(v)
            v *= 5
            s = s0

    # Controlar frame rate
    clock.tick(FPS)


    # Processar posicoes
    s = s + v

    # Desenhar fundo
    screen.fill((BLACK))

    for _ in range(1):
        x = random.randint(0, 640)
        y = random.randint(0, 480)
        pg.draw.circle(screen, (255,255,255), (x, y), 2)

    # if verifica_colisao(s[0], s[1], (570, y_luci), 10):
    #     tela = 4

    # if verifica_colisao(s[0], s[1], (x_satelite - circle_radius, y_satelite - circle_radius), 1) or verifica_colisao(s[0], s[1], (circle_center[0] - circle_radius, circle_center[1] - circle_radius), 1) or verifica_colisao(s[0], s[1], (planeta[0] - planet_radius, planeta[1] - planet_radius), 1):
    #     tela = 3

    # Desenhar personagem
    rect = pg.Rect(s, (10, 10))  # First tuple is position, second is size.
    screen.blit(personagem, rect)


    celeste = pg.draw.circle(screen, (0, 200, 200), (x_satelite,y_satelite), 20)  # First tuple is position, second is size.
    screen.blit(imp, (10, 180))


    rect_luci = pg.Rect((570, y_luci), (50,50))  # First tuple is position, second is size.
    screen.blit(luci_retangulo, rect_luci)

    screen.blit(luci, (570, y_luci))

    # Sol
    pg.draw.circle(screen, circle_color, circle_center, circle_radius)

    # Planeta
    pg.draw.circle(screen, planet_color, planeta, planet_radius)

    screen.blit(imagem_satelite, (x_satelite - circle_radius, y_satelite - circle_radius))
    screen.blit(imagem_sol, (circle_center[0] - circle_radius, circle_center[1] - circle_radius))

    for i in range(tiros):
        screen.blit(imagem_tiro, (5+(i*25),5))

    # Update!
    pressed = False