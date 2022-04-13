
class Poste:
    def __init__(self,tipo_de_poste,latitude,longitude,altura,esforco,tipo_de_rede_eletrica,casa=None,comercio=None,predio=None,equipamento=None,codigo=None,ocupante=None):
        self.__tipo_de_poste = tipo_de_poste
        self.__latitude = latitude
        self.__longitude = longitude
        self.__altura_do_poste = altura
        self.__esforco_do_poste = esforco
        self.__rede_eletrica = tipo_de_rede_eletrica
        self.__quantidade_de_casa = casa
        self.__quantidade_de_comercio = comercio
        self.__quantidade_de_apartamento = predio
        self.__tipo_equipamento = equipamento
        self.__codigo_do_poste = codigo
        self.__ocupacao = ocupante

    def __str__(self):
        return f"{self.__tipo_de_poste} - {self.__altura_do_poste}/{self.__esforco_do_poste} - {self.__quantidade_de_casa}"