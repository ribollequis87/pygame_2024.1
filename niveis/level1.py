import pygame as pg
import numpy as np
from constantes import *
from funcoes import Utils

class Level1:

    def __init__(self):
        # Inicialização dos parâmetros do jogo
        self.tiros = 4  
        self.s = np.array([80, 190])  # Posição inicial do personagem
        self.pressed = False  # Estado do botão de disparo
        self.v = 0  # Velocidade inicial
        self.assets = Assets()  # Instância dos recursos do jogo
        self.sound_laser = pg.mixer.Sound('sound/laser.mp3')  # Som do laser

    def update(self):
        # Atualização do estado do jogo

        self.pressed = False  # Reinicialização do estado de pressionamento do botão

        for event in pg.event.get():  # Captura de eventos
            if event.type == pg.QUIT:
                return False  # Encerra o jogo se fechar a janela
            
            mouse = pg.mouse.get_pos()  # Posição do mouse

            if event.type == pg.MOUSEBUTTONDOWN and self.tiros >= 0: 
                for i in range(7):
                    # Verifica se o botão de seleção de velocidade foi pressionado
                    if Utils.verificar_colisao_retangulo(mouse[0], mouse[1], 458 + (i * 25), 15, 20, 20):
                        self.assets.v0 = i + 1

                # Verifica se o botão de disparo foi pressionado
                if event.type == pg.MOUSEBUTTONDOWN and self.tiros >= 0 and not Utils.verificar_colisao_retangulo(mouse[0], mouse[1], 458, 15, 175, 250):
                    self.pressed = True
                    self.sound_laser.play()  # Toca o som do laser

            if event.type == pg.KEYDOWN:
                # Altera a velocidade do personagem
                if event.key == pg.K_UP and self.assets.v0 < 7 and self.assets.v0 >= 1:
                    self.assets.v0 = self.assets.v0 + 1
                if event.key == pg.K_DOWN and self.assets.v0 <= 7 and self.assets.v0 > 1:
                    self.assets.v0 = self.assets.v0 - 1

        # Verifica colisões e limites
        if Utils.verificar_colisao_retangulo(self.s[0], self.s[1], 570, (self.assets.y_luci-20), 50, 50):
            return 4  # Retorna 4 para indicar que o jogador perdeu
        
        if Utils.verificar_circulo_circulo(self.s[0], self.s[1], 10, self.assets.x_satelite, self.assets.y_satelite, self.assets.circle_radius):
            if self.tiros <= 0:
                return 2  # Retorna 2 para indicar que o jogador perdeu
            else:
                self.s[0] = 700
                self.s[1] = 700

        # Controla o número de tiros
        if self.tiros == 4:
            if self.pressed:
                self.tiros -= 1
                self.y = pg.mouse.get_pos()
                self.v = self.y - self.assets.s0
                self.v = self.v / np.linalg.norm(self.v)
                self.v *= self.assets.v0
                self.s = self.assets.s0

        # Verifica se o personagem atingiu os limites da tela
        if (self.s[0] < 10 or self.s[0] > 630 or self.s[1] < 10 or self.s[1] > 470):
            if self.tiros <= 0:
                return 2  # Retorna 2 para indicar que o jogador perdeu
            if self.pressed:
                self.tiros -= 1
                self.y = pg.mouse.get_pos()
                self.v = self.y - self.assets.s0
                self.v = self.v / np.linalg.norm(self.v)
                self.v *= self.assets.v0
                self.s = self.assets.s0

        # Controla o frame rate
        self.assets.clock.tick(self.assets.FPS)

        # Atualiza a posição do personagem
        self.v = self.v
        self.s = self.s + self.v

        # Aplica a força gravitacional do satélite
        if self.s[0] != 80 and self.s[1] != 190:
            distance = np.linalg.norm((self.assets.x_satelite, self.assets.y_satelite) - self.s)
            gravitational_direction = ((self.assets.x_satelite, self.assets.y_satelite) - self.s) / distance
            gravitational_force = (self.assets.constante_satelite / distance**2) * gravitational_direction
            self.v = self.v + gravitational_force

        pg.display.update()

        return 3  # Retorna 3 para indicar que o jogo deve continuar

    def draw(self):
        # Desenha os elementos na tela

        self.assets.screen.fill(self.assets.BLACK)  # Preenche a tela com preto

        self.assets.screen.blit(self.assets.imagem_fundo, (0, 0))  # Desenha o fundo

        self.assets.screen.blit(self.assets.luci, (570, self.assets.y_luci))  # Desenha o personagem

        if self.s[0] != 80 and self.s[1] != 190:
            self.rect = pg.Rect(self.s, (10, 10))
            self.assets.screen.blit(self.assets.personagem, self.rect)  # Desenha o personagem

            self.rect = pg.Rect((self.s[0] - 5, self.s[1] - 5), (10, 10))
            self.assets.screen.blit(self.assets.imagem_tiro, self.rect)  # Desenha o tiro

        self.assets.screen.blit(self.assets.imagem_satelite, (self.assets.x_satelite - self.assets.circle_radius, self.assets.y_satelite - self.assets.circle_radius))  # Desenha o satélite

        self.assets.screen.blit(self.assets.imp, (10, 180))  # Desenha a imagem imp

        # Desenha os tiros e a barra de velocidade
        for i in range(self.tiros):
            self.assets.screen.blit(self.assets.imagem_tiro, (15 + (i * 25), 15))
        for i in range(7):
            self.assets.screen.blit(self.assets.imagem_raio_vazio, (608 - (i * 25), 15))
        for i in range(self.assets.v0):
            self.assets.screen.blit(self.assets.imagem_raio, (458 + (i * 25), 15))