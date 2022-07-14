import re


class Rede:
    def __init__(self, name):
        self._pon = name
        self._cto = []
        self._qnt_cto = []
        self._activated = False
        self._topology = ""
        self._spl = []

    @property
    def name(self):
        return self._pon

    @property
    def cto(self):
        return self._cto

    @cto.setter
    def cto(self, value):
        self._cto.append(value)

    @property
    def activated(self):
        for i in self.cto:
            if i.type == 'CTO' or i.type == 'CTO-Indoor':
                self._activated = True
                return self._activated

    @property
    def spl_rede(self):
        cto_16p = re.compile("[A-Z]{2}[.][0-9]{1,2}[.][0-9]{1,2}[.][0-9]{1,2}[ ]?[-]?[ ]?[16pP]{3}")
        cto_8p = re.compile("[A-Z]{2}[.][0-9]{1,2}[.][0-9]{1,2}[.][0-9]{1,2}")
        if self.activated:
            for i in self.cto:
                if "'2" in i.name:
                    self._spl.append("DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X2 G.657A NC-NC 250UM 2M/2M")
                    self._spl.append("DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X8 G.657A NC-NC 250UM 2M/2M")
                    self._spl.append("DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X8 G.657A NC-NC 250UM 2M/2M")
                    self._topology = "1x2 1x8 1x8"
                search_16p = cto_16p.findall(i.name)
                search_8p = cto_8p.findall(i.name)
                for sp16 in search_16p:
                    if sp16:
                        self._spl.append("DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X16 G.657A NC-SC/APC 900UM 0.9M/0.6M")
                        self._qnt_cto.append(sp16)
                if len(search_8p) == 2:
                    self._spl.append("DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X8 G.657A NC-SC/APC 0.9M/0.6M")
                    [self._spl.append("ADAPTADOR ÓPTICO SM SIMPLEX SC/APC") for i in range(8)]
                for sp8 in search_8p:
                    if sp8:
                        self._qnt_cto.append(sp8)
            if not self._topology:
                if len(self._qnt_cto) <= 8:
                    self._spl.append("DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X8 G.657A NC-NC 250UM 2M/2M")
                    self._topology = "1x8"
                else:
                    self._spl.append("DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X16 G.657A NC-NC 250UM 2M/2M")
                    self._topology = "1x16"
        return self._spl
