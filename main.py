import pygame as pg
import numpy as np
from funcoes import *
from constantes import *
import random
from level1 import level_1
from level2 import level_2
from level3 import level_3

pg.init()

tela = 0
largura, altura = 640, 480
screen = pg.display.set_mode((largura, altura))

rodando = True

while rodando:

    if tela == 0:
        imagem_fundo = pg.image.load('images/inicial.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False
            if event.type == pg.MOUSEBUTTONDOWN:
                tela = 1

    if tela == 1:
        imagem_fundo = pg.image.load('images/tela_niveis1.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False
            if event.type == pg.MOUSEBUTTONDOWN:
                tela = 2
 
    if tela == 2:
        level_1(tela, rodando)

    if tela == 3:
        imagem_fundo = pg.image.load('images/tela_niveis2.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False
            if event.type == pg.MOUSEBUTTONDOWN:
                tela = 4

    if tela == 4:
        level_2(tela, rodando)

    if tela == 5:
        imagem_fundo = pg.image.load('images/tela_niveis3.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False
            if event.type == pg.MOUSEBUTTONDOWN:
                tela = 6

    if tela == 6:
        level_3(tela, rodando)

    if tela == 7:
        imagem_fundo = pg.image.load('images/tela_niveis4.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False
            if event.type == pg.MOUSEBUTTONDOWN:
                rodando = False

    if tela == 8:
        imagem_fundo = pg.image.load('images\OIG3.jpg')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False
            if event.type == pg.MOUSEBUTTONDOWN:
                tela = 1

    pg.display.update()

# começa na tela de start
# se pressionar vai para a tela de níveis (1)

# se pressionar vai para o nível 1
# se passar vai para a tela de níveis (2)

# se pressionar vai para o nível 2
# se passar vai para a tela de níveis (3)

# se pressionar vai para o nível 3
# se passar vai para a tela de níveis (4)

# se pressionar vai para o fim
                
pg.quit()