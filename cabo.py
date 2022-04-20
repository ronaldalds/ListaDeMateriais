from projeto import Projeto
from math import sqrt
from poste import Poste
class Cabo(Projeto):
    def __init__(self,arquivo):
        super().__init__(arquivo)
        self.__percuso = super()._extracao_cabo('linha')
        self.__nome_cabo = {}
        self.__comprimento = {}
        self.__tipo_alca = {}
        self.__tipo_laco = {}
        self.__quantidade_alca = {}
        self.__quantidade_laco = {}
        self.__quantidade_de_fibra_no_cabo = {}
        self.__vao_suportado = {}
        self.__peso_do_cabo = {}
        self.__diametro_externo = {}
        self.__pressao_do_vento = {}


    @property
    def tratamento(self):

        postes = super()._extracao_coordenada()
        for x in self.__percuso:
            for c,y in enumerate(self.__percuso[x]):
                for i in postes:
                    if super().distancia(y,postes[i]) <= 2:
                        self.__percuso[x][c] = i
                        break

                    else:
                        if super().distancia(y, postes[i]) <= 10:
                            if self.__percuso[x][c] == type(int):
                                break
                            self.__percuso[x][c] = i

        return self.__percuso


    @property
    def nome(self):
        self.__nome_cabo = super()._extracao_cabo('nome')
        return self.__nome_cabo

    @property
    def percuso(self):

        return self.__percuso


test = Cabo('Rede FTTh.kml')


n = 259
# print(test.nome[n],test.tratamento[n],test.percuso[n])
# print(test.coordanada_poste)
print(test.tratamento)