
from elemento import Elemento
import re

class Cabo(Elemento):
    def __init__(self,arquivo):
        super().__init__(arquivo)
        self._percuso = {}
        self.__comprimento = {}
        self._tipo_fibra = {}
        self.__ceo = {}
        self.__reserva = {}
        self.__cto_hub = {}
        self.__cto = {}
        self.__quantidade_laco = {}
        self.__quantidade_alca = {}
        self.__quantidade_bap = []
        self.__osnap_cabo()

    def somador(self, tipo, qnt):
        dados = {}
        for i in qnt:
            try:
                dados[tipo[i]] += qnt[i]
            except:
                dados[tipo[i]] = qnt[i]

        return dados

    def tipo_fibras(self):
        padrao = re.compile("[0-9]{1,2}[Ff]")
        for i in self._nome_fibra:
            if "REDE" in self._nome_fibra[i].upper():
                self._tipo_fibra[i] = self._nome_fibra[i]
                busca = padrao.search(self._nome_fibra[i].upper())
                if busca:
                    if busca.group() == '12F':
                        self._tipo_fibra[i] = 'CFOA-SM-ASU80-S 12F MINI-RA'
                    elif busca.group() == '06F':
                        self._tipo_fibra[i] = 'CFOA-SM-ASU80-S 06F MINI-RA'
                    else:
                        self._tipo_fibra[i] = self._nome_fibra[i]
            else:
                self._tipo_fibra[i] = self._nome_fibra[i].split(';')[4].split('|')[2].strip()
        return self._tipo_fibra

    def __osnap_cabo(self):
        all = {**self._coordenada_poste,**self._coordenada_pop}
        self._percuso = self._coordenada_fibra
        for x in self._coordenada_fibra:
            for c,y in enumerate(self._coordenada_fibra[x]):
                for i in all:
                    if super().distancia(y,all[i]) <= 2:
                        self._percuso[x][c] = i
                        break
                    else:
                        if super().distancia(y, all[i]) <= 10:
                            if type(self._coordenada_fibra[x][c]) == int:
                                break
                            self._percuso[x][c] = i

    def comprimento_cabo(self):
        self.ceo()
        self.reserva()
        self.cto_hub()
        self.cto()
        p1 = 0
        distancia = 0
        all = {**self._coordenada_poste, **self._coordenada_pop}
        for i in self._percuso:
            for d in self._percuso[i]:
                try:
                    pt = all[d]
                except:
                    pt = d
                if d == 'POP':
                    distancia += 80
                    p1 = pt
                if p1 == 0:
                    p1 = pt
                distancia += (super().distancia(p1, pt)) * 1.03
                p1 = pt
            equipamento = self.__ceo[i]+self.__reserva[i]+self.__cto_hub[i]+self.__cto[i]
            self.__comprimento[i] = round(distancia,2) + equipamento
            distancia = 0
            p1 = 0
        return self.__comprimento

    def ceo(self):
        distancia = 0
        poste_ceo = {**self.poste_por_elemento('CEO'),**self.poste_por_elemento('CEO-Futura')}
        for i in self._percuso:
            for n,d in enumerate(self._percuso[i]):
                for ceo in poste_ceo:
                    l1 = self._nome_elemento[ceo].split(';')
                    l2 = self._nome_fibra[i].split(';')
                    if d == poste_ceo[ceo] and l1[0]==l2[0] and l1[1]==l2[1] and l1[2]==l2[2] and l1[3]==l2[3]:
                        if n == 0 or n == (len(self._percuso[i]) - 1):
                            distancia += 15
                        else:
                            distancia += 30
            self.__ceo[i] = round(distancia,2)
            distancia = 0
        return self.__ceo

    def reserva(self):
        distancia = 0
        padrao = re.compile("[0-9]{2,3}")
        poste_reserva = self.poste_por_elemento('Reserva')
        for i in self._percuso:
            for n, d in enumerate(self._percuso[i]):
                for reserva in poste_reserva:
                    l1 = self._nome_elemento[reserva].split(';')
                    l2 = self._nome_fibra[i].split(';')
                    if d == poste_reserva[reserva] and l1[0]==l2[0] and l1[1]==l2[1] and l1[2]==l2[2] and l1[3]==l2[3]:
                        busca = padrao.search(self._nome_elemento[reserva])
                        if busca:
                            distancia += int(busca.group())
                        else:
                            distancia += 80
            self.__reserva[i] = round(distancia, 2)
            distancia = 0
        return self.__reserva

    def cto_hub(self):
        distancia = 0
        poste_cto_hub = {**self.poste_por_elemento('CTO-HUB'), **self.poste_por_elemento('CTO-HUB-Futura')}
        for i in self._percuso:
            for n, d in enumerate(self._percuso[i]):
                for cto_hub in poste_cto_hub:
                    l1 = self._nome_elemento[cto_hub].split(';')
                    l2 = self._nome_fibra[i].split(';')
                    if d == poste_cto_hub[cto_hub] and l1[0] == l2[0] and l1[1] == l2[1]:
                        if n == 0 or n == (len(self._percuso[i]) - 1):
                            distancia += 10
                        else:
                            distancia += 20
            self.__cto_hub[i] = round(distancia, 2)
            distancia = 0
        return self.__cto_hub

    def cto(self):
        distancia = 0
        poste_cto = {**self.poste_por_elemento('CTO'), **self.poste_por_elemento('CTO-Futura')}
        for i in self._percuso:
            for n, d in enumerate(self._percuso[i]):
                for cto in poste_cto:
                    l1 = self._nome_elemento[cto].split(';')
                    l2 = self._nome_fibra[i].split(';')
                    if d == poste_cto[cto] and l1[0]==l2[0] and l1[1]==l2[1] and l1[2]==l2[2] and l1[3]==l2[3]:
                        if n == 0 or n == (len(self._percuso[i]) - 1):
                            distancia += 10
                        else:
                            distancia += 20
            self.__cto[i] = round(distancia, 2)
            distancia = 0
        return self.__cto

    @property
    def laco(self):
        for i in self._coordenada_fibra:
            laco = len(self._coordenada_fibra[i])
            self.__quantidade_laco[i] = round(laco * 0.15)
        return self.__quantidade_laco
    @property
    def alca(self):
        for i in self._coordenada_fibra:
            laco = (len(self._coordenada_fibra[i]) - 1)
            self.__quantidade_alca[i] = round(laco * 2)
        return self.__quantidade_alca
    @property
    def bap(self):
        for i in self._percuso.values():
            for t in i:
                if t not in self.__quantidade_bap:
                    self.__quantidade_bap.append(t)
        return self.__quantidade_bap
    @property
    def nome(self):
        return self._nome_fibra

