
from elemento import Elemento
import re

class Cabo(Elemento):
    def __init__(self,arquivo):
        super().__init__(arquivo)
        self.__percuso = {}
        self.__comprimento = {}
        self._tipo_fibra = {}
        self.__osnap()
        # self.__fibras()

    # def __fibras(self):
    #     for i in self._nome_fibra:
    #         print(self._nome_fibra[i])


    def __osnap(self):
        all = {**self._coordenada_poste,**self._coordenada_pop}
        self.__percuso = self._coordenada_fibra
        for x in self._coordenada_fibra:
            for c,y in enumerate(self._coordenada_fibra[x]):
                for i in all:
                    if super().distancia(y,all[i]) <= 2:
                        self.__percuso[x][c] = i
                        break
                    else:
                        if super().distancia(y, all[i]) <= 10:
                            if type(self._coordenada_fibra[x][c]) == int:
                                break
                            self.__percuso[x][c] = i
    @property
    def comprimento_cabo(self, margem=3):
        p1 = 0
        distancia = 0
        all = {**self._coordenada_poste, **self._coordenada_pop}
        for i in self.__percuso:
            for d in self.__percuso[i]:
                if d == 'POP':
                    distancia += 80
                    p1 = all[d]
                if p1 == 0:
                    p1 = all[d]
                elif type(p1) == list and type(d) == int:
                    distancia += (super().distancia(p1, all[d]))*(1+(margem/100))
                    p1 = all[d]
                elif type(p1) == list and type(d) == list:
                    distancia += (super().distancia(p1, d))*(1+(margem/100))
                    p1 = d
            self.__comprimento[i] = round(distancia,2)
            distancia = 0
            p1 = 0
        return self.__comprimento
    @property
    def ceo(self):
        dados = {}
        distancia = 0
        poste_ceo = {**self.poste_por_elemento('CEO'),**self.poste_por_elemento('CEO-Futura')}
        for i in self.__percuso:
            for n,d in enumerate(self.__percuso[i]):
                for ceo in poste_ceo:
                    l1 = self._nome_elemento[ceo].split(';')
                    l2 = self._nome_fibra[i].split(';')
                    if d == poste_ceo[ceo] and l1[0]==l2[0] and l1[1]==l2[1] and l1[2]==l2[2] and l1[3]==l2[3]:
                        if n == 0 or n == (len(self.__percuso[i]) - 1):
                            distancia += 15
                        else:
                            distancia += 30
            dados[i] = round(distancia,2)
            distancia = 0
        return dados
    @property
    def reserva(self):
        dados = {}
        distancia = 0
        padrao = re.compile("[0-9]{2,3}")
        poste_reserva = self.poste_por_elemento('Reserva')
        for i in self.__percuso:
            for n, d in enumerate(self.__percuso[i]):
                for reserva in poste_reserva:
                    l1 = self._nome_elemento[reserva].split(';')
                    l2 = self._nome_fibra[i].split(';')
                    if d == poste_reserva[reserva] and l1[0]==l2[0] and l1[1]==l2[1] and l1[2]==l2[2] and l1[3]==l2[3]:
                        busca = padrao.search(self._nome_elemento[reserva])
                        if busca:
                            distancia += int(busca.group())
                        else:
                            distancia += 80
            dados[i] = round(distancia, 2)
            distancia = 0
        return dados
    @property
    def cto_hub(self):
        dados = {}
        distancia = 0
        poste_cto_hub = {**self.poste_por_elemento('CTO-HUB'), **self.poste_por_elemento('CTO-HUB-Futura')}
        for i in self.__percuso:
            for n, d in enumerate(self.__percuso[i]):
                for cto_hub in poste_cto_hub:
                    l1 = self._nome_elemento[cto_hub].split(';')
                    l2 = self._nome_fibra[i].split(';')
                    if d == poste_cto_hub[cto_hub] and l1[0] == l2[0] and l1[1] == l2[1]:
                        if n == 0 or n == (len(self.__percuso[i]) - 1):
                            distancia += 10
                        else:
                            distancia += 20
            dados[i] = round(distancia, 2)
            distancia = 0
        return dados

    @property
    def cto(self):
        dados = {}
        distancia = 0
        poste_cto = {**self.poste_por_elemento('CTO'), **self.poste_por_elemento('CTO-Futura')}
        for i in self.__percuso:
            for n, d in enumerate(self.__percuso[i]):
                for cto in poste_cto:
                    l1 = self._nome_elemento[cto].split(';')
                    l2 = self._nome_fibra[i].split(';')
                    if d == poste_cto[cto] and l1[0]==l2[0] and l1[1]==l2[1] and l1[2]==l2[2] and l1[3]==l2[3]:
                        if n == 0 or n == (len(self.__percuso[i]) - 1):
                            distancia += 10
                        else:
                            distancia += 20
            dados[i] = round(distancia, 2)
            distancia = 0
        return dados
    # def laco(self, poste):
    #     self.__dados = self.tratamento(poste)
    #     for i in self.__dados:
    #         laco = (len(self.__dados[i])-1)
    #         self.__quantidade_laco[i] = round(laco * 0.15)
    #     return self.__quantidade_laco
    #
    # def alca(self, poste):
    #     self.__dados = self.tratamento(poste)
    #     for i in self.__dados:
    #         alca = (len(self.__dados[i])-1)*2
    #         self.__quantidade_alca[i] = round(alca)
    #     return self.__quantidade_alca
    #
    # @property
    # def bap(self):
    #     self.__dados = self.__poste_tratado
    #     bap = []
    #     for i in self.__dados.values():
    #         for b in i:
    #             if type(b) == list:
    #                 continue
    #             bap.append(b)
    #     self.__quantidade_bap = len(set(bap))
    #     return self.__quantidade_bap
    #
    # @property
    # def nome(self):
    #     self.__nome_cabo = super().cabo_rede('nome')
    #     return self.__nome_cabo
    #

