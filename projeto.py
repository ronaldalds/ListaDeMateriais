import xml.etree.ElementTree as Et
from math import sqrt

class Projeto:
    def __init__(self, arquivo):
        doc = Et.parse(arquivo)
        self.__root = doc.getroot()
        self.__site = '{http://www.opengis.net/kml/2.2}'
        self.poste_coordenada = {}
        self.style = {}
        self.pop = {}
        self.__ext_coordenadas()
        self.__ext_style()
        self.__ext_pop()
        self.coordenada_poste_pop = {**self.poste_coordenada, **self.pop}

    def __ext_coordenadas(self):
        for root in self.__root.iter(f'{self.__site}Folder'):
            if 'POSTE' in root.findtext(f'{self.__site}name').upper():
                for n, poste in enumerate(root.iter(f'{self.__site}Placemark')):
                    for coord in poste.iter(f'{self.__site}Point'):
                        self.poste_coordenada[n + 1] = coord.findtext(f'{self.__site}coordinates').split(',')

    def __ext_style(self):
        for root in self.__root.iter(f'{self.__site}Style'):
            self.style[root.attrib['id']] = ''
            for icon_style in root.iter(f'{self.__site}IconStyle'):
                cor_icon = icon_style.findtext(f'{self.__site}color')
                for icon in icon_style.iter(f'{self.__site}Icon'):
                    tipo_icon = icon.findtext(f'{self.__site}href').replace('http://maps.google.com/mapfiles/kml/','')
                    if cor_icon == None:
                        for label in root.iter(f'{self.__site}LabelStyle'):
                            cor_icon = label.findtext(f'{self.__site}color')
                    self.style[root.attrib['id']] = f'{tipo_icon}{cor_icon}'

            if self.style[root.attrib['id']] == '':
                for poly in root.iter(f'{self.__site}PolyStyle'):
                    cor_poly = poly.findtext(f'{self.__site}color')
                    self.style[root.attrib['id']] = cor_poly

            if self.style[root.attrib['id']] == '':
                for line in root.iter(f'{self.__site}LineStyle'):
                    cor_line = line.findtext(f'{self.__site}color')
                    self.style[root.attrib['id']] = cor_line

        for root2 in self.__root.iter(f'{self.__site}StyleMap'):
            for pair in root2.iter(f'{self.__site}Pair'):
                if 'normal' in pair.findtext(f'{self.__site}key'):
                    trato_url = pair.findtext(f'{self.__site}styleUrl').replace('#', '')
                    self.style[root2.attrib['id']] = self.style[trato_url]

    def descricao_poste(self, item):
        dados = {}
        for root in self.__root.iter(f'{self.__site}Folder'):
            if 'POSTE' in root.findtext(f'{self.__site}name').upper():
                for n,poste in enumerate(root.iter(f'{self.__site}Placemark')):
                    for data in poste.iter(f'{self.__site}Data'):
                        if item in data.attrib['name']:
                            dados[n+1] = data.findtext(f'{self.__site}value')
                            break
                        else:
                            dados[n+1] = None
        return dados

    def __ext_pop(self):
        self.pop = {'POP': None}
        for root in self.__root.iter(f'{self.__site}Folder'):
            for pop in root.iter(f'{self.__site}Placemark'):
                if 'shapes/ranger_station.png' in self.style[pop.findtext(f'{self.__site}styleUrl').replace('#', '')]:
                    for c in pop.iter(f'{self.__site}Point'):
                        self.pop['POP'] = c.findtext(f'{self.__site}coordinates').split(',')
                        break
                    break
                break
        return self.pop

    def fibra_rede(self, item):
        n = 1
        dados = {}
        for root in self.__root.iter(f'{self.__site}Folder'):
            if 'REDE FTTH' == root.findtext(f'{self.__site}name').upper():
                for olt in root.iter(f'{self.__site}Folder'):
                    if 'OLT' in olt.findtext(f'{self.__site}name').upper():
                        for rota in olt.iter(f'{self.__site}Folder'):
                            if 'ROTA' in rota.findtext(f'{self.__site}name').upper():
                                for AP in rota.iter(f'{self.__site}Folder'):
                                    if 'AP' == AP.findtext(f'{self.__site}name').upper():
                                        for fibra in AP.iter(f'{self.__site}Placemark'):
                                            for linha in fibra.iter(f'{self.__site}LineString'):
                                                if 'nome' in item:
                                                    a = olt.findtext(f'{self.__site}name').strip()
                                                    b = rota.findtext(f'{self.__site}name').strip()
                                                    c = fibra.findtext(f'{self.__site}name').strip()
                                                    dados[n] = f'{a};{b};{c}'

                                                elif 'linha' in item:
                                                    pontos = []
                                                    for i in linha.findtext(f'{self.__site}coordinates').strip().split(' '):
                                                        pontos.append(i.split(','))
                                                        dados[n] = pontos
                                                n += 1

                                for AS in rota.iter(f'{self.__site}Folder'):
                                    if 'AS' == AS.findtext(f'{self.__site}name').upper():
                                        for fibra in AS.iter(f'{self.__site}Placemark'):
                                            for linha in fibra.iter(f'{self.__site}LineString'):
                                                if 'nome' in item:
                                                    a = olt.findtext(f'{self.__site}name').strip()
                                                    b = rota.findtext(f'{self.__site}name').strip()
                                                    c = fibra.findtext(f'{self.__site}name').strip()
                                                    dados[n] = f'{a};{b};{c}'

                                                elif 'linha' in item:
                                                    pontos = []
                                                    for i in linha.findtext(f'{self.__site}coordinates').strip().split(' '):
                                                        pontos.append(i.split(','))
                                                        dados[n] = pontos
                                                n += 1

                                for setor in rota.iter(f'{self.__site}Folder'):
                                    if 'SETOR' in setor.findtext(f'{self.__site}name').upper():
                                        for rede in rota.iter(f'{self.__site}Folder'):
                                            if 'REDE' in rede.findtext(f'{self.__site}name').upper():
                                                for fibra in rede.iter(f'{self.__site}Placemark'):
                                                    for linha in fibra.iter(f'{self.__site}LineString'):
                                                        if 'nome' in item:
                                                            a = olt.findtext(f'{self.__site}name').strip()
                                                            b = rota.findtext(f'{self.__site}name').strip()
                                                            c = setor.findtext(f'{self.__site}name').strip()
                                                            d = rede.findtext(f'{self.__site}name').strip()
                                                            e = fibra.findtext(f'{self.__site}name').strip()
                                                            dados[n] = f'{a};{b};{c};{d};{e}'

                                                        elif 'linha' in item:
                                                            pontos = []
                                                            for i in linha.findtext(f'{self.__site}coordinates').strip().split(
                                                                    ' '):
                                                                pontos.append(i.split(','))
                                                                dados[n] = pontos
                                                        n += 1
        return dados

    def elemento_rede(self, tipo):
        n = 1
        dados = {}
        for root in self.__root.iter(f'{self.__site}Folder'):
            if 'REDE FTTH' == root.findtext(f'{self.__site}name').upper():
                for elemento in root.iter(f'{self.__site}Placemark'):
                    for coord in elemento.iter(f'{self.__site}Point'):
                        if 'coordenada' in tipo:
                            dados[n] = coord.findtext(f'{self.__site}coordinates').split(',')
                            n += 1
                            break
                        elif 'nome' in tipo:
                            dados[n] = elemento.findtext(f'{self.__site}name')
                            n += 1
                            break
                        elif 'style' in tipo:
                            dados[n] = elemento.findtext(f'{self.__site}styleUrl').replace('#', '')
                            n += 1
                            break
        return dados

    def distancia(self, x, y):  # ['-40.652', '-3.55307', '0']
        cat1 = ((float(x[0])) - (float(y[0]))) * 1852 * 60
        cat2 = ((float(x[1])) - (float(y[1]))) * 1852 * 60
        h = sqrt((cat1 * cat1) + (cat2 * cat2))

        return float(h)
