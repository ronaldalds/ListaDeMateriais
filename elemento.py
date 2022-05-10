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
        self.__coordenada_elemento = super().ext_elemento('coordenada')
        for x in self.__coordenada_elemento:
            for i in poste:
                if super().distancia(self.__coordenada_elemento[x], poste[i]) <= 2:
                    self.__coordenada_elemento[x] = i
                    break
        return self.__coordenada_elemento

    def __separador(self):
        self.__tipo_elemento = super().ext_elemento('style')
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
        self.__coordenada_elemento = super().ext_elemento('coordenada')
        return self.__coordenada_elemento

    @property
    def nome_elemento(self):
        self.__nome_elemento = super().ext_elemento('nome')
        return self.__nome_elemento

    @property
    def tipo_elemento(self):
        self.__tipo = self.__separador()
        return self.__tipo

    @property
    def coordenada_reserva(self):
        self.__dados = {}
        for i in self.tipo_elemento:
            if self.tipo_elemento[i] == 'Reserva':
                self.__dados[i] = self.coordenada_elemento[i]
        return self.__dados

    def poste_reserva(self,poste):
        self.__dados = {}
        for i in self.tipo_elemento:
            if self.tipo_elemento[i] == 'Reserva':
                self.__dados[i] = self.tratamento(poste)[i]
        return self.__dados

    @property
    def coordenada_ceo(self):
        self.__dados = {}
        for i in self.tipo_elemento:
            if self.tipo_elemento[i] == 'CEO':
                self.__dados[i] = self.coordenada_elemento[i]
        return self.__dados

    def poste_ceo(self,poste):
        self.__dados = {}
        for i in self.tipo_elemento:
            if self.tipo_elemento[i] == 'CEO':
                self.__dados[i] = self.tratamento(poste)[i]
        return self.__dados

    @property
    def coordenada_cto_hub(self):
        self.__dados = {}
        for i in self.tipo_elemento:
            if self.tipo_elemento[i] == 'CTO-HUB':
                self.__dados[i] = self.coordenada_elemento[i]
        return self.__dados

    def poste_cto_hub(self,poste):
        self.__dados = {}
        for i in self.tipo_elemento:
            if self.tipo_elemento[i] == 'CTO-HUB':
                self.__dados[i] = self.tratamento(poste)[i]
        return self.__dados

    @property
    def coordenada_cto(self):
        self.__dados = {}
        for i in self.tipo_elemento:
            if self.tipo_elemento[i] == 'CTO':
                self.__dados[i] = self.coordenada_elemento[i]
        return self.__dados

    def poste_cto(self,poste):
        self.__dados = {}
        for i in self.tipo_elemento:
            if self.tipo_elemento[i] == 'CTO':
                self.__dados[i] = self.tratamento(poste)[i]
        return self.__dados

    @property
    def coordenada_cto_futura(self):
        self.__dados = {}
        for i in self.tipo_elemento:
            if self.tipo_elemento[i] == 'CTO-Futura':
                self.__dados[i] = self.coordenada_elemento[i]
        return self.__dados

    def poste_cto_futura(self,poste):
        self.__dados = {}
        for i in self.tipo_elemento:
            if self.tipo_elemento[i] == 'CTO-Futura':
                self.__dados[i] = self.tratamento(poste)[i]
        return self.__dados

    def contador(self, tipo):
        cont = 0
        for i in self.__tipo.values():
            if tipo == i:
                cont += 1
        return cont