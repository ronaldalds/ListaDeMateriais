
class Poste:
    def __init__(self,latitude,longitude,altura,esforco,tipo_de_rede_eletrica,ocupante):
        print("contruindo objeto")
        self.latitude = latitude
        self.longitude = longitude
        self.altura_do_poste = altura
        self.esforco_do_poste = esforco
        self.rede_eletrica = tipo_de_rede_eletrica
        self.ocupacao = ocupante
        self.quantidade_de_casa = 0
        self.quantidade_de_comercio = 0
        self.quantidade_de_apartamento = 0
        self.cabo = 0
