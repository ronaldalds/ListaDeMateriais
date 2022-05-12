from projeto import Projeto

class Style(Projeto):
    def __init__(self,arquivo):
        super().__init__(arquivo)
        self.__style_item = {}

    @property
    def tipo_style(self):
        self.__style_item = super().style
        return self.__style_item