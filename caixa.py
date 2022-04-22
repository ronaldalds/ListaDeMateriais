from projeto import Projeto

class Caixa(Projeto):
    def __init__(self,arquivo):
        super().__init__(arquivo)
        self.__coordenada_caixa = super()._ext_caixa_ftth('coordenada')
        self.__nome_caixa = super()._ext_caixa_ftth('nome')

    # def tratamento(self,poste,disc):
    #     self.__dados = disc
    #     for x in disc:
    #         print(x)
    #         for i in poste:
    #             if self.distancia(disc[x],poste[i]) <= 2:
    #                 self.__dados[x] = i
    #                 break
    #             else:
    #                 if self.distancia(disc[x], poste[i]) <= 10:
    #                     if disc[x] == type(int):
    #                         break
    #                     self.__dados[x] = i
    #     return self.__dados

    @property
    def coordenada_caixa(self):
        return self.__coordenada_caixa

    @property
    def nome_caixa(self):
        return self.__nome_caixa