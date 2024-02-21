import pygame as pg
from constantes import *
from funcoes import Utils
from niveis.level1 import Level1
from niveis.level2 import Level2
from niveis.level3 import Level3

pg.init()

assets = Assets()
funcoes = Utils()

# Configurações da tela
largura, altura = 640, 480
screen = pg.display.set_mode((largura, altura))

rodando = True
tela_atual = 0

tempo_passado = 0
tempo_exibicao = 220000

while rodando:

    if tela_atual == 0:
        imagem_fundo = pg.image.load('images/inicial.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False

        tempo_passado += pg.time.get_ticks()
        if tempo_passado >= tempo_exibicao:
            tela_atual = 999

    elif tela_atual == 999:

        imagem_fundo = pg.image.load('images/tela_jogar.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        # pg.draw.rect(screen, (200, 200, 200), (277, 320, 90, 25), 1) # JOGAR

        # pg.draw.rect(screen, (200, 200, 200), (260, 360, 120, 25), 1) # INSTRUÇÕES
        
        # pg.draw.rect(screen, (200, 200, 200), (285, 395, 73, 25), 1) # SAIR

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False

            pos = pg.mouse.get_pos()

            if event.type == pg.MOUSEBUTTONDOWN and funcoes.verificar_colisao_retangulo(pos[0], pos[1], 285, 395, 73, 25):
                rodando = False

            if event.type == pg.MOUSEBUTTONDOWN and funcoes.verificar_colisao_retangulo(pos[0], pos[1], 277, 320, 90, 25):
                tela_atual = 1

    elif tela_atual == 1:
        imagem_fundo = pg.image.load('images/tela_niveis1.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False

            pos = pg.mouse.get_pos()

            if event.type == pg.MOUSEBUTTONDOWN and funcoes.verificar_colisao_retangulo(pos[0], pos[1], 70, 200, 120, 100):
                tela_atual = 2

    elif tela_atual == 3:
        imagem_fundo = pg.image.load('images/tela_niveis2.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False

            pos = pg.mouse.get_pos()

            if event.type == pg.MOUSEBUTTONDOWN and funcoes.verificar_colisao_retangulo(pos[0], pos[1], 230, 40, 120, 100):
                tela_atual = 4

    elif tela_atual == 5:
        imagem_fundo = pg.image.load('images/tela_niveis3.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False

            pos = pg.mouse.get_pos()
            
            if event.type == pg.MOUSEBUTTONDOWN and funcoes.verificar_colisao_retangulo(pos[0], pos[1], 475, 200, 120, 100):
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

        if rodando == False:
            break

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

        if rodando == False:
            break

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

        if rodando == False:
            break

        rodando = level3.update()
            
        if rodando == 7:
            tela_atual = 7

        if rodando == 5:
            tela_atual = 5

    pg.display.update()

pg.quit()