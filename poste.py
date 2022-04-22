from projeto import Projeto
class Poste(Projeto):
    def __init__(self, arquivo):
        super().__init__(arquivo)
        self.__coordenada_poste = {}
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
    def coordanada_poste(self):
        self.__coordenada_poste = self._ext_coordenada_poste
        return self.__coordenada_poste

    @property
    def tipo_poste(self):
        self.__tipo_poste = self._ext_poste("00")#chamada no arquivo do google earth no ExtendedData 00.tipo
        return self.__tipo_poste

    @property
    def altura_poste(self):
        self.__altura_poste = self._ext_poste("01")#chamada no arquivo do google earth no ExtendedData 01.altura
        return self.__altura_poste

    @property
    def esforco_poste(self):
        self.__esforco_poste = self._ext_poste("02")#chamada no arquivo do google earth no ExtendedData 02.esforco
        return self.__esforco_poste

    @property
    def rede_eletrica(self):
        self.__rede_eletrica = self._ext_poste("03")#chamada no arquivo do google earth no ExtendedData 03.rede
        return self.__rede_eletrica

    @property
    def quantidade_casa(self):
        self.__quantidade_casa = self._ext_poste("04")#chamada no arquivo do google earth no ExtendedData 04.casa
        return self.__quantidade_casa

    @property
    def quantidade_comercio(self):
        self.__quantidade_comercio = self._ext_poste("05")#chamada no arquivo do google earth no ExtendedData 05.comercio
        return self.__quantidade_comercio

    @property
    def quantidade_apartamento(self):
        self.__quantidade_apartamento = self._ext_poste("06")#chamada no arquivo do google earth no ExtendedData 06.predio
        return self.__quantidade_apartamento

    @property
    def tipo_equipamento(self):
        self.__tipo_equipamento = self._ext_poste("07")#chamada no arquivo do google earth no ExtendedData 07.equipamento
        return self.__tipo_equipamento

    @property
    def codigo_poste(self):
        self.__codigo_poste = self._ext_poste("08")#chamada no arquivo do google earth no ExtendedData 08.codigo
        return self.__codigo_poste

    @property
    def ocupacao(self):
        self.__ocupacao = self._ext_poste("09")#chamada no arquivo do google earth no ExtendedData 09.ocupante
        return self.__ocupacao

    @property
    def foto(self):
        self.__foto = self._ext_poste("10")# verificar função de busca para busca fotos do mapeamento
        return self.__foto