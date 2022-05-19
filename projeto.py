import xml.etree.ElementTree as Et
from math import sqrt

class Projeto:
    def __init__(self, arquivo):
        doc = Et.parse(arquivo)
        self._root = doc.getroot()
        self._site = '{http://www.opengis.net/kml/2.2}'

        self._nome_elemento = {}
        self._tipo_elemento = {}
        self._coordenada_elemento = {}

        self._nome_fibra = {}
        self._coordenada_fibra = {}

        self.__ext_rede()
        self.style = {}
        self.pop = {}
        self.__ext_style()

    def __ext_style(self):
        for root in self._root.iter(f'{self._site}Style'):
            self.style[root.attrib['id']] = ''
            for icon_style in root.iter(f'{self._site}IconStyle'):
                cor_icon = icon_style.findtext(f'{self._site}color')
                for icon in icon_style.iter(f'{self._site}Icon'):
                    tipo_icon = icon.findtext(f'{self._site}href').replace('http://maps.google.com/mapfiles/kml/', '')
                    if cor_icon == None:
                        for label in root.iter(f'{self._site}LabelStyle'):
                            cor_icon = label.findtext(f'{self._site}color')
                    self.style[root.attrib['id']] = f'{tipo_icon}{cor_icon}'

            if self.style[root.attrib['id']] == '':
                for poly in root.iter(f'{self._site}PolyStyle'):
                    cor_poly = poly.findtext(f'{self._site}color')
                    self.style[root.attrib['id']] = cor_poly

            if self.style[root.attrib['id']] == '':
                for line in root.iter(f'{self._site}LineStyle'):
                    cor_line = line.findtext(f'{self._site}color')
                    self.style[root.attrib['id']] = cor_line

        for root2 in self._root.iter(f'{self._site}StyleMap'):
            for pair in root2.iter(f'{self._site}Pair'):
                if 'normal' in pair.findtext(f'{self._site}key'):
                    trato_url = pair.findtext(f'{self._site}styleUrl').replace('#', '')
                    self.style[root2.attrib['id']] = self.style[trato_url]

    def __ext_rede(self):
        nf = 1
        ne = 1
        for root in self._root.iter(f'{self._site}Folder'):
            if 'REDE FTTH' == root.findtext(f'{self._site}name').upper():
                for olt in root.iter(f'{self._site}Folder'):
                    if 'OLT' in olt.findtext(f'{self._site}name').upper():
                        for rota in olt.iter(f'{self._site}Folder'):
                            if 'ROTA' in rota.findtext(f'{self._site}name').upper():
                                for AP in rota.iter(f'{self._site}Folder'):
                                    if 'AP' == AP.findtext(f'{self._site}name').upper():
                                        for fibra in AP.iter(f'{self._site}Placemark'):
                                            for elemento in fibra.iter(f'{self._site}Point'):
                                                a = olt.findtext(f'{self._site}name').strip()
                                                b = rota.findtext(f'{self._site}name').strip()
                                                c = ''
                                                d = ''
                                                e = fibra.findtext(f'{self._site}name').strip()
                                                self._tipo_elemento[ne] = fibra.findtext(f'{self._site}styleUrl').replace('#', '')
                                                self._nome_elemento[ne] = f'{a};{b};{c};{d};{e}'
                                                self._coordenada_elemento[ne] = elemento.findtext(f'{self._site}coordinates').split(',')
                                                ne += 1
                                            for linha in fibra.iter(f'{self._site}LineString'):
                                                a = olt.findtext(f'{self._site}name').strip()
                                                b = rota.findtext(f'{self._site}name').strip()
                                                c = ''
                                                d = ''
                                                e = fibra.findtext(f'{self._site}name').strip()
                                                self._nome_fibra[nf] = f'{a};{b};{c};{d};{e}'
                                                pontos = []
                                                for i in linha.findtext(f'{self._site}coordinates').strip().split(' '):
                                                    pontos.append(i.split(','))
                                                    self._coordenada_fibra[nf] = pontos
                                                nf += 1

                                for AS in rota.iter(f'{self._site}Folder'):
                                    if 'AS' == AS.findtext(f'{self._site}name').upper():
                                        for fibra in AS.iter(f'{self._site}Placemark'):
                                            for elemento in fibra.iter(f'{self._site}Point'):
                                                a = olt.findtext(f'{self._site}name').strip()
                                                b = rota.findtext(f'{self._site}name').strip()
                                                c = ''
                                                d = ''
                                                e = fibra.findtext(f'{self._site}name').strip()
                                                self._tipo_elemento[ne] = fibra.findtext(f'{self._site}styleUrl').replace('#', '')
                                                self._nome_elemento[ne] = f'{a};{b};{c};{d};{e}'
                                                self._coordenada_elemento[ne] = elemento.findtext(f'{self._site}coordinates').split(',')
                                                ne += 1
                                            for linha in fibra.iter(f'{self._site}LineString'):
                                                a = olt.findtext(f'{self._site}name').strip()
                                                b = rota.findtext(f'{self._site}name').strip()
                                                c = ''
                                                d = ''
                                                e = fibra.findtext(f'{self._site}name').strip()
                                                self._nome_fibra[nf] = f'{a};{b};{c};{d};{e}'
                                                pontos = []
                                                for i in linha.findtext(f'{self._site}coordinates').strip().split(' '):
                                                    pontos.append(i.split(','))
                                                    self._coordenada_fibra[nf] = pontos
                                                nf += 1

                                for setor in rota.iter(f'{self._site}Folder'):
                                    if 'SETOR' in setor.findtext(f'{self._site}name').upper():
                                        for hub in setor.iter(f'{self._site}Placemark'):
                                            for elemento in hub.iter(f'{self._site}Point'):
                                                a = olt.findtext(f'{self._site}name').strip()
                                                b = rota.findtext(f'{self._site}name').strip()
                                                c = setor.findtext(f'{self._site}name').strip()
                                                d = ''
                                                e = hub.findtext(f'{self._site}name').strip()
                                                self._tipo_elemento[ne] = hub.findtext(
                                                    f'{self._site}styleUrl').replace('#', '')
                                                self._nome_elemento[ne] = f'{a};{b};{c};{d};{e}'
                                                self._coordenada_elemento[ne] = elemento.findtext(
                                                    f'{self._site}coordinates').split(',')
                                                ne += 1
                                        for rede in setor.iter(f'{self._site}Folder'):
                                            if 'REDE' in rede.findtext(f'{self._site}name').upper():
                                                for fibra in rede.iter(f'{self._site}Placemark'):
                                                    for elemento in fibra.iter(f'{self._site}Point'):
                                                        a = olt.findtext(f'{self._site}name').strip()
                                                        b = rota.findtext(f'{self._site}name').strip()
                                                        c = setor.findtext(f'{self._site}name').strip()
                                                        d = rede.findtext(f'{self._site}name').strip()
                                                        e = fibra.findtext(f'{self._site}name').strip()
                                                        self._tipo_elemento[ne] = fibra.findtext(f'{self._site}styleUrl').replace('#', '')
                                                        self._nome_elemento[ne] = f'{a};{b};{c};{d};{e}'
                                                        self._coordenada_elemento[ne] = elemento.findtext(f'{self._site}coordinates').split(',')
                                                        ne += 1
                                                    for linha in fibra.iter(f'{self._site}LineString'):
                                                        a = olt.findtext(f'{self._site}name').strip()
                                                        b = rota.findtext(f'{self._site}name').strip()
                                                        c = setor.findtext(f'{self._site}name').strip()
                                                        d = rede.findtext(f'{self._site}name').strip()
                                                        e = fibra.findtext(f'{self._site}name').strip()
                                                        self._nome_fibra[nf] = f'{a};{b};{c};{d};{e}'
                                                        pontos = []
                                                        for i in linha.findtext(f'{self._site}coordinates').strip().split(' '):
                                                            pontos.append(i.split(','))
                                                            self._coordenada_fibra[nf] = pontos
                                                        nf += 1

    def distancia(self, x, y):
        cat1 = ((float(x[0])) - (float(y[0]))) * 1852 * 60
        cat2 = ((float(x[1])) - (float(y[1]))) * 1852 * 60
        h = sqrt((cat1 * cat1) + (cat2 * cat2))

        return float(h)
