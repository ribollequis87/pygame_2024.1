import pygame as pg
import numpy as np
from funcoes import *
from constantes import *
import random

pg.init()

tiros = 3
font = pg.font.SysFont('Arial', 36)  
text_color = (255, 255, 255)

tela = 2

while rodando:
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

        # if verifica_colisao(s[0], s[1], circle_center, circle_radius): 
        #     rnd = abs(np.random.randn(2))
        #     v0 = pg.mouse.get_pos() - s0
        #     v0 = (v0 / np.linalg.norm(v0)) * 0.1
        #     s, v = s0, v0*rnd
        #     tiros -= 1

    # Controlar frame rate
    clock.tick(FPS)


    # Processar posicoes
    v = v 
    s = s + v

    # if tela == 1:
    #     largura, altura = 640, 480
    #     screen = pg.display.set_mode((largura, altura))
    #     imagem_fundo = pg.image.load('images\OIG1.jpg')
    #     imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
    #     screen.blit(imagem_fundo, (0, 0))
    #     if event.type == pg.MOUSEBUTTONDOWN:
    #         tela == 2

    if tela == 2:
        # Desenhar fundo
        screen.fill((BLACK))

        for _ in range(1):
            x = random.randint(0, 640)
            y = random.randint(0, 480)
            pg.draw.circle(screen, (255,255,255), (x, y), 2)

        # Desenhar personagem
        rect = pg.Rect(s, (10, 10))  # First tuple is position, second is size.
        screen.blit(personagem, rect)

        # rect_canhao = pg.Rect(s, (10, 10))  # First tuple is position, second is size.
        # screen.blit(canhao, rect_canhao)

        celeste = pg.draw.circle(screen, (0, 200, 200), (x_satelite,y_satelite), 20)  # First tuple is position, second is size.
        # screen.blit(corpo_celeste, celeste)

        # Using blit to copy content from one surface to other
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
        screen.blit(imagem_planeta, (planeta[0] - planet_radius, planeta[1] - planet_radius))

        # text_surface = font.render(f"Tiros restantes: {tiros}", True, text_color)
        # screen.blit(text_surface, (10, 10))  # Posição do texto na tela

        for i in range(tiros):
            screen.blit(imagem_tiro, (5+(i*25),5))

        # if verifica_colisao(y[0], y[1], circle_center, circle_radius):

        # Update!
        pressed = False

    if tela == 3:
        largura, altura = 640, 480
        screen = pg.display.set_mode((largura, altura))
        imagem_fundo = pg.image.load('images\OIG3.jpg')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

    pg.display.update()

pg.quit()