from cabo import Cabo
import re

class Equipamento(Cabo):
    def __init__(self, arquivo):
        super().__init__(arquivo)
        self._spliter = []
        self._bandeja = []

    def cont_spl(self,rex,lista):
        c = 0
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

    def spliter(self):
        spl_hub = self.nome_por_elemento('HUB-DPR')
        spl_cto_hub = self.nome_por_elemento('CTO-HUB')
        spl_cto = self.nome_por_elemento('CTO')
        spl = {**spl_cto_hub,**spl_hub,**spl_cto}
        spl_conecto_1x8 = re.compile("[A-Z]{2}[.][0-9]{1,2}[.][0-9]{1,2}[.][0-9]{1,2}[ ]?[/|][ ]?[A-Z]{1,2}[.][0-9]{1,2}[.][0-9]{1,2}[.][0-9]{1,2}")
        spl_nc_1x2 = re.compile("[0-9]{1,2}['][1]")
        spl_nc_1x8 = re.compile("[0-9]{1,2}['][2]")
        # spl_nc_1x16 = re.compile("[0-9]")
        conecto_1x8 = "DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X8 G.657A NC-SC/APC 0.9M/0.6M"
        nc_1x2 = "DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X2 G.657A NC-NC 250UM 2M/2M"
        nc_1x8 = "DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X8 G.657A NC-NC 250UM 2M/2M"
        # nc_1x16 = f"DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X16 G.657A NC-NC 250UM 2M/2M"
        self._spliter.append([conecto_1x8,self.cont_spl(spl_conecto_1x8, spl)])
        self._spliter.append([nc_1x2,self.cont_spl(spl_nc_1x2, spl)])
        self._spliter.append([nc_1x8,self.cont_spl(spl_nc_1x2, spl)+self.cont_spl(spl_nc_1x8, spl)])
        # self._spliter.append(f'{conecto_1x8} - {self.cont_spl(spl_conecto_1x8, spl)} und')
        return self._spliter

    def cont_bandeja(self,rex,lista):
        c = 0
        for i in lista:
            busca = rex.findall(lista[i])
            print(busca)
            if len(busca) > 0:
                c += 1
        return c

    def bandeja_cto(self):
        cto_hub = {**self.nome_por_elemento('CTO-HUB')}
        bandeja_esd = re.compile("[.][0-9]{1,2}[']?[1-2]?[-]")
        bandeja_drt = re.compile("[-][0-9]{1,2}[']?[1-2]?[.]")
        bdj = "BANDEJA INFERIOR PARA CTO PRESLEY"
        self._bandeja.append([bdj,self.cont_bandeja(bandeja_esd,cto_hub)])
        self._bandeja.append([bdj, self.cont_bandeja(bandeja_drt, cto_hub)])
        return self._bandeja