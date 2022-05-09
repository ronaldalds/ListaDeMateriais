from elemento import Elemento
class Reserva(Elemento):
    def __init__(self,arquivo):
        super().__init__(arquivo)
        self.__reserva = {}
        self.__nome_cabo = {}
        self.__comprimento = {}
        self.__quantidade_de_fibra_no_cabo = {}
        self.__vao_suportado = {}


    def coordenada_reserva(self):

        for i in super().tipo_elemento:
            if super().tipo_elemento[i] == 'Reserva':
                self.__reserva[i] = super().coordenada_elemento[i]
        return self.__reserva