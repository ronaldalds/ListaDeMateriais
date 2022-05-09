from projeto import Projeto


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

    def tratamento(self,poste):
        self.__dados = super().ext_cabo('linha')
        for x in self.__dados:
            for c,y in enumerate(self.__dados[x]):
                for i in poste:
                    if super().distancia(y,poste[i]) <= 2:
                        self.__dados[x][c] = i
                        break
                    else:
                        if super().distancia(y, poste[i]) <= 10:
                            if self.__dados[x][c] == type(int):
                                break
                            self.__dados[x][c] = i
        return self.__dados

    def comprimento(self,poste,margem=0.05):
        self.__dados = self.tratamento(poste)
        p1 = 0
        distancia = 0
        for i in self.__dados:
            for d in self.__dados[i]:
                if d == 'POP':
                    distancia += 80
                    p1 = poste[d]
                if p1 == 0:
                    p1 = poste[d]
                elif type(p1) == list and type(d) == int:
                    distancia += (super().distancia(p1, poste[d]))*(1+margem)
                    p1 = poste[d]
                elif type(p1) == list and type(d) == list:
                    distancia += (super().distancia(p1, d))*(1+margem)
                    p1 = d
            self.__comprimento[i] = round(distancia,2)
            distancia = 0
            p1 = 0

        return self.__comprimento

    @property
    def nome(self):
        self.__nome_cabo = super().ext_cabo('nome')
        return self.__nome_cabo

    @property
    def percuso(self):
        self.__percuso = super().ext_cabo('linha')
        return self.__percuso

