class Utils:
    
    @staticmethod
    def verificar_colisao_circulo(x, y, cx, cy, raio):
        distancia_centro_ponto = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
        return distancia_centro_ponto <= raio

    @staticmethod
    def verificar_colisao_retangulo(x, y, x_quadrado, y_quadrado, largura_quadrado, altura_quadrado):
        return (x_quadrado <= x <= x_quadrado + largura_quadrado) and (y_quadrado <= y <= y_quadrado + altura_quadrado)
    
    @staticmethod
    def verificar_circulo_circulo(x1, y1, raio1, x2, y2, raio2):
        distancia_centros = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return distancia_centros <= raio1 + raio2