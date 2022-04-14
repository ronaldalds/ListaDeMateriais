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
        self.__pasta = '{http://www.opengis.net/kml/2.2}Folder'
        self.__name = '{http://www.opengis.net/kml/2.2}name'
        self.__placemark = '{http://www.opengis.net/kml/2.2}Placemark'
        self.__data = '{http://www.opengis.net/kml/2.2}Data'
        self.__displayName = '{http://www.opengis.net/kml/2.2}displayName'
        self.__value = '{http://www.opengis.net/kml/2.2}value'
        self.__point = '{http://www.opengis.net/kml/2.2}Point'
        self.__coordinates = '{http://www.opengis.net/kml/2.2}Coordinates'
        self.__numero_poste = 1


        for root in self.__root.iter(self.__pasta):
            if 'Poste' in root.findtext(self.__name):
                for poste in root.iter(self.__placemark):
                    for coord in root.iter(self.__point):
                        self.__coordenada_poste[self.__numero_poste] = coord.findtext(self.__coordinates)
                    for data in poste.iter(self.__data):
                        if "00" in str(data.findtext(self.__displayName)):
                            self.__tipo_poste[self.__numero_poste] = data.findtext(self.__value)
                            break
                        else:
                            self.__tipo_poste[self.__numero_poste] = ""

                        if "01" in str(data.findtext(self.__displayName)):
                            self.__altura_poste[self.__numero_poste] = data.findtext(self.__value)
                            break
                        else:
                            self.__altura_poste[self.__numero_poste] = ""

                        if "02" in str(data.findtext(self.__displayName)):
                            self.__esforco_poste[self.__numero_poste] = data.findtext(self.__value)
                            break
                        else:
                            self.__esforco_poste[self.__numero_poste] = ""

                        if "03" in str(data.findtext(self.__displayName)):
                            self.__rede_eletrica[self.__numero_poste] = data.findtext(self.__value)
                            break
                        else:
                            self.__rede_eletrica[self.__numero_poste] = ""

                        if "04" in str(data.findtext(self.__displayName)):
                            self.__quantidade_casa[self.__numero_poste] = data.findtext(self.__value)
                            break
                        else:
                            self.__quantidade_casa[self.__numero_poste] = ""

                        if "05" in str(data.findtext(self.__displayName)):
                            self.__quantidade_comercio[self.__numero_poste] = data.findtext(self.__value)
                            break
                        else:
                            self.__quantidade_comercio[self.__numero_poste] = ""

                        if "06" in str(data.findtext(self.__displayName)):
                            self.__quantidade_apartamento[self.__numero_poste] = data.findtext(self.__value)
                            break
                        else:
                            self.__quantidade_apartamento[self.__numero_poste] = ""

                        if "07" in str(data.findtext(self.__displayName)):
                            self.__tipo_equipamento[self.__numero_poste] = data.findtext(self.__value)
                            break
                        else:
                            self.__tipo_equipamento[self.__numero_poste] = ""

                        if "08" in str(data.findtext(self.__displayName)):
                            self.__codigo_poste[self.__numero_poste] = data.findtext(self.__value)
                            break
                        else:
                            self.__codigo_poste[self.__numero_poste] = ""

                        if "09" in str(data.findtext(self.__displayName)):
                            self.__ocupacao[self.__numero_poste] = data.findtext(self.__value)
                            break
                        else:
                            self.__ocupacao[self.__numero_poste] = ""
                    self.__numero_poste += 1


arquivo = Poste('Coreaú.kml')
print(arquivo._Poste__tipo_poste)
