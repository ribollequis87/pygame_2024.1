import pygame as pg
from constantes import *
from funcoes import Utils
from niveis.level1 import Level1
from niveis.level2 import Level2
from niveis.level3 import Level3

# Inicialização do Pygame
pg.init()
pg.mixer.init()

# Criação dos objetos de recursos e funções úteis
assets = Assets()
funcoes = Utils()

# Configurações da tela
largura, altura = 640, 480
screen = pg.display.set_mode((largura, altura))

# Variáveis de controle do jogo
rodando = True
tela_atual = 0

tempo_passado = 0
tempo_exibicao = 50000

# Carregamento e reprodução da música de fundo
pg.mixer.music.load('sound/thunderbird-game-over-9232.mp3')
pg.mixer.music.play()

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
            tela_atual = 1

    elif tela_atual == 1:

        imagem_fundo = pg.image.load('images/tela_jogar.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False

            pos = pg.mouse.get_pos()

            if event.type == pg.MOUSEBUTTONDOWN and funcoes.verificar_colisao_retangulo(pos[0], pos[1], 275, 352, 100, 28):
                tela_atual = 2

            if event.type == pg.MOUSEBUTTONDOWN and funcoes.verificar_colisao_retangulo(pos[0], pos[1], 288, 395, 73, 27):
                rodando = False


    elif tela_atual == 2:
        imagem_fundo = pg.image.load('images/tela_niveis1.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False

            pos = pg.mouse.get_pos()

            if event.type == pg.MOUSEBUTTONDOWN and funcoes.verificar_colisao_retangulo(pos[0], pos[1], 70, 200, 120, 100):
                tela_atual = 3

    elif tela_atual == 4:
        imagem_fundo = pg.image.load('images/tela_niveis2.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False

            pos = pg.mouse.get_pos()

            if event.type == pg.MOUSEBUTTONDOWN and funcoes.verificar_colisao_retangulo(pos[0], pos[1], 230, 40, 120, 100):
                tela_atual = 5

    elif tela_atual == 6:
        imagem_fundo = pg.image.load('images/tela_niveis3.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False

            pos = pg.mouse.get_pos()
            
            if event.type == pg.MOUSEBUTTONDOWN and funcoes.verificar_colisao_retangulo(pos[0], pos[1], 475, 200, 120, 100):
                tela_atual = 7

    elif tela_atual == 8:
        imagem_fundo = pg.image.load('images/tela_niveis4.png')
        imagem_fundo = pg.transform.scale(imagem_fundo, (largura, altura))
        screen.blit(imagem_fundo, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False
            if event.type == pg.MOUSEBUTTONDOWN:
                rodando = False

    elif tela_atual == 3:

        level1 = Level1()

        while rodando == 3:
            level1.draw()
            rodando = level1.update()

        if rodando == False:
            break

        rodando = level1.update()
            
        if rodando == 4:
            tela_atual = 4

        if rodando == 2:
            tela_atual = 2

    elif tela_atual == 5:

        level2 = Level2()

        while rodando == 5:
            level2.draw()
            rodando = level2.update()

        if rodando == False:
            break

        rodando = level2.update()
            
        if rodando == 6:
            tela_atual = 6

        if rodando == 4:
            tela_atual = 4

    elif tela_atual == 7:

        level3 = Level3()

        while rodando == 7:
            level3.draw()
            rodando = level3.update()

        if rodando == False:
            break

        rodando = level3.update()
            
        if rodando == 8:
            tela_atual = 8

        if rodando == 6:
            tela_atual = 6

    pg.display.update()

pg.mixer.quit()
pg.quit()