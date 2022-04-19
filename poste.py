import xml.etree.ElementTree as Et

class Poste:
    def __init__(self, arquivo):
        doc = Et.parse(arquivo)
        self.__root = doc.getroot()
        self.__coordenada_poste = {}
        self.__tipo_poste = {}
        self.__altura_poste = {}
        self.__esforco_poste = {}
        self.__rede_eletrica = {}
        self.__quantidade_casa = {}
        self.__quantidade_comercio = {}
        self.__quantidade_apartamento = {}
        self.__tipo_equipamento = {}
        self.__codigo_poste = {}
        self.__ocupacao = {}
        self.__foto = {}
        self.__folder = '{http://www.opengis.net/kml/2.2}Folder'
        self.__name = '{http://www.opengis.net/kml/2.2}name'
        self.__placemark = '{http://www.opengis.net/kml/2.2}Placemark'
        self.__data = '{http://www.opengis.net/kml/2.2}Data'
        self.__displayName = '{http://www.opengis.net/kml/2.2}displayName'
        self.__value = '{http://www.opengis.net/kml/2.2}value'
        self.__point = '{http://www.opengis.net/kml/2.2}Point'
        self.__coordinates = '{http://www.opengis.net/kml/2.2}coordinates'


    def __extracao(self, item):
        self.__numero_poste = 1
        self.__dados = {}
        for root in self.__root.iter(self.__folder):
            if 'Poste' in root.findtext(self.__name):
                for poste in root.iter(self.__placemark):
                    for data in poste.iter(self.__data):
                        if item in str(data.findtext(self.__displayName)):
                            self.__dados[self.__numero_poste] = data.findtext(self.__value)
                            break
                        else:
                            self.__dados[self.__numero_poste] = ""
                    self.__numero_poste += 1
        return self.__dados
    @property
    def coordenada(self):
        self.__numero_poste = 1
        self.__dados = {}
        for root in self.__root.iter(self.__folder):
            if 'Poste' in root.findtext(self.__name):
                for poste in root.iter(self.__placemark):
                    for coord in poste.iter(self.__point):
                        self.__dados[self.__numero_poste] = coord.findtext(self.__coordinates).split(',')
                    self.__numero_poste += 1
        return self.__dados

    @property
    def tipo_poste(self):
        self.__tipo_poste = self.__extracao("00")#chamada no arquivo do google earth no ExtendedData 00.tipo
        return self.__tipo_poste

    @property
    def altura_poste(self):
        self.__altura_poste = self.__extracao("01")#chamada no arquivo do google earth no ExtendedData 01.altura
        return self.__altura_poste

    @property
    def esforco_poste(self):
        self.__esforco_poste = self.__extracao("02")#chamada no arquivo do google earth no ExtendedData 02.esforco
        return self.__esforco_poste

    @property
    def rede_eletrica(self):
        self.__rede_eletrica = self.__extracao("03")#chamada no arquivo do google earth no ExtendedData 03.rede
        return self.__rede_eletrica

    @property
    def quantidade_casa(self):
        self.__quantidade_casa = self.__extracao("04")#chamada no arquivo do google earth no ExtendedData 04.casa
        return self.__quantidade_casa

    @property
    def quantidade_comercio(self):
        self.__quantidade_comercio = self.__extracao("05")#chamada no arquivo do google earth no ExtendedData 05.comercio
        return self.__quantidade_comercio

    @property
    def quantidade_apartamento(self):
        self.__quantidade_apartamento = self.__extracao("06")#chamada no arquivo do google earth no ExtendedData 06.predio
        return self.__quantidade_apartamento

    @property
    def tipo_equipamento(self):
        self.__tipo_equipamento = self.__extracao("07")#chamada no arquivo do google earth no ExtendedData 07.equipamento
        return self.__tipo_equipamento

    @property
    def codigo_poste(self):
        self.__codigo_poste = self.__extracao("08")#chamada no arquivo do google earth no ExtendedData 08.codigo
        return self.__codigo_poste

    @property
    def ocupacao(self):
        self.__ocupacao = self.__extracao("09")#chamada no arquivo do google earth no ExtendedData 09.ocupante
        return self.__ocupacao

    @property
    def foto(self):
        self.__foto = self.__extracao("10")# verificar função de busca para busca fotos do mapeamento
        return self.__foto