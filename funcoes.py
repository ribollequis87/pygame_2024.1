class Utils:
    
    @staticmethod
    def verificar_colisao_circulo(x, y, cx, cy, raio):
        distancia_centro_ponto = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
        return distancia_centro_ponto <= raio

    @staticmethod
    def verificar_colisao_retangulo(x, y, x_quadrado, y_quadrado, largura_quadrado, altura_quadrado):
        return (x_quadrado <= x <= x_quadrado + largura_quadrado) and (y_quadrado <= y <= y_quadrado + altura_quadrado)

    @staticmethod
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