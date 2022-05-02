import xml.etree.ElementTree as Et
from math import sqrt

class Projeto:
    def __init__(self, arquivo):
        doc = Et.parse(arquivo)
        self.__root = doc.getroot()
        self.__document = '{http://www.opengis.net/kml/2.2}Document'
        self.__folder = '{http://www.opengis.net/kml/2.2}Folder'
        self.__name = '{http://www.opengis.net/kml/2.2}name'
        self.__placemark = '{http://www.opengis.net/kml/2.2}Placemark'
        self.__data = '{http://www.opengis.net/kml/2.2}Data'
        self.__displayName = '{http://www.opengis.net/kml/2.2}displayName'
        self.__value = '{http://www.opengis.net/kml/2.2}value'
        self.__point = '{http://www.opengis.net/kml/2.2}Point'
        self.__coordinates = '{http://www.opengis.net/kml/2.2}coordinates'
        self.__lineString = '{http://www.opengis.net/kml/2.2}LineString'
        self.__styleUrl = '{http://www.opengis.net/kml/2.2}styleUrl'
        self.__style = '{http://www.opengis.net/kml/2.2}Style'
        self.__styleMap = '{http://www.opengis.net/kml/2.2}StyleMap'
        self.__href = '{http://www.opengis.net/kml/2.2}href'
        self.__icon = '{http://www.opengis.net/kml/2.2}Icon'
        self.__pair = '{http://www.opengis.net/kml/2.2}Pair'
        self.__key = '{http://www.opengis.net/kml/2.2}key'

    @property
    def _ext_style(self):
        self.__dados = {}
        for root in self.__root.iter(self.__style):
            for icon in root.iter(self.__icon):
                trato_tipo = icon.findtext(self.__href).replace('http://maps.google.com/mapfiles/kml/', '')
                self.__dados[root.attrib['id']] = trato_tipo
        for root2 in self.__root.iter(self.__styleMap):
            for pair in root2.iter(self.__pair):
                if 'normal' in pair.findtext(self.__key):
                    trato_url = pair.findtext(self.__styleUrl).replace('#', '')
                    self.__dados[root2.attrib['id']] = self.__dados[trato_url]
        return self.__dados

    def _ext_cabo(self, item):
        self.__numero_cabo = 1
        self.__dados = {}
        for root in self.__root.iter(self.__placemark):
            for cabo in root.iter(self.__lineString):
                if 'nome' in item:
                    self.__dados[self.__numero_cabo] = root.findtext(self.__name).strip()
                elif 'linha' in item:
                    pontos = []
                    for i in cabo.findtext(self.__coordinates).strip().split(' '):
                        pontos.append(i.split(','))
                    self.__dados[self.__numero_cabo] = pontos
                self.__numero_cabo += 1
        return self.__dados

    def _ext_poste(self, item):
        self.__numero_poste = 1
        self.__dados = {}
        for root in self.__root.iter(self.__folder):
            for poste in root.iter(self.__placemark):
                for data in poste.iter(self.__data):
                    if item in str(data.findtext(self.__displayName)):
                        self.__dados[self.__numero_poste] = data.findtext(self.__value)
                        break
                    else:
                        self.__dados[self.__numero_poste] = ""
                self.__numero_poste += 1
        return self.__dados

    def _ext_caixa_ftth(self,tipo):
        self.__numero_caixa = 1
        self.__dados = {}
        for root in self.__root.iter(self.__placemark):
            for coord in root.iter(self.__point):
                if 'coordenada' in tipo:
                    self.__dados[self.__numero_caixa] = coord.findtext(self.__coordinates).split(',')
                    break
                elif 'nome' in tipo:
                    self.__dados[self.__numero_caixa] = root.findtext(self.__name)
                    break
                elif 'style' in tipo:
                    self.__dados[self.__numero_caixa] = root.findtext(self.__styleUrl).replace('#','')
                    break
            self.__numero_caixa += 1
        return self.__dados

    @property
    def _ext_coordenada_poste(self):
        self.__numero_poste = 1
        self.__dados = {}
        for root in self.__root.iter(self.__folder):
            if 'POSTE' in root.findtext(self.__name).upper():
                for poste in root.iter(self.__placemark):
                    for coord in poste.iter(self.__point):
                        self.__dados[self.__numero_poste] = coord.findtext(self.__coordinates).split(',')
                    self.__numero_poste += 1
        return self.__dados

    def distancia(self,x,y):#['-40.652', '-3.55307', '0']
        cat1 = ((float(x[0])) - (float(y[0]))) * 1852 * 60
        cat2 = ((float(x[1])) - (float(y[1]))) * 1852 * 60
        h = sqrt((cat1 * cat1) + (cat2 * cat2))

        return float(h)
