import pygame as pg
import numpy as np
from funcoes import *

c = 100  # Constante gravitacional
CENTRO_GRAVITACIONAL = (400, 300)  # Posição do centro gravitacional

# Tamanho da tela e definição do FPS
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
FPS = 60  # Frames per Second

BLACK = (0, 0, 0)
COR_PERSONAGEM = (200, 200, 200)

# Inicializar posicoes
s0 = np.array([80,190])
a = np.array([0, 0.05])
y = pg.mouse.get_pos()
v = y - s0
v = v/np.linalg.norm(v)
v *= 5
s = s0

sol = np.array([300, 100])
planeta = np.array([100, 300])

# Personagem
personagem = pg.Surface((5, 5))  # Tamanho do personagem
personagem.fill(COR_PERSONAGEM)  # Cor do personagem

canhao = pg.Surface((5, 5))  # Tamanho do personagem
canhao.fill((100,100,100))  # Cor do personagem

corpo_celeste = pg.Surface((20, 20))  
corpo_celeste.fill((30,50,100))  # Cor do personagem

pg.display.set_caption('image')
luci = pg.image.load("images/nave.png").convert()
luci = pg.transform.scale(luci,(60,30))
luci_retangulo = pg.Surface((60, 30))  # Tamanho do personagem
luci_retangulo.fill((200,200,200))  # Cor do personagem

pg.display.set_caption('image')
imp = pg.image.load("images/terra.png").convert()
imp = pg.transform.scale(imp,(60,60))

rodando = True
pressed = False

x_satelite = np.random.randint(150,490)
y_satelite = np.random.randint(150,330)

y_luci = np.random.randint(150,330)

# Parâmetros do círculo
circle_color = (255, 0, 0)
circle_radius = 25
circle_center = (300, 100)
circle_rect = pg.Rect(circle_center[0] - circle_radius, circle_center[1] - circle_radius,
                        circle_radius * 2, circle_radius * 2)

# Parâmetros do planeta
planet_color = (0, 0, 255)
planet_radius = 20
planet_rect = pg.Rect(planeta[0] - planet_radius, planeta[1] - planet_radius,
                        planet_radius * 2, planet_radius * 2)

imagem_satelite = pg.image.load('images/venus.png')
imagem_satelite = pg.transform.scale(imagem_satelite, (2 * circle_radius, 2 * circle_radius))

imagem_sol = pg.image.load('images/marte.webp')
imagem_sol = pg.transform.scale(imagem_sol, (2 * circle_radius, 2 * circle_radius))

imagem_planeta = pg.image.load('images/urano.png')
imagem_planeta = pg.transform.scale(imagem_planeta, (2 * planet_radius, 2 * planet_radius))

imagem_tiro = pg.image.load('images/bola_de_fogo.png')
imagem_tiro = pg.transform.scale(imagem_tiro, (20,20))