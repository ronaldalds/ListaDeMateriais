from projeto import Projeto

class Elemento(Projeto):
    def __init__(self,arquivo):
        super().__init__(arquivo)
        self.__coordenada_elemento = {}
        self.__nome_elemento = {}
        self.__tipo_elemento = {}
        self.__style = {}
        self.__tipo = {}

    def tratamento(self,poste):
        self.__coordenada_elemento = super().ext_caixa_ftth('coordenada')
        for x in self.__coordenada_elemento:
            for i in poste:
                if super().distancia(self.__coordenada_elemento[x], poste[i]) <= 2:
                    self.__coordenada_elemento[x] = i
                    break
        return self.__coordenada_elemento

    def __separador(self):
        self.__tipo_elemento = super().ext_caixa_ftth('style')
        self.__style = super().ext_style
        for tipo in self.__tipo_elemento:
            if 'donut.png' in self.__style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'CEO'
            elif 'polygon.png' in self.__style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'Reserva'
            elif 'square.png' in self.__style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'CTO-HUB'
            elif 'red-diamond.png' in self.__style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'CTO'
            elif 'ylw-diamond.png' in self.__style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'CTO-Futura'
            elif 'shapes/ranger_station.png' in self.__style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'POP'
        return self.__tipo_elemento

    @property
    def coordenada_elemento(self):
        self.__coordenada_elemento = super().ext_caixa_ftth('coordenada')
        return self.__coordenada_elemento

    @property
    def nome_elemento(self):
        self.__nome_elemento = super().ext_caixa_ftth('nome')
        return self.__nome_elemento

    @property
    def tipo_elemento(self):
        self.__tipo = self.__separador()
        return self.__tipo




    def contador(self, tipo):
        cont = 0
        for i in self.__tipo.values():
            if tipo == i:
                cont += 1
        return cont