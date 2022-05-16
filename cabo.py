
from elemento import Elemento
import re

class Cabo(Elemento):
    def __init__(self,arquivo):
        super().__init__(arquivo)
        self.__coordenadas = super().fibra_rede('linha')
        self.__percuso = super().fibra_rede('linha')
        # self.__nome_cabo = {}
        self.__comprimento = {}
        # self.__tipo_alca = {}
        # self.__tipo_laco = {}
        # self.__quantidade_alca = {}
        # self.__quantidade_laco = {}
        # self.__quantidade_bap = {}
        # self.__quantidade_de_fibra_no_cabo = {}
        # self.__vao_suportado = {}
        # self.__peso_do_cabo = {}
        # self.__diametro_externo = {}
        # self.__pressao_do_vento = {}
        self.__tratamento()

    @property
    def percuso(self):
        return self.__percuso
    @property
    def coordenadas(self):
        return self.__coordenadas
    def __tratamento(self):
        for x in self.__percuso:
            for c,y in enumerate(self.__percuso[x]):
                for i in self.coordenada_poste_pop:
                    if super().distancia(y,self.coordenada_poste_pop[i]) <= 2:
                        self.__percuso[x][c] = i
                        break
                    else:
                        if super().distancia(y, self.coordenada_poste_pop[i]) <= 10:
                            if type(self.__percuso[x][c]) == int:
                                break
                            self.__percuso[x][c] = i
    def comprimento_cabo(self, margem=3):
        p1 = 0
        distancia = 0
        for i in self.__percuso:
            for d in self.__percuso[i]:
                if d == 'POP':
                    distancia += 80
                    p1 = self.coordenada_poste_pop[d]
                if p1 == 0:
                    p1 = self.coordenada_poste_pop[d]
                elif type(p1) == list and type(d) == int:
                    distancia += (super().distancia(p1, self.coordenada_poste_pop[d]))*(1+(margem/100))
                    p1 = self.coordenada_poste_pop[d]
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
                for ceo in poste_ceo.values():
                    if d == ceo:
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
                    if d == poste_reserva[reserva]:
                        busca = padrao.search(self.nome_elemento[reserva])
                        if busca:
                            distancia += int(busca.group())
                        else:
                            distancia += 80
            dados[i] = round(distancia, 2)
            distancia = 0
        return dados

    # def cto_hub(self, poste):
    #     self.__dados = self.tratamento(poste)
    #     distancia = 0
    #     poste_cto_hub = self.__elemento.poste_cto_hub(poste)
    #     for i in self.__dados:
    #         for d in self.__dados[i]:
    #             for cto_hub in poste_cto_hub.values():
    #                 if d == cto_hub:
    #                     if i == 0 or i == len(self.__dados)-1:
    #                         distancia += 15
    #                     distancia += 30
    #         self.__comprimento[i] = round(distancia,2)
    #         distancia = 0
    #     return self.__comprimento
    #
    # def cto(self, poste):
    #     self.__dados = self.tratamento(poste)
    #     distancia = 0
    #     poste_cto = self.__elemento.poste_cto(poste)
    #     for i in self.__dados:
    #         for d in self.__dados[i]:
    #             for cto in poste_cto.values():
    #                 if d == cto:
    #                     if i == 0 or i == len(self.__dados) - 1:
    #                         distancia += 15
    #                     distancia += 30
    #         self.__comprimento[i] = round(distancia,2)
    #         distancia = 0
    #     return self.__comprimento
    #
    # def cto_futura(self, poste):
    #     self.__dados = self.tratamento(poste)
    #     distancia = 0
    #     poste_cto_futura = self.__elemento.poste_cto_futura(poste)
    #     for i in self.__dados:
    #         for d in self.__dados[i]:
    #             for cto_futura in poste_cto_futura.values():
    #                 if d == cto_futura:
    #                     if i == 0 or i == len(self.__dados) - 1:
    #                         distancia += 15
    #                     distancia += 30
    #         self.__comprimento[i] = round(distancia,2)
    #         distancia = 0
    #     return self.__comprimento
    #
    # def comprimento_cabo(self, margem=0.03):
    #     self.__dados = self.__poste_tratado
    #
    #     p1 = 0
    #     distancia = 0
    #     for i in self.__dados:
    #         for d in self.__dados[i]:
    #             if d == 'POP':
    #                 distancia += 80
    #                 p1 = self.__poste[d]
    #             if p1 == 0:
    #                 p1 = self.__poste[d]
    #             elif type(p1) == list and type(d) == int:
    #                 distancia += (super().distancia(p1, self.__poste[d]))*(1+margem)
    #                 p1 = self.__poste[d]
    #             elif type(p1) == list and type(d) == list:
    #                 distancia += (super().distancia(p1, d))*(1+margem)
    #                 p1 = d
    #         self.__comprimento[i] = round(distancia,2)
    #         distancia = 0
    #         p1 = 0
    #     return self.__comprimento
    #
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

