
class Poste:
    def __init__(self,tipo_de_poste,latitude,longitude,altura,esforco,tipo_de_rede_eletrica,casa,comercio,predio,equipamento,codigo,ocupante):
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