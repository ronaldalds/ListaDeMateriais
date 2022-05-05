from projeto import Projeto
class Poste(Projeto):
    def __init__(self, arquivo):
        super().__init__(arquivo)
        self.__coordenada_pop = super()._ext_pop
        self.__coordenada_poste = super()._ext_poste("POSTE")
        self.__coordenada_pop_poste = {**self.__coordenada_poste,**self.__coordenada_pop}
        self.__tipo_poste = super()._ext_poste("00")
        self.__altura_poste = super()._ext_poste("01")
        self.__esforco_poste = super()._ext_poste("02")
        self.__rede_eletrica = super()._ext_poste("03")
        self.__quantidade_casa = super()._ext_poste("04")
        self.__quantidade_comercio = super()._ext_poste("05")
        self.__quantidade_apartamento = super()._ext_poste("06")
        self.__tipo_equipamento = super()._ext_poste("07")
        self.__codigo_poste = super()._ext_poste("08")
        self.__ocupacao = super()._ext_poste("09")
        self.__foto = {}

    @property
    def coordenada_pop_poste(self):
        return self.__coordenada_pop_poste

    @property
    def coordanada_pop(self):
        return self.__coordenada_pop

    @property
    def coordanada_poste(self):
        return self.__coordenada_poste

    @property
    def tipo_poste(self):
        return self.__tipo_poste

    @property
    def altura_poste(self):
        return self.__altura_poste

    @property
    def esforco_poste(self):
        return self.__esforco_poste

    @property
    def rede_eletrica(self):
        return self.__rede_eletrica

    @property
    def quantidade_casa(self):
        return self.__quantidade_casa

    @property
    def quantidade_comercio(self):
        return self.__quantidade_comercio

    @property
    def quantidade_apartamento(self):
        return self.__quantidade_apartamento

    @property
    def tipo_equipamento(self):
        return self.__tipo_equipamento

    @property
    def codigo_poste(self):
        return self.__codigo_poste

    @property
    def ocupacao(self):
        return self.__ocupacao

    @property
    def foto(self):
        self.__foto = self._ext_poste("10")# verificar função de busca para busca fotos do mapeamento
        return self.__foto