from projeto import Projeto
from math import sqrt
class Cabo(Projeto):
    def __init__(self,arquivo):
        super().__init__(arquivo)
        self.__percuso = {}
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
    def distancia(self,x,y):#x=['-40.65200273', '-3.5530714', '0'] y=['-40.64269', '-3.55596', '0']
        cat1 = ((float(x[0])) - (float(y[0]))) * 1852 * 60
        cat2 = ((float(x[1])) - (float(y[1]))) * 1852 * 60

        h = sqrt((cat1 * cat1) + (cat2 * cat2))

        return float(h)

    @property
    def nome(self):
        self.__nome_cabo = self._extracao_cabo('nome')
        return self.__nome_cabo

    @property
    def percuso(self):
        self.__percuso = self._extracao_cabo('linha')
        return self.__percuso