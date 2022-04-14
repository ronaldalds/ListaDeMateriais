import xml.etree.ElementTree as Et

class Poste:
    def __init__(self,arquivo):
        self.__arquivo = arquivo
        self.__tipo_poste = []
        self.__latitude = self.extracao_latitude(arquivo)
        self.__longitude = self.extracao_longitude(arquivo)
        self.__altura_poste = self.extracao_altura_poste(arquivo)
        self.__esforco_poste = self.extracao_esforco_poste(arquivo)
        self.__rede_eletrica = self.extracao_rede_eletrica(arquivo)
        self.__quantidade_casa = self.extracao_quantidade_casa(arquivo)
        self.__quantidade_comercio = self.extracao_quantidade_comercio(arquivo)
        self.__quantidade_apartamento = self.extracao_quantidade_apartamento(arquivo)
        self.__tipo_equipamento = self.extracao_tipo_equipamento(arquivo)
        self.__codigo_poste = self.extracao_codigo_poste(arquivo)
        self.__ocupacao = self.extracao_ocupacao(arquivo)


    # def __str__(self):
    #     cliente = self.__quantidade_de_casa + self.__quantidade_de_comercio + self.__quantidade_de_apartamento
    #     return f"{self.__tipo_de_poste} - {self.__altura_do_poste}/{self.__esforco_do_poste} - C{cliente}"
    def __getitem__(self, item):
    def extracao_dados(self):
        pass













    def extracao_tipo_poste(self):
        pass
    def extracao_latitude(self,arquivo):
        pass
    def extracao_longitude(self,arquivo):
        pass
    def extracao_altura_poste(self,arquivo):
        pass
    def extracao_esforco_poste(self,arquivo):
        pass
    def extracao_rede_eletrica(self,arquivo):
        pass
    def extracao_quantidade_casa(self,arquivo):
        pass
    def extracao_quantidade_comercio(self,arquivo):
        pass
    def extracao_quantidade_apartamento(self,arquivo):
        pass
    def extracao_tipo_equipamento(self,arquivo):
        pass
    def extracao_codigo_poste(self,arquivo):
        pass
    def extracao_ocupacao(self,arquivo):
        pass
