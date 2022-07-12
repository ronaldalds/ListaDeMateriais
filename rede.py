class Rede:
    def __init__(self, name):
        self._pon = name
        self._cto = []

    @property
    def name(self):
        return self._pon

    @property
    def cto(self):
        return self._cto

    @cto.setter
    def cto(self, value):
        self._cto.append(value)
