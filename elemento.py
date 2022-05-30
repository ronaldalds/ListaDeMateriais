from poste import Poste
import re


class Elemento(Poste):
    def __init__(self, arquivo):
        super().__init__(arquivo)
        self._coordenada_pop = {'POP': None}
        self._nome_pop = {'POP': None}
        self._elemento_poste = {}
        self.__separador()
        self.__ext_pop()
        self.osnap_elemento()

    def spliter(self):
        spl = {**self.nome_por_elemento('CEO'),**self.nome_por_elemento('CTO'), **self.nome_por_elemento('CTO-HUB')}
        print(spl)
        dados = []
        spl_conecto_1x8 = re.compile("[A-Z]{2}[.][0-9]{1,2}[.][0-9]{1,2}[.][0-9]{1,2}[ ]?[/|][ ]?[A-Z]{1,2}[.][0-9]{1,2}[.][0-9]{1,2}[.][0-9]{1,2}")
        spl_conecto_1x16 = re.compile("[0-9]")
        spl_nc_1x2 = re.compile("[0-9]")
        spl_nc_1x8 = re.compile("[0-9]")
        spl_nc_1x16 = re.compile("[0-9]")
        for i in spl:
            busca_conector_1x8 = spl_conecto_1x8.search(spl[i])
            if busca_conector_1x8:
                dados.append("DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X8 G.657A NC-SC/APC 0.9M/0.6M")
        return len(dados)
    def __ext_pop(self):
        for pop in self._root.iter(f'{self._site}Placemark'):
            if 'shapes/ranger_station.pngff0000ff' in self.style[pop.findtext(f'{self._site}styleUrl').replace('#', '')]:
                self._nome_pop['POP'] = pop.findtext(f'{self._site}name')
                for c in pop.iter(f'{self._site}Point'):
                    self._coordenada_pop['POP'] = c.findtext(f'{self._site}coordinates').split(',')
                break

    def osnap_elemento(self):
        for x in self._coordenada_elemento:
            for i in self._coordenada_poste:
                if super().distancia(self._coordenada_elemento[x], self._coordenada_poste[i]) <= 2:
                    self._elemento_poste[x] = i
                    break
                else:
                    self._elemento_poste[x] = self._coordenada_elemento[x]

    def __separador(self):
        for tipo in self._tipo_elemento:
            if 'shapes/donut.pngff00ff00' in self.style[self._tipo_elemento[tipo]]:
                self._tipo_elemento[tipo] = 'CEO'
            elif 'shapes/donut.pngff00ffff' in self.style[self._tipo_elemento[tipo]]:
                self._tipo_elemento[tipo] = 'CEO-Futura'
            elif 'shapes/donut.pngff0000ff' in self.style[self._tipo_elemento[tipo]]:
                self._tipo_elemento[tipo] = 'HUB-DPR'
            elif 'shapes/polygon.png' in self.style[self._tipo_elemento[tipo]]:
                self._tipo_elemento[tipo] = 'Reserva'
            elif 'shapes/square.pngff0000ff' in self.style[self._tipo_elemento[tipo]]:
                self._tipo_elemento[tipo] = 'CTO-HUB'
            elif 'shapes/square.pngff00ffff' in self.style[self._tipo_elemento[tipo]]:
                self._tipo_elemento[tipo] = 'CTO-HUB-Futura'
            elif 'paddle/red-diamond.png' in self.style[self._tipo_elemento[tipo]]:
                self._tipo_elemento[tipo] = 'CTO'
            elif 'paddle/ltblu-diamond.png' in self.style[self._tipo_elemento[tipo]]:
                self._tipo_elemento[tipo] = 'CTO-Indoor'
            elif 'paddle/ylw-diamond.png' in self.style[self._tipo_elemento[tipo]]:
                self._tipo_elemento[tipo] = 'CTO-Futura'
            elif 'shapes/ranger_station.png' in self.style[self._tipo_elemento[tipo]]:
                self._tipo_elemento[tipo] = 'POP'

    def coordenada_por_elemento(self, elemento):
        dados = {}
        for i in self._tipo_elemento:
            if self._tipo_elemento[i] == elemento:
                dados[i] = self._coordenada_elemento[i]
        return dados

    def poste_por_elemento(self, elemento):
        dados = {}
        for i in self._tipo_elemento:
            if self._tipo_elemento[i] == elemento:
                dados[i] = self._elemento_poste[i]
        return dados

    def nome_por_elemento(self, elemento):
        dados = {}
        for i in self._tipo_elemento:
            # for t in elemento: # trabalhar com solicitação em lista
            if self._tipo_elemento[i] == elemento:
                dados[i] = self._nome_elemento[i][-1]
        return dados

    def contador(self, elemento):
        cont = 0
        for i in self._tipo_elemento.values():
            if elemento == i:
                cont += 1
        return cont

    @property
    def nome(self):
        return self._nome_elemento
