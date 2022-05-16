from projeto import Projeto

class Elemento(Projeto):
    def __init__(self,arquivo):
        super().__init__(arquivo)
        self.coordenada_elemento = super().elemento_rede('coordenada')
        self.nome_elemento = super().elemento_rede('nome')
        self.tipo_elemento = super().elemento_rede('style')
        self.poste_elemento = {}
        self.__separador()
        self.__tratamento()

    def __tratamento(self):
        for x in self.coordenada_elemento:
            for i in self.poste_coordenada:
                if super().distancia(self.coordenada_elemento[x], self.poste_coordenada[i]) <= 2:
                    self.poste_elemento[x] = i
                    break
                else:
                    self.poste_elemento[x] = self.coordenada_elemento[x]
    def __separador(self):
        for tipo in self.tipo_elemento:
            if 'shapes/donut.pngff00ff00' in self.style[self.tipo_elemento[tipo]]:
                self.tipo_elemento[tipo] = 'CEO'
            elif 'shapes/donut.pngff00ffff' in self.style[self.tipo_elemento[tipo]]:
                self.tipo_elemento[tipo] = 'CEO-Futura'
            elif 'shapes/donut.pngff0000ff' in self.style[self.tipo_elemento[tipo]]:
                self.tipo_elemento[tipo] = 'HUB-DPR'
            elif 'shapes/polygon.png' in self.style[self.tipo_elemento[tipo]]:
                self.tipo_elemento[tipo] = 'Reserva'
            elif 'shapes/square.pngff0000ff' in self.style[self.tipo_elemento[tipo]]:
                self.tipo_elemento[tipo] = 'CTO-HUB'
            elif 'shapes/square.pngff00ffff' in self.style[self.tipo_elemento[tipo]]:
                self.tipo_elemento[tipo] = 'CTO-HUB-Futura'
            elif 'paddle/red-diamond.png' in self.style[self.tipo_elemento[tipo]]:
                self.tipo_elemento[tipo] = 'CTO'
            elif 'paddle/ltblu-diamond.png' in self.style[self.tipo_elemento[tipo]]:
                self.tipo_elemento[tipo] = 'CTO-Indoor'
            elif 'paddle/ylw-diamond.png' in self.style[self.tipo_elemento[tipo]]:
                self.tipo_elemento[tipo] = 'CTO-Futura'
            elif 'shapes/ranger_station.png' in self.style[self.tipo_elemento[tipo]]:
                self.tipo_elemento[tipo] = 'POP'

    def coordenada_por_elemento(self,elemento):
        dados = {}
        for i in self.tipo_elemento:
            if self.tipo_elemento[i] == elemento:
                dados[i] = self.coordenada_elemento[i]
        return dados

    def poste_por_elemento(self,elemento):
        dados = {}
        for i in self.tipo_elemento:
            if self.tipo_elemento[i] == elemento:
                dados[i] = self.poste_elemento[i]
        return dados

    def contador(self, elemento):
        cont = 0
        for i in self.tipo_elemento.values():
            if elemento == i:
                cont += 1
        return cont