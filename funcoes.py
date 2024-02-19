def verifica_colisao(x, y, circle_center, circle_radius):
    distancia_centro = ((x - circle_center[0]) * 2 + (y - circle_center[1]) * 2) ** 0.5
    return distancia_centro <= circle_radius

def calcular_aceleracao_gravitacional(particula, centro_gravitacional, c):
    px, py = particula.posicao
    cx, cy = centro_gravitacional
    dx = cx - px
    dy = cy - py
    dist = max(1, (dx ** 2 + dy ** 2) ** 0.5)
    aceleracao = c / dist ** 2
    ax = aceleracao * dx / dist
    ay = aceleracao * dy / dist
    return ax, ay