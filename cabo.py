from projeto import Projeto
from math import sqrt
from poste import Poste
class Cabo(Projeto):
    def __init__(self,arquivo):
        super().__init__(arquivo)
        self.__percuso = super()._ext_cabo('linha')
        self.__nome_cabo = super()._ext_cabo('nome')
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

    def tratamento(self,poste,disc):
        self.__dados = disc
        for x in disc:
            for c,y in enumerate(disc[x]):
                for i in poste:
                    if self.distancia(y,poste[i]) <= 2:
                        self.__dados[x][c] = i
                        break
                    else:
                        if self.distancia(y, poste[i]) <= 10:
                            if disc[x][c] == type(int):
                                break
                            self.__dados[x][c] = i
        return self.__dados

    @property
    def nome(self):
        return self.__nome_cabo

    @property
    def percuso(self):

        return self.__percuso