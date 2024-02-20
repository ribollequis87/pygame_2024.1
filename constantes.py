import pygame as pg
import numpy as np

class Assets:

    def __init__(self):
        self.c = 100  # Constante gravitacional
        self.CENTRO_GRAVITACIONAL = (400, 300)  # Posição do centro gravitacional

        self.constante_satelite = 600
        self.constante_sol = 500
        self.constante_planeta = 400

        # Tamanho da tela e definição do FPS
        self.screen = pg.display.set_mode((640, 480))
        self.clock = pg.time.Clock()
        self.FPS = 60  # Frames per Second

        self.BLACK = (0, 0, 0)
        self.COR_PERSONAGEM = (200, 200, 200)

        self.v0 = 5

        # Inicializar posicoes
        self.s0 = np.array([80, 190])
        self.a = np.array([0, 0.05])
        self.y = pg.mouse.get_pos()
        self.v = self.y - self.s0
        self.v = self.v / np.linalg.norm(self.v)
        self.v *= self.v0
        self.s = self.s0

        self.sol = np.array([300, 100])
        self.planeta = np.array([100, 300])

        # Personagem
        self.personagem = pg.Surface((10, 10))  # Tamanho do personagem
        self.personagem.fill(self.COR_PERSONAGEM)  # Cor do personagem

        self.canhao = pg.Surface((5, 5))  # Tamanho do personagem
        self.canhao.fill((100, 100, 100))  # Cor do personagem

        self.corpo_celeste = pg.Surface((20, 20))
        self.corpo_celeste.fill((30, 50, 100))  # Cor do personagem

        pg.display.set_caption('image')
        self.luci = pg.image.load("images/nave.png").convert()
        self.luci = pg.transform.scale(self.luci, (60, 30))
        self.luci_retangulo = pg.Surface((60, 30))  # Tamanho do personagem
        self.luci_retangulo.fill((200, 200, 200))  # Cor do personagem

        pg.display.set_caption('image')
        self.imp = pg.image.load("images/nave1.png").convert()
        self.imp = pg.transform.scale(self.imp, (80, 45))

        self.rodando = True
        self.pressed = False

        self.x_satelite = np.random.randint(150, 500)
        self.y_satelite = np.random.randint(150, 300)

        self.y_luci = np.random.randint(150, 330)

        # Parâmetros do círculo
        self.circle_color = (255, 0, 0)
        self.circle_radius = 25
        self.circle_center = (300, 100)
        self.circle_rect = pg.Rect(self.circle_center[0] - self.circle_radius, self.circle_center[1] - self.circle_radius,
                                   self.circle_radius * 2, self.circle_radius * 2)

        # Parâmetros do planeta
        self.planet_color = (0, 0, 255)
        self.planet_radius = 20
        self.planet_rect = pg.Rect(self.planeta[0] - self.planet_radius, self.planeta[1] - self.planet_radius,
                                    self.planet_radius * 2, self.planet_radius * 2)

        self.imagem_satelite = pg.image.load('images/pluto.png')
        self.imagem_satelite = pg.transform.scale(self.imagem_satelite, (2 * self.circle_radius, 2 * self.circle_radius))

        self.imagem_sol = pg.image.load('images/marte.webp')
        self.imagem_sol = pg.transform.scale(self.imagem_sol, (2 * self.circle_radius, 2 * self.circle_radius))

        self.imagem_planeta = pg.image.load('images/urano.png')
        self.imagem_planeta = pg.transform.scale(self.imagem_planeta, (2.3 * self.planet_radius, 2.3 * self.planet_radius))

        self.imagem_tiro = pg.image.load('images/portal.png')
        self.imagem_tiro = pg.transform.scale(self.imagem_tiro, (20, 20))

        self.imagem_fundo = pg.image.load('images/background.png')
        self.imagem_fundo = pg.transform.scale(self.imagem_fundo, (640, 510))

        self.imagem_raio = pg.image.load('images/raio.png')
        self.imagem_raio = pg.transform.scale(self.imagem_raio, (20, 25))

        self.imagem_raio_vazio = pg.image.load('images/raio_vazio.png')
        self.imagem_raio_vazio = pg.transform.scale(self.imagem_raio_vazio, (20, 25))