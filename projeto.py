import xml.etree.ElementTree as Et
from math import sqrt

c = 0
e = 0


class Projeto:
    def __init__(self, arquivo):
        doc = Et.parse(arquivo)
        self._root = doc.getroot()
        self._site = '{http://www.opengis.net/kml/2.2}'

        self._nome_elemento = {}
        self._tipo_elemento = {}
        self._coordenada_elemento = {}

        self._nome_fibra = {}
        self._tipo_fibra = {}
        self._coordenada_fibra = {}
        self._ra = {}
        self._alimentador = {}
        self._cdlh = {}

        self.style = {}
        self.pop = {}
        self._ext_style()
        self.lista_rede()
        self.fibra_ra()
        self.alimentador()
        self.cordoalha()

    def cordoalha(self):
        for i in self._nome_fibra:
            if 'CORDOALHA' in self._nome_fibra[i][2].upper():
                self._cdlh[i] = self._nome_fibra[i]

    def alimentador(self):
        for i in self._nome_fibra:
            if 'AP' == self._nome_fibra[i][2].upper():
                self._alimentador[i] = self._nome_fibra[i]
            if 'AS' == self._nome_fibra[i][2].upper():
                self._alimentador[i] = self._nome_fibra[i]

    def fibra_ra(self):
        for i in self._nome_fibra:
            if 'REDE' in self._nome_fibra[i][3].upper():
                self._ra[i] = self._nome_fibra[i]

    def lista_rede(self):
        for ro in self._root.iter(f'{self._site}Folder'):
            if 'REDE FTTH' == ro[0].text.upper():
                self.ext_cabo(ro)
                self.ext_elemento(ro)

    def ext_cabo(self, item, nome=None, tipo=None, coord=None):
        global c
        if nome is None:
            nome = []
            tipo = []
            coord = []
        for i in item:
            if 'Document' in i.tag:
                self.ext_cabo(i, nome, tipo, coord)
            elif 'Folder' in i.tag:
                nome.append(f'{i[0].text}')
                self.ext_cabo(i, nome, tipo, coord)
                nome.pop()
            elif 'Placemark' in i.tag:
                for t in i.iter(f'{self._site}LineString'):
                    c += 1
                    nome.append(f'{i[0].text}')
                    self._nome_fibra[c] = list(nome)
                    nome.pop()
                    self._tipo_fibra[c] = i.findtext(f'{self._site}styleUrl').replace('#', '')
                    pontos = []
                    for linha in t.findtext(f'{self._site}coordinates').strip().split(' '):
                        pontos.append(linha.split(','))
                        self._coordenada_fibra[c] = pontos

    def ext_elemento(self, item, nome=None, tipo=None, coord=None):
        global e
        if nome is None:
            nome = []
            tipo = []
            coord = []
        for i in item:
            if 'Document' in i.tag:
                self.ext_elemento(i, nome, tipo, coord)
            elif 'Folder' in i.tag:
                nome.append(f'{i[0].text}')
                self.ext_elemento(i, nome, tipo, coord)
                nome.pop()
            elif 'Placemark' in i.tag:
                for t in i.iter(f'{self._site}Point'):
                    e += 1
                    nome.append(f'{i[0].text}')
                    self._nome_elemento[e] = list(nome)
                    nome.pop()
                    self._tipo_elemento[e] = i.findtext(f'{self._site}styleUrl').replace('#', '')
                    self._coordenada_elemento[e] = t.findtext(f'{self._site}coordinates').split(',')

    def _ext_style(self):
        for root in self._root[0]:
            if 'Style' in root.tag:
                # print(root.tag)
                self.style[root.attrib['id']] = ''
                for icon_style in root.iter(f'{self._site}IconStyle'):
                    cor_icon = icon_style.findtext(f'{self._site}color')
                    for icon in icon_style.iter(f'{self._site}Icon'):
                        tipo_icon = icon.findtext(f'{self._site}href').replace('http://maps.google.com/mapfiles/kml/',
                                                                               '')
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

    def distancia(self, x, y):
        cat1 = ((float(x[0])) - (float(y[0]))) * 1852 * 60
        cat2 = ((float(x[1])) - (float(y[1]))) * 1852 * 60
        h = sqrt((cat1 * cat1) + (cat2 * cat2))
        return float(h)
