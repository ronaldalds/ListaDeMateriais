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
        lista = {**self.nome_por_elemento('CTO-HUB'),**self.nome_por_elemento('HUB-DPR')}
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
                            topologia = []
                            for cto_rede in self._nome_elemento.values():
                                if r[0] == cto_rede[0] and r[2] == cto_rede[2] and r[3] == cto_rede[3]:
                                    topologia.append(cto_rede[-1])

                            if "'1" not in s:
                                if len(topologia) > 8:
                                    topologia = '1x16'
                                else:
                                    topologia = '1x8'
                            else:
                                topologia = "1x2 1x8 1x8"
                            self._rede_ativa_cto_hub.append([r[0], r[2], r[3],topologia])

    def cont_spl(self,rex):
        c = []
        spl_hub = self.nome_por_elemento('HUB-DPR')
        spl_cto_hub = self.nome_por_elemento('CTO-HUB')
        spl_cto = self.nome_por_elemento('CTO')
        lista = {**spl_cto_hub, **spl_hub, **spl_cto}
        for i in lista:
            busca = rex.findall(lista[i])
            if len(busca) > 0:
                if "'2" in busca[0]:
                    c.append(lista[i])
                else:
                    for f in self._ra:
                        for s in busca:
                            t1 = self._poste_elemento[i]
                            t2 = self._percuso[f]
                            t3 = s.split("'")[0]
                            if ((t1 == t2[0]) or (t1 == t2[-1])) and (t3 in self._nome_fibra[f][3]):
                                c.append(lista[i])
        return c

    def spliter_con_1x8(self):
        padrao = re.compile(
"[A-Z]{2}[.][0-9]{1,2}[.][0-9]{1,2}[.][0-9]{1,2}[ ]?[/|][ ]?[A-Z]{1,2}[.][0-9]{1,2}[.][0-9]{1,2}[.][0-9]{1,2}")
        cto_hub = self.nome_por_elemento('CTO-HUB')
        cto = self.nome_por_elemento('CTO')
        lista = {**cto_hub, **cto}
        spl_con_1x8 = []
        for i in lista:
            busca = padrao.findall(lista[i])
            if len(busca) > 0:
                spl_con_1x8.append(busca)
        return spl_con_1x8

    def spliter_nc_1x16(self):
        nc_1x16 = []
        for i in self._rede_ativa_cto_hub:
            if "1x16" == i[-1]:
                nc_1x16.append(i)
        return nc_1x16

    def spliter_nc_1x2(self):
        spl_nc_1x2 = re.compile("[0-9]{1,2}['][1]")
        return self.cont_spl(spl_nc_1x2)

    def spliter_nc_1x8(self):
        spl_nc_1x8 = re.compile("[0-9]{1,2}['][1-2]")
        nc_1x8 = self.cont_spl(spl_nc_1x8)
        for i in self._rede_ativa_cto_hub:
            if "1x8" == i[-1]:
                nc_1x8.append(i)
        return nc_1x8

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

    def tubete_45(self):
        padrao_fibra = re.compile("[0-9]{1,2}[0-9]?[fF]")
        ceo = {**self.poste_por_elemento("CEO"),**self.poste_por_elemento("HUB-DPR"),**self.poste_por_elemento("CTO-HUB")}
        fusao_ceo_hub = 0

        for i in self._alimentador:
            for c in ceo:
                if ceo[c] == self._percuso[i][0] or ceo[c] == self._percuso[i][-1]:
                    fusoes = padrao_fibra.search(self._alimentador[i][-1])
                    f = int(re.sub('[^0-9]','',fusoes.group()))
                    fusao_ceo_hub += f
                    # print(self._nome_elemento[c][-1],f)
                    break

        rede = len(self._rede_ativa_cto_hub)
        # print(rede)
        spl_nc_1x2 = self.spliter_nc_1x2()
        # print(spl_nc_1x2)
        spl_nc_1x8 = self.spliter_nc_1x8() * 9
        # print(spl_nc_1x8)
        cto_ativa = len(self.coordenada_por_elemento("CTO"))
        # print(cto_ativa)
        spl_con_1x8 = self.spliter_con_1x8()
        # print(spl_con_1x8)
        tubetes = fusao_ceo_hub + rede + spl_nc_1x2 + spl_nc_1x8 + cto_ativa + spl_con_1x8

        return tubetes