from projeto import Projeto


class Poste(Projeto):
    def __init__(self, arquivo):
        super().__init__(arquivo)
        self._coordenada_poste = {}
        self._tipo_poste = {}
        self._altura_poste = {}
        self._esforco_poste = {}
        self._rede_eletrica = {}
        self._quantidade_casa = {}
        self._quantidade_comercio = {}
        self._quantidade_apartamento = {}
        self._tipo_equipamento = {}
        self._codigo_poste = {}
        self._ocupacao = {}
        self._foto = {}
        self.descricao_poste()

    def descricao_poste(self):
        for root in self._root.iter(f'{self._site}Folder'):
            if 'POSTE' in root.findtext(f'{self._site}name').upper():
                for n, poste in enumerate(root.iter(f'{self._site}Placemark')):
                    for coord in poste.iter(f'{self._site}Point'):
                        self._coordenada_poste[n + 1] = coord.findtext(f'{self._site}coordinates').split(',')
                    for data in poste.iter(f'{self._site}Data'):
                        if '00' in data.attrib['name']:
                            self._tipo_poste[n + 1] = data.findtext(f'{self._site}value')
                        elif '01' in data.attrib['name']:
                            self._altura_poste[n + 1] = data.findtext(f'{self._site}value')
                        elif '02' in data.attrib['name']:
                            self._esforco_poste[n + 1] = data.findtext(f'{self._site}value')
                        elif '03' in data.attrib['name']:
                            self._rede_eletrica[n + 1] = data.findtext(f'{self._site}value')
                        elif '04' in data.attrib['name']:
                            self._quantidade_casa[n + 1] = data.findtext(f'{self._site}value')
                        elif '05' in data.attrib['name']:
                            self._quantidade_comercio[n + 1] = data.findtext(f'{self._site}value')
                        elif '06' in data.attrib['name']:
                            self._quantidade_apartamento[n + 1] = data.findtext(f'{self._site}value')
                        elif '07' in data.attrib['name']:
                            self._tipo_equipamento[n + 1] = data.findtext(f'{self._site}value')
                        elif '08' in data.attrib['name']:
                            self._codigo_poste[n + 1] = data.findtext(f'{self._site}value')
                        elif '09' in data.attrib['name']:
                            self._ocupacao[n + 1] = data.findtext(f'{self._site}value')
                        elif 'pictures' in data.attrib['name']:
                            self._foto[n + 1] = data.findtext(f'{self._site}value')

    @property
    def coordenada_poste(self):
        return self._coordenada_poste

    @property
    def tipo_poste(self):
        return self._tipo_poste

    @property
    def altura_poste(self):
        return self._altura_poste

    @property
    def esforco_poste(self):
        return self._esforco_poste

    @property
    def rede_eletrica(self):
        return self._rede_eletrica

    @property
    def quantidade_casa(self):
        return self._quantidade_casa

    @property
    def quantidade_comercio(self):
        return self._quantidade_comercio

    @property
    def quantidade_apartamento(self):
        return self._quantidade_apartamento

    @property
    def tipo_equipamento(self):
        return self._tipo_equipamento

    @property
    def codigo_poste(self):
        return self._codigo_poste

    @property
    def ocupacao(self):
        return self._ocupacao

    @property
    def foto(self):
        return self._foto
