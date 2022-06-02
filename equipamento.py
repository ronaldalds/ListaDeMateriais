from cabo import Cabo
import re
import math

class Equipamento(Cabo):
    def __init__(self, arquivo):
        super().__init__(arquivo)
        self._spliter = []
        self._bandeja = []
        self._rede_ativa_cto_hub = []
        self._bap_lancamento = []
        self._bap_fusao = 0
        self.rede_cto_hub()

    def rede_cto_hub(self):
        lista = {**self.nome_por_elemento('CTO-HUB')}
        padrao_hub = re.compile("[A-Z]{2}[.][0-9]{1,2}[']?[1-2]?[-][0-9]{1,2}[']?[1-2]?[-]?[0-9]{1,2}?[']?[1-2]?")
        padrao_rede = re.compile("[0-9]{1,2}[']?[1-2]?")
        for i in lista:
            busca = padrao_hub.findall(lista[i])
            if len(busca) > 0:
                rede = padrao_rede.findall(busca[0])
                for f in self._ra:
                    for s in rede:
                        t1 = self._poste_elemento[i]
                        t2 = self._percuso[f]
                        t3 = s.split("'")[0]
                        if ((t1 == t2[0]) or (t1 == t2[-1])) and (t3 in self._nome_fibra[f][3]):
                            r = self._nome_fibra[f]
                            self._rede_ativa_cto_hub.append([r[0], r[2], r[3]])

    def cont_spl(self,rex):
        c = 0
        spl_hub = self.nome_por_elemento('HUB-DPR')
        spl_cto_hub = self.nome_por_elemento('CTO-HUB')
        spl_cto = self.nome_por_elemento('CTO')
        lista = {**spl_cto_hub, **spl_hub, **spl_cto}
        for i in lista:
            busca = rex.findall(lista[i])
            if len(busca) > 0:
                if "'2" in busca[0]:
                    c += 1
                elif len(busca[0].split("'")[0]) > 5:
                    c += 1
                else:
                    for f in self._ra:
                        for s in busca:
                            t1 = self._poste_elemento[i]
                            t2 = self._percuso[f]
                            t3 = s.split("'")[0]
                            if ((t1 == t2[0]) or (t1 == t2[-1])) and (t3 in self._nome_fibra[f][3]):
                                c += 1
        return c

    def spliter_con_1x8(self):
        spl_conecto_1x8 = re.compile("[A-Z]{2}[.][0-9]{1,2}[.][0-9]{1,2}[.][0-9]{1,2}[ ]?[/|][ ]?[A-Z]{1,2}[.][0-9]{1,2}[.][0-9]{1,2}[.][0-9]{1,2}")
        conecto_1x8 = "DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X8 G.657A NC-SC/APC 0.9M/0.6M"
        return self.cont_spl(spl_conecto_1x8)

    def spliter_nc_1x2(self):
        spl_nc_1x2 = re.compile("[0-9]{1,2}['][1]")
        nc_1x2 = "DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X2 G.657A NC-NC 250UM 2M/2M"
        return self.cont_spl(spl_nc_1x2)

    def spliter_nc_1x8(self):
        spl_nc_1x8 = re.compile("[0-9]{1,2}['][1-2]")
        nc_1x8 = "DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X8 G.657A NC-NC 250UM 2M/2M"
        return self.cont_spl(spl_nc_1x8)

    def bandeja_cto_hub(self):
        return len(self._rede_ativa_cto_hub)

    @property
    def plaqueta_lancamento(self):
        for i in self._coordenada_fibra:
            self._plaqueta_lancamento += (len(self._coordenada_fibra[i]) - 1)
        return self._plaqueta_lancamento

    @property
    def plaqueta_fusao(self):
        return self._plaqueta_fusao

    def bap_lancamento(self):
        for i in self._percuso.values():
            for t in i:
                if t not in self._bap_lancamento:
                    self._bap_lancamento.append(t)
        return len(self._bap_lancamento)

    def bap_fusao(self):
        b1 = self.poste_por_elemento('CTO')
        b2 = self.poste_por_elemento('CTO-HUB')
        self._bap_fusao = len({**b1,**b2})*2
        return self._bap_fusao

    def fio_lancamento(self):
        cordoalha = self.cabo()['CDLH']*1.3
        plaqueta = self._plaqueta_lancamento*0.3
        ceo = self.contador('CEO')*2 + self.contador('HUB-DPR')*2
        rt = self.contador('Reserva')*2
        fio_espina = cordoalha + plaqueta + ceo + rt
        return math.ceil(fio_espina/130)

    def fio_fusao(self):
        plaqueta = self._plaqueta_fusao*0.3
        cto = self.contador('CTO')*1
        fio_espina = plaqueta + cto
        return math.ceil(fio_espina/130)

    def prensa_cabo(self):
        prensa_reserva = self.contador('Reserva') * 2
        prensa_ceo = self.contador('CEO') * 2
        prensa = prensa_ceo + prensa_reserva
        return prensa

    def tubete(self):
        padrao_fibra = re.compile("[0-9]{1,2,3}[fF]")
        ceo = {**self.poste_por_elemento("CEO"),**self.poste_por_elemento("HUB-DPR"),**self.poste_por_elemento("CTO-HUB")}
        for i in self._alimentador:
            # print(self._percuso[i])
            # for n,f in enumerate(self._percuso[i]):
            for c in ceo.values():
                if c == self._percuso[i][0] or c == self._percuso[i][-1]:
                    print(c,i,self._percuso[i],self._alimentador[i][-1])

            # print(i)
        rede = len(self._rede_ativa_cto_hub)
        spl_nc_1x2 = self.spliter_nc_1x2()
        spl_nc_1x8 = self.spliter_nc_1x8() * 9

        return ceo