from projeto import Projeto
from elemento import Elemento
import re
from poste import Poste
class Cabo(Projeto):
    def __init__(self,arquivo):
        super().__init__(arquivo)
        self.__percuso = {}
        self.__nome_cabo = {}
        self.__comprimento = {}
        self.__tipo_alca = {}
        self.__tipo_laco = {}
        self.__quantidade_alca = {}
        self.__quantidade_laco = {}
        self.__quantidade_bap = {}
        self.__quantidade_de_fibra_no_cabo = {}
        self.__vao_suportado = {}
        self.__peso_do_cabo = {}
        self.__diametro_externo = {}
        self.__pressao_do_vento = {}
        self.__elemento = Elemento(arquivo)
        self.__poste_tratado = self.tratamento


    @property
    def poste_tratado(self):
        return self.__poste_tratado


    def tratamento(self, poste):
        self.__dados = super().cabo_rede('linha')
        for x in self.__dados:
            for c,y in enumerate(self.__dados[x]):
                for i in poste:
                    if super().distancia(y,poste[i]) <= 2:
                        self.__dados[x][c] = i
                        break
                    else:
                        if super().distancia(y, poste[i]) <= 10:
                            if self.__dados[x][c] == type(int):
                                break
                            self.__dados[x][c] = i
        return self.__dados

    def ceo(self, poste):
        self.__dados = self.tratamento(poste)
        distancia = 0
        poste_ceo = self.__elemento.poste_ceo(poste)
        for i in self.__dados:
            for d in self.__dados[i]:
                for ceo in poste_ceo.values():
                    if d == ceo:
                        distancia += 15
            self.__comprimento[i] = round(distancia,2)
            distancia = 0
        return self.__comprimento

    def reserva(self, poste):
        self.__dados = self.tratamento(poste)
        distancia = 0
        padrao = re.compile("[0-9]{2,3}")
        nome_reserva = self.__elemento.nome_elemento
        poste_reserva = self.__elemento.poste_reserva(poste)
        for i in self.__dados:
            for d in self.__dados[i]:
                for reserva in poste_reserva:
                    if d == poste_reserva[reserva]:
                        busca = padrao.search(nome_reserva[reserva])
                        if busca:
                            distancia += int(busca.group())
                        else:
                            distancia += 80
            self.__comprimento[i] = round(distancia,2)
            distancia = 0
        return self.__comprimento

    def cto_hub(self, poste):
        self.__dados = self.tratamento(poste)
        distancia = 0
        poste_cto_hub = self.__elemento.poste_cto_hub(poste)
        for i in self.__dados:
            for d in self.__dados[i]:
                for cto_hub in poste_cto_hub.values():
                    if d == cto_hub:
                        if i == 0 or i == len(self.__dados)-1:
                            distancia += 15
                        distancia += 30
            self.__comprimento[i] = round(distancia,2)
            distancia = 0
        return self.__comprimento

    def cto(self, poste):
        self.__dados = self.tratamento(poste)
        distancia = 0
        poste_cto = self.__elemento.poste_cto(poste)
        for i in self.__dados:
            for d in self.__dados[i]:
                for cto in poste_cto.values():
                    if d == cto:
                        if i == 0 or i == len(self.__dados) - 1:
                            distancia += 15
                        distancia += 30
            self.__comprimento[i] = round(distancia,2)
            distancia = 0
        return self.__comprimento

    def cto_futura(self, poste):
        self.__dados = self.tratamento(poste)
        distancia = 0
        poste_cto_futura = self.__elemento.poste_cto_futura(poste)
        for i in self.__dados:
            for d in self.__dados[i]:
                for cto_futura in poste_cto_futura.values():
                    if d == cto_futura:
                        if i == 0 or i == len(self.__dados) - 1:
                            distancia += 15
                        distancia += 30
            self.__comprimento[i] = round(distancia,2)
            distancia = 0
        return self.__comprimento

    def comprimento_cabo(self, margem=0.03):
        self.__dados = self.__poste_tratado

        p1 = 0
        distancia = 0
        for i in self.__dados:
            for d in self.__dados[i]:
                if d == 'POP':
                    distancia += 80
                    p1 = self.__poste[d]
                if p1 == 0:
                    p1 = self.__poste[d]
                elif type(p1) == list and type(d) == int:
                    distancia += (super().distancia(p1, self.__poste[d]))*(1+margem)
                    p1 = self.__poste[d]
                elif type(p1) == list and type(d) == list:
                    distancia += (super().distancia(p1, d))*(1+margem)
                    p1 = d
            self.__comprimento[i] = round(distancia,2)
            distancia = 0
            p1 = 0
        return self.__comprimento

    def laco(self, poste):
        self.__dados = self.tratamento(poste)
        for i in self.__dados:
            laco = (len(self.__dados[i])-1)
            self.__quantidade_laco[i] = round(laco * 0.15)
        return self.__quantidade_laco

    def alca(self, poste):
        self.__dados = self.tratamento(poste)
        for i in self.__dados:
            alca = (len(self.__dados[i])-1)*2
            self.__quantidade_alca[i] = round(alca)
        return self.__quantidade_alca

    @property
    def bap(self):
        self.__dados = self.__poste_tratado
        bap = []
        for i in self.__dados.values():
            for b in i:
                if type(b) == list:
                    continue
                bap.append(b)
        self.__quantidade_bap = len(set(bap))
        return self.__quantidade_bap

    @property
    def nome(self):
        self.__nome_cabo = super().cabo_rede('nome')
        return self.__nome_cabo

    @property
    def percuso(self):
        self.__percuso = super().cabo_rede('linha')
        return self.__percuso
