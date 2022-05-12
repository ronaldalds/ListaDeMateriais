from projeto import Projeto

class Elemento(Projeto):
    def __init__(self,arquivo):
        super().__init__(arquivo)
        self.__coordenada_elemento = super().elemento_rede('coordenada')
        self.__nome_elemento = super().elemento_rede('nome')
        self.__tipo_elemento = super().elemento_rede('style')
        self.__poste_elemento = {}
        self.__separador()
        self.__tratamento()

    def __tratamento(self):
        for x in self.__coordenada_elemento:
            for i in self.poste_coordenada:
                if super().distancia(self.__coordenada_elemento[x], self.poste_coordenada[i]) <= 2:
                    self.__poste_elemento[x] = i
                    break
                else:
                    self.__poste_elemento[x] = self.__coordenada_elemento[x]
    def __separador(self):
        for tipo in self.__tipo_elemento:
            if 'shapes/donut.pngff00ff00' in self.style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'CEO'
            elif 'shapes/donut.pngff0000ff' in self.style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'HUB-DPR'
            elif 'shapes/polygon.png' in self.style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'Reserva'
            elif 'shapes/square.pngff0000ff' in self.style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'CTO-HUB'
            elif 'shapes/square.pngff00ffff' in self.style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'CTO-HUB-Futura'
            elif 'paddle/red-diamond.png' in self.style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'CTO'
            elif 'paddle/ltblu-diamond.png' in self.style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'CTO-Indoor'
            elif 'paddle/ylw-diamond.png' in self.style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'CTO-Futura'
            elif 'shapes/ranger_station.png' in self.style[self.__tipo_elemento[tipo]]:
                self.__tipo_elemento[tipo] = 'POP'

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

    def coordenada_por_elemento(self,elemento):
        dados = {}
        for i in self.__tipo_elemento:
            if self.__tipo_elemento[i] == elemento:
                dados[i] = self.__coordenada_elemento[i]
        return dados

    def poste_por_elemento(self,elemento):
        dados = {}
        for i in self.__tipo_elemento:
            if self.__tipo_elemento[i] == elemento:
                dados[i] = self.__poste_elemento[i]
        return dados

    def contador(self, elemento):
        cont = 0
        for i in self.__tipo_elemento.values():
            if elemento == i:
                cont += 1
        return cont