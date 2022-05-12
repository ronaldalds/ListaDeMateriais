from projeto import Projeto

class Elemento(Projeto):
    def __init__(self,arquivo):
        super().__init__(arquivo)
        self.__coordenada_elemento = super().elemento_rede('coordenada')
        self.__poste = super().poste('POSTE')
        self.__nome_elemento = super().elemento_rede('nome')
        self.__poste_elemento = {}
        self.__tipo_elemento = super().elemento_rede('style')
        self.__style = super().style
        self.__separador()
        self.tratamento()
    def tratamento(self):
        for x in self.__coordenada_elemento:
            for i in self.__poste:
                if super().distancia(self.__coordenada_elemento[x], self.__poste[i]) <= 2:
                    self.__poste_elemento[x] = i
                    break
                else:
                    self.__poste_elemento[x] = self.__coordenada_elemento[x]
        return self.__poste_elemento
    def __separador(self):
        for tipo in self.__tipo_elemento:
            if 'shapes/donut.pngff00ff00' in self.__style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'CEO'
            elif 'shapes/donut.pngff0000ff' in self.__style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'HUB-DPR'
            elif 'shapes/polygon.png' in self.__style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'Reserva'
            elif 'shapes/square.pngff0000ff' in self.__style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'CTO-HUB'
            elif 'shapes/square.pngff00ffff' in self.__style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'CTO-HUB-Futura'
            elif 'paddle/red-diamond.png' in self.__style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'CTO'
            elif 'paddle/ltblu-diamond.png' in self.__style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'CTO-Indoor'
            elif 'paddle/ylw-diamond.png' in self.__style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'CTO-Futura'
            elif 'shapes/ranger_station.png' in self.__style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'POP'
        return self.__tipo_elemento
    @property
    def coordenada_elemento(self):
        return self.__coordenada_elemento
    @property
    def poste_elemento(self):
        return self.__poste_elemento
    @property
    def nome_elemento(self):
        return self.__nome_elemento
    @property
    def tipo_elemento(self):
        return self.__tipo_elemento
    # @property
    # def coordenada_reserva(self):
    #     dados = {}
    #     for i in self.__tipo_elemento:
    #         if self.__tipo_elemento[i] == 'Reserva':
    #             self.__dados[i] = self.coordenada_elemento[i]
    #     return dados
    #
    # def poste_reserva(self,poste):
    #     self.__dados = {}
    #     for i in self.__tipo_elemento:
    #         if self.__tipo_elemento[i] == 'Reserva':
    #             self.__dados[i] = self.tratamento(poste)[i]
    #     return self.__dados

    # def contador(self, tipo):
    #     cont = 0
    #     for i in self.__tipo_style.values():
    #         if tipo == i:
    #             cont += 1
    #     return cont