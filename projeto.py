import xml.etree.ElementTree as Et

class Projeto:
    def __init__(self, arquivo):
        doc = Et.parse(arquivo)
        self.__root = doc.getroot()
        self.__folder = '{http://www.opengis.net/kml/2.2}Folder'
        self.__name = '{http://www.opengis.net/kml/2.2}name'
        self.__placemark = '{http://www.opengis.net/kml/2.2}Placemark'
        self.__data = '{http://www.opengis.net/kml/2.2}Data'
        self.__displayName = '{http://www.opengis.net/kml/2.2}displayName'
        self.__value = '{http://www.opengis.net/kml/2.2}value'
        self.__point = '{http://www.opengis.net/kml/2.2}Point'
        self.__coordinates = '{http://www.opengis.net/kml/2.2}coordinates'
        self.__lineString = '{http://www.opengis.net/kml/2.2}LineString'

    def _extracao_cabo(self, item):
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

    def _extracao_poste(self, item):
        self.__numero_poste = 1
        self.__dados = {}
        for root in self.__root.iter(self.__folder):
            if 'POSTE' in root.findtext(self.__name).upper():
                for poste in root.iter(self.__placemark):
                    for data in poste.iter(self.__data):
                        if item in str(data.findtext(self.__displayName)):
                            self.__dados[self.__numero_poste] = data.findtext(self.__value)
                            break
                        else:
                            self.__dados[self.__numero_poste] = ""
                    self.__numero_poste += 1
        return self.__dados

    def _extracao_coordenada(self):
        self.__numero_poste = 1
        self.__dados = {}
        for root in self.__root.iter(self.__folder):
            if 'POSTE' in root.findtext(self.__name).upper():
                for poste in root.iter(self.__placemark):
                    for coord in poste.iter(self.__point):
                        self.__dados[self.__numero_poste] = coord.findtext(self.__coordinates).split(',')
                    self.__numero_poste += 1
        return self.__dados