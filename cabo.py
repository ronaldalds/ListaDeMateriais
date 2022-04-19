import xml.etree.ElementTree as Et

class Cabo:
    def __init__(self,arquivo):
        doc = Et.parse(arquivo)
        self.__root = doc.getroot()
        self.__percuso = {}
        self.__nome_cabo = {}
        self.__comprimento = {}
        self.__tipo_alca = {}
        self.__tipo_laco = {}
        self.__quantidade_alca = {}
        self.__quantidade_laco = {}
        self.__quantidade_de_fibra_no_cabo = {}
        self.__vao_suportado = {}
        self.__peso_do_cabo = {}
        self.diametro_externo = {}
        self.pressao_do_vento = {}
        self.__folder = '{http://www.opengis.net/kml/2.2}Folder'
        self.__name = '{http://www.opengis.net/kml/2.2}name'
        self.__placemark = '{http://www.opengis.net/kml/2.2}Placemark'
        self.__data = '{http://www.opengis.net/kml/2.2}Data'
        self.__displayName = '{http://www.opengis.net/kml/2.2}displayName'
        self.__value = '{http://www.opengis.net/kml/2.2}value'
        self.__point = '{http://www.opengis.net/kml/2.2}Point'
        self.__coordinates = '{http://www.opengis.net/kml/2.2}coordinates'
        self.__lineString = '{http://www.opengis.net/kml/2.2}LineString'


    def __extracao(self,item):
        self.__numero_cabo = 1
        self.__dados = {}
        for root in self.__root.iter(self.__placemark):
            for cabo in root.iter(self.__lineString):
                if 'nome' in item:
                    self.__dados[self.__numero_cabo] = root.findtext(self.__name).strip()
                elif 'linha' in item:
                    self.__dados[self.__numero_cabo] = cabo.findtext(self.__coordinates).strip()
                self.__numero_cabo += 1
        return self.__dados

    @property
    def nome(self):
        self.__nome_cabo = self.__extracao('nome')
        return self.__nome_cabo

    @property
    def percuso(self):
        self.__percuso = self.__extracao('linha')
        return self.__percuso

arquivo = Cabo('Coreaú.kml')

teste = arquivo.percuso

# print(len(teste))
print(teste)