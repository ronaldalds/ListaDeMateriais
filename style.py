from projeto import Projeto

class Style(Projeto):
    def __init__(self,arquivo):
        super().__init__(arquivo)
        self.__style_item = super().ext_style

    @property
    def tipo_style(self):
        return self.__style_item