from helpers import meter


class Point:
    def __init__(self, stored=None, name=None, style=None):
        self._stored = stored
        self._name = name
        self._type = ''
        self._style = style
        self._coordinates = []
        self._pole = ''

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

    @property
    def name(self):
        return self._name

    def type(self, value):
        if self._type == '':
            for i in value:
                if self._style == i.identifier:
                    self._type = i.type
                    return i.type
        else:
            return self._type

    def pole(self, value):
        if self._pole == '':
            for i in value.values():
                if meter(i.coordinates, self._coordinates) < 2:
                    self._pole = i
                    return i
        else:
            return self._pole
