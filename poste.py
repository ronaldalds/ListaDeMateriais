
class Poste:
    def __init__(self,tipo_de_poste,latitude,longitude,altura,esforco,tipo_de_rede_eletrica):
        self.__tipo_de_poste = tipo_de_poste
        self.__latitude = latitude
        self.__longitude = longitude
        self.__altura_do_poste = altura
        self.__esforco_do_poste = esforco
        self.__rede_eletrica = tipo_de_rede_eletrica
        self.__ocupacao = []
        self.__quantidade_de_casa = 0
        self.__quantidade_de_comercio = 0
        self.__quantidade_de_apartamento = 0
        self.__cabo = []
        self.__bap = 0
        self.__sco = 0
        self.__olhal = 0
        self.__braco_extensao = 0
        self.__reserva_tecnica = 0
        self.__dieletrico = 0
