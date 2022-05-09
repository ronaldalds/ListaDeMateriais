import xml.etree.ElementTree as Et
from math import sqrt


class Projeto:
    def __init__(self, arquivo):
        doc = Et.parse(arquivo)
        self.__root = doc.getroot()
        self.__site = '{http://www.opengis.net/kml/2.2}'
        self.__tipo_style = self.ext_style

    @property
    def ext_style(self):
        self.__dados = {}
        for root in self.__root.iter(f'{self.__site}Style'):
            for icon in root.iter(f'{self.__site}Icon'):
                trato_tipo = icon.findtext(f'{self.__site}href').replace('http://maps.google.com/mapfiles/kml/', '')
                self.__dados[root.attrib['id']] = trato_tipo
        for root2 in self.__root.iter(f'{self.__site}StyleMap'):
            for pair in root2.iter(f'{self.__site}Pair'):
                if 'normal' in pair.findtext(f'{self.__site}key'):
                    trato_url = pair.findtext(f'{self.__site}styleUrl').replace('#', '')
                    self.__dados[root2.attrib['id']] = self.__dados[trato_url]
        return self.__dados

    @property
    def ext_pop(self):
        self.__dados = {'POP': None}
        for root in self.__root.iter(f'{self.__site}Folder'):
            for pop in root.iter(f'{self.__site}Placemark'):
                if 'shapes/ranger_station.png' in self.__tipo_style[
                    pop.findtext(f'{self.__site}styleUrl').replace('#', '')]:
                    for c in pop.iter(f'{self.__site}Point'):
                        self.__dados['POP'] = c.findtext(f'{self.__site}coordinates').split(',')
                        break
                    break
                break
        return self.__dados

    def ext_cabo(self, item):
        self.__numero_cabo = 1
        self.__dados = {}
        for root in self.__root.iter(f'{self.__site}Placemark'):
            for cabo in root.iter(f'{self.__site}LineString'):
                if 'nome' in item:
                    self.__dados[self.__numero_cabo] = root.findtext(f'{self.__site}name').strip()
                elif 'linha' in item:
                    pontos = []
                    for i in cabo.findtext(f'{self.__site}coordinates').strip().split(' '):
                        pontos.append(i.split(','))
                    self.__dados[self.__numero_cabo] = pontos
                self.__numero_cabo += 1
        return self.__dados

    def ext_poste(self, item):
        self.__numero_poste = 1
        self.__dados = {}
        for root in self.__root.iter(f'{self.__site}Folder'):
            if 'POSTE' in root.findtext(f'{self.__site}name').upper():
                for poste in root.iter(f'{self.__site}Placemark'):
                    if 'POSTE' in item:
                        for coord in poste.iter(f'{self.__site}Point'):
                            self.__dados[self.__numero_poste] = coord.findtext(f'{self.__site}coordinates').split(',')
                            break
                        else:
                            self.__dados[self.__numero_poste] = None
                    else:
                        for data in poste.iter(f'{self.__site}Data'):
                            if item in data.attrib['name']:
                                self.__dados[self.__numero_poste] = data.findtext(f'{self.__site}value')
                                break
                            else:
                                self.__dados[self.__numero_poste] = None
                    self.__numero_poste += 1
        return self.__dados

    def ext_caixa_ftth(self, tipo):
        self.__numero_caixa = 1
        self.__dados = {}
        for root in self.__root.iter(f'{self.__site}Placemark'):
            for coord in root.iter(f'{self.__site}Point'):
                if 'coordenada' in tipo:
                    self.__dados[self.__numero_caixa] = coord.findtext(f'{self.__site}coordinates').split(',')
                    self.__numero_caixa += 1
                    break
                elif 'nome' in tipo:
                    self.__dados[self.__numero_caixa] = root.findtext(f'{self.__site}name')
                    self.__numero_caixa += 1
                    break
                elif 'style' in tipo:
                    self.__dados[self.__numero_caixa] = root.findtext(f'{self.__site}styleUrl').replace('#', '')
                    self.__numero_caixa += 1
                    break
        return self.__dados

    def distancia(self, x, y):  # ['-40.652', '-3.55307', '0']
        cat1 = ((float(x[0])) - (float(y[0]))) * 1852 * 60
        cat2 = ((float(x[1])) - (float(y[1]))) * 1852 * 60
        h = sqrt((cat1 * cat1) + (cat2 * cat2))

        return float(h)
