from projeto import Projeto


class Poste(Projeto):
    def __init__(self, arquivo):
        super().__init__(arquivo)
        self.__coordenada_pop = {}
        self.__coordenada_poste = {}
        self.__coordenada_pop_poste = {}
        self.__tipo_poste = {}
        self.__altura_poste = {}
        self.__esforco_poste = {}
        self.__rede_eletrica = {}
        self.__quantidade_casa = {}
        self.__quantidade_comercio = {}
        self.__quantidade_apartamento = {}
        self.__tipo_equipamento = {}
        self.__codigo_poste = {}
        self.__ocupacao = {}
        self.__foto = {}

    @property
    def coordenada_pop_poste(self):
        self.__coordenada_pop_poste = {**self.coordenada_poste, **self.coordenada_pop}
        return self.__coordenada_pop_poste

    @property
    def coordenada_pop(self):
        self.__coordenada_pop = super().ext_pop
        return self.__coordenada_pop

    @property
    def coordenada_poste(self):
        self.__coordenada_poste = super().ext_poste("POSTE")
        return self.__coordenada_poste

    @property
    def tipo_poste(self):
        self.__tipo_poste = super().ext_poste("00")
        return self.__tipo_poste

    @property
    def altura_poste(self):
        self.__altura_poste = super().ext_poste("01")
        return self.__altura_poste

    @property
    def esforco_poste(self):
        self.__esforco_poste = super().ext_poste("02")
        return self.__esforco_poste

    @property
    def rede_eletrica(self):
        self.__rede_eletrica = super().ext_poste("03")
        return self.__rede_eletrica

    @property
    def quantidade_casa(self):
        self.__quantidade_casa = super().ext_poste("04")
        return self.__quantidade_casa

    @property
    def quantidade_comercio(self):
        self.__quantidade_comercio = super().ext_poste("05")
        return self.__quantidade_comercio

    @property
    def quantidade_apartamento(self):
        self.__quantidade_apartamento = super().ext_poste("06")
        return self.__quantidade_apartamento

    @property
    def tipo_equipamento(self):
        self.__tipo_equipamento = super().ext_poste("07")
        return self.__tipo_equipamento

    @property
    def codigo_poste(self):
        self.__codigo_poste = super().ext_poste("08")
        return self.__codigo_poste

    @property
    def ocupacao(self):
        self.__ocupacao = super().ext_poste("09")
        return self.__ocupacao

    @property
    def foto(self):
        self.__foto = self.ext_poste("pictures")  # verificar função de busca para busca fotos do mapeamento
        return self.__foto
