from projeto import Projeto

class Caixa(Projeto):
    def __init__(self,arquivo):
        super().__init__(arquivo)
        self.__coordenada_caixa = super()._ext_caixa_ftth('coordenada')
        self.__nome_caixa = super()._ext_caixa_ftth('nome')
        self.__tipo_caixa = super()._ext_caixa_ftth('style')
        self.__style = super()._ext_style
        self.__tipo = self.__separador()

    def tratamento(self,poste):
        dados = self.__coordenada_caixa
        for x in self.__coordenada_caixa:
            for i in poste:
                if super().distancia(self.__coordenada_caixa[x],poste[i]) <= 2:
                    dados[x] = i
                    break
        return dados

    def __separador(self):
        for tipo in self.__tipo_caixa:
            if 'donut.png' in self.__style[self.__tipo_caixa[tipo]]:
                self.__tipo_caixa[tipo] = 'CEO'
            elif 'polygon.png' in self.__style[self.__tipo_caixa[tipo]]:
                self.__tipo_caixa[tipo] = 'Reserva'
            elif 'square.png' in self.__style[self.__tipo_caixa[tipo]]:
                self.__tipo_caixa[tipo] = 'CTO-HUB'
            elif 'red-diamond.png' in self.__style[self.__tipo_caixa[tipo]]:
                self.__tipo_caixa[tipo] = 'CTO'
            elif 'ylw-diamond.png' in self.__style[self.__tipo_caixa[tipo]]:
                self.__tipo_caixa[tipo] = 'CTO-Futura'
            elif 'shapes/ranger_station.png' in self.__style[self.__tipo_caixa[tipo]]:
                self.__tipo_caixa[tipo] = 'POP'
        return self.__tipo_caixa

    @property
    def coordenada_caixa(self):
        return self.__coordenada_caixa

    @property
    def nome_caixa(self):
        return self.__nome_caixa

    @property
    def tipo(self):
        return self.__tipo

    def contador(self, tipo):
        cont = 0
        for i in self.__tipo.values():
            if tipo == i:
                cont += 1
        return cont