import pygame as pg
import numpy as np

class Assets:

    def __init__(self):

        # 1- Constantes para a simulação gravitacional
        self.c = 100  # Constante gravitacional
        self.CENTRO_GRAVITACIONAL = (400, 300)  # Posição do centro gravitacional

        # 2- Constantes para cada Planeta Difetente
        self.constante_satelite = 800
        self.constante_sol = 700
        self.constante_planeta = 600

        # 3- Tamanho da tela e definição do FPS
        self.screen = pg.display.set_mode((640, 480))
        self.clock = pg.time.Clock()
        self.FPS = 60 

        # 4- Cores
        self.BLACK = (0, 0, 0)
        self.COR_PERSONAGEM = (200, 200, 200)

        # 5- Velocidade inicial do personagem
        self.v0 = 5

        # 6- Posições iniciais
        self.s0 = np.array([80, 190])
        self.a = np.array([0, 0.05])
        self.y = pg.mouse.get_pos()
        self.v = self.y - self.s0
        self.v = self.v / np.linalg.norm(self.v)
        self.v *= self.v0
        self.s = self.s0

        # 7- Posições dos corpos celestes
        self.sol = np.array([300, 100])
        self.planeta = np.array([100, 300])

        # 8- Personagem
        self.personagem = pg.Surface((10, 10))  
        self.personagem.fill(self.COR_PERSONAGEM)  

        # 9- Canhão
        self.canhao = pg.Surface((5, 5))  
        self.canhao.fill((100, 100, 100))  

        # 10- Corpo Celeste
        self.corpo_celeste = pg.Surface((20, 20))
        self.corpo_celeste.fill((30, 50, 100))  

        # 11- Carregamento de imagens
        pg.display.set_caption('image')
        self.luci = pg.image.load("images/nave.png")
        self.luci = pg.transform.scale(self.luci, (60, 30))
        self.luci_retangulo = pg.Surface((60, 30))  
        self.luci_retangulo.fill((200, 200, 200))  

        self.imp = pg.image.load("images/nave1.png")
        self.imp = pg.transform.scale(self.imp, (80, 45))

        self.imagem_satelite = pg.image.load('images/pluto.png')
        self.imagem_satelite = pg.transform.scale(self.imagem_satelite, (50, 50))

        self.imagem_sol = pg.image.load('images/venus.png')
        self.imagem_sol = pg.transform.scale(self.imagem_sol, (50, 50))

        self.imagem_planeta = pg.image.load('images/urano.png')
        self.imagem_planeta = pg.transform.scale(self.imagem_planeta, (50, 50))

        self.imagem_tiro = pg.image.load('images/portal.png')
        self.imagem_tiro = pg.transform.scale(self.imagem_tiro, (20, 20))

        self.imagem_fundo = pg.image.load('images/background.png')
        self.imagem_fundo = pg.transform.scale(self.imagem_fundo, (640, 510))

        self.imagem_raio = pg.image.load('images/raio.png')
        self.imagem_raio = pg.transform.scale(self.imagem_raio, (20, 25))

        self.imagem_raio_vazio = pg.image.load('images/raio_vazio.png')
        self.imagem_raio_vazio = pg.transform.scale(self.imagem_raio_vazio, (20, 25))

        # 12- Estado do jogo
        self.rodando = True
        self.pressed = False

        # 13- Posições aleatórias para os corpos celestes
        self.x_satelite = np.random.randint(180, 480)
        self.y_satelite = np.random.randint(180, 270)

        self.x_sol = np.random.randint(180, 480)
        self.y_sol = np.random.randint(80, 150)

        self.x_planeta = np.random.randint(180, 480)
        self.y_planeta = np.random.randint(300, 340)

        self.y_luci = np.random.randint(150, 330)

        # 14- Parâmetros do círculo
        self.circle_color = (255, 0, 0)
        self.circle_radius = 25
        self.circle_center = (300, 100)
        self.circle_rect = pg.Rect(self.x_sol - self.circle_radius, self.y_sol - self.circle_radius, self.circle_radius * 2, self.circle_radius * 2)

        # 15- Parâmetros do planeta
        self.planet_color = (0, 0, 255)
        self.planet_radius = 20
        self.planet_rect = pg.Rect(self.x_planeta - self.planet_radius, self.y_planeta - self.planet_radius, self.planet_radius * 2, self.planet_radius * 2)