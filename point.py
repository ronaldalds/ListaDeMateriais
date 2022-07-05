class Point:
    def __init__(self, stored=None, name=None, style=None):
        self._stored = stored
        self._name = name
        self._type = ''
        self._style = style
        self._coordinates = []

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value):
        self._coordinates = value.split(',')

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, value):
        self._style = value
