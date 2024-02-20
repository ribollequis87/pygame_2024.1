import pygame as pg
from constantes import *
from niveis.level1 import Level1
from niveis.level2 import Level2
from niveis.level3 import Level3

pg.init()

assets = Assets()

# Configurações da tela
largura, altura = 640, 480
screen = pg.display.set_mode((largura, altura))

rodando = True
tela_atual = 0

while rodando:

    if tela_atual == 0:
        imagem_fundo = pg.image.load('images/inicial.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False
            if event.type == pg.MOUSEBUTTONDOWN:
                tela_atual = 1

    elif tela_atual == 1:
        imagem_fundo = pg.image.load('images/tela_niveis1.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False
            if event.type == pg.MOUSEBUTTONDOWN:
                tela_atual = 2

    elif tela_atual == 3:
        imagem_fundo = pg.image.load('images/tela_niveis2.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False
            if event.type == pg.MOUSEBUTTONDOWN:
                tela_atual = 4

    elif tela_atual == 5:
        imagem_fundo = pg.image.load('images/tela_niveis3.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False
            if event.type == pg.MOUSEBUTTONDOWN:
                tela_atual = 6

    elif tela_atual == 7:
        imagem_fundo = pg.image.load('images/tela_niveis4.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False
            if event.type == pg.MOUSEBUTTONDOWN:
                rodando = False

    elif tela_atual == 2:

        level1 = Level1(assets)

        while rodando == 2:
            level1.draw()
            rodando = level1.update()

        rodando = level1.update()
            
        if rodando == 3:
            tela_atual = 3

        if rodando == 1:
            tela_atual = 1

    elif tela_atual == 4:

        level2 = Level2()

        while rodando == 4:
            level2.draw()
            rodando = level2.update()

        rodando = level2.update()
            
        if rodando == 5:
            tela_atual = 5

        if rodando == 3:
            tela_atual = 3

    elif tela_atual == 6:

        level3 = Level3()

        while rodando == 6:
            level3.draw()
            rodando = level3.update()

        rodando = level3.update()
            
        if rodando == 7:
            tela_atual = 7

        if rodando == 5:
            tela_atual = 5

    pg.display.update()

pg.quit()