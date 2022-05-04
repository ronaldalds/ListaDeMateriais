from projeto import Projeto

class Caixa(Projeto):
    def __init__(self,arquivo):
        super().__init__(arquivo)
        self.__coordenada_caixa = super()._ext_caixa_ftth('coordenada')
        self.__nome_caixa = super()._ext_caixa_ftth('nome')
        self.__tipo_caixa = super()._ext_caixa_ftth('style')
        self.__style = super()._ext_style

    def tratamento(self,poste,disc):
        self.__dados = disc
        for x in disc:
            for i in poste:
                if self.distancia(disc[x],poste[i]) <= 2:
                    self.__dados[x] = i
                    break
        return self.__dados

    @property
    def coordenada_caixa(self):
        return self.__coordenada_caixa

    @property
    def nome_caixa(self):
        return self.__nome_caixa

    @property
    def tipo_caixa(self):
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

    def qnt_caixa(self, tipo):
        cont = 0
        for i in self.tipo_caixa.values():
            if tipo == i:
                cont += 1
        return cont
