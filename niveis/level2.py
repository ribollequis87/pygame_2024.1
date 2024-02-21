import pygame as pg
import numpy as np
import random
from constantes import *
from funcoes import Utils

class Level2:

    def __init__(self):
        
        self.tiros = 3  # Número de tiros disponíveis
        self.s = np.array([80, 190])  # Posição inicial do personagem
        self.pressed = False  # Flag para indicar se o botão do mouse está pressionado
        self.v = 0
        self.assets = Assets()

    def update(self):
        # Capturar evento

        self.pressed = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False  
            
            if event.type == pg.MOUSEBUTTONDOWN and self.tiros >= 0:
                self.pressed = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and self.assets.v0 < 7 and self.assets.v0 >= 1:
                    self.assets.v0 = self.assets.v0 + 1

                if event.key == pg.K_DOWN and self.assets.v0 <= 7 and self.assets.v0 > 1:
                    self.assets.v0 = self.assets.v0 - 1


        if Utils.verificar_colisao_retangulo(self.s[0], self.s[1], 570, (self.assets.y_luci-20), 50, 50):
            return 5

        # Verificar se o personagem atingiu os limites da tela
        if self.tiros == 3:
            if self.pressed:
                self.tiros -= 1
                self.y = pg.mouse.get_pos()
                self.v = self.y - self.assets.s0
                self.v = self.v / np.linalg.norm(self.v)
                self.v *= self.assets.v0
                self.s = self.assets.s0

        if (self.s[0] < 10 or self.s[0] > 630 or self.s[1] < 10 or self.s[1] > 470):

            if self.tiros <= 0:
                return 3

            if self.pressed:
                self.tiros -= 1
                self.y = pg.mouse.get_pos()
                self.v = self.y - self.assets.s0
                self.v = self.v / np.linalg.norm(self.v)
                self.v *= self.assets.v0
                self.s = self.assets.s0

        # Controlar frame rate
        self.assets.clock.tick(self.assets.FPS)

        # Processar posição
        self.v = self.v
        self.s = self.s + self.v

        if self.s[0] != 80 and self.s[1] != 190:

            distance_1 = np.linalg.norm((self.assets.x_satelite, self.assets.y_satelite) - self.s)
            gravtional_direction_1 = ((self.assets.x_satelite, self.assets.y_satelite) - self.s) / distance_1
            gravtional_force_1 = (self.assets.constante_satelite / distance_1**2) * gravtional_direction_1
            self.v = self.v + gravtional_force_1

            distance_2 = np.linalg.norm((self.assets.x_sol - self.assets.circle_radius, self.assets.y_sol - self.assets.circle_radius) - self.s)
            gravtional_direction_2 = ((self.assets.x_sol - self.assets.circle_radius, self.assets.y_sol - self.assets.circle_radius) - self.s) / distance_2
            gravtional_force_2 = (self.assets.constante_sol / distance_2**2) * gravtional_direction_2
            self.v = self.v + gravtional_force_2

        pg.display.update()

        return 4

    def draw(self):

        self.assets.screen.fill(self.assets.BLACK)

        self.assets.screen.blit(self.assets.imagem_fundo, (0, 0))

        for _ in range(1):
            x = random.randint(0, 640)
            y = random.randint(0, 480)
            pg.draw.circle(self.assets.screen, (255, 255, 255), (x, y), 2)

        # Desenhar personagem
        if self.s[0] != 80 and self.s[1] != 190:

            self.rect = pg.Rect(self.s, (10, 10))
            self.assets.screen.blit(self.assets.personagem, self.rect)

            self.rect = pg.Rect((self.s[0] - 5, self.s[1] - 5), (10, 10))
            self.assets.screen.blit(self.assets.imagem_tiro, self.rect)

        celeste = pg.draw.circle(self.assets.screen, (0, 200, 200), (self.assets.x_satelite, self.assets.y_satelite), 20)
        self.assets.screen.blit(self.assets.imp, (10, 180))

        # rect_luci = pg.Rect((570, self.assets.y_luci), (50, 50))
        # self.assets.screen.blit(self.assets.luci_retangulo, rect_luci)
        self.assets.screen.blit(self.assets.luci, (570, self.assets.y_luci))

        # Desenhar o Sol e o planeta
        # pg.draw.circle(self.assets.screen, self.assets.circle_color, self.assets.circle_center, self.assets.circle_radius)

        # Desenhar imagens
        self.assets.screen.blit(self.assets.imagem_satelite, (self.assets.x_satelite - self.assets.circle_radius, self.assets.y_satelite - self.assets.circle_radius))
        self.assets.screen.blit(self.assets.imagem_sol, (self.assets.x_sol - self.assets.circle_radius, self.assets.y_sol - self.assets.circle_radius))

        # Desenhar tiros disponíveis
        for i in range(self.tiros):
            self.assets.screen.blit(self.assets.imagem_tiro, (15 + (i * 25), 15))

        for i in range(7):
            self.assets.screen.blit(self.assets.imagem_raio_vazio, (608 - (i * 25), 15))

        for i in range(self.assets.v0):
            self.assets.screen.blit(self.assets.imagem_raio, (458 + (i * 25), 15))