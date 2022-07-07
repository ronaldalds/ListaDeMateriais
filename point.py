from helpers import meter
import re

class Point:
    def __init__(self, stored=None, name=None, style=None):
        self._stored = stored
        self._name = name
        self._type = ''
        self._style = style
        self._coordinates = []
        self._pole = ''
        self._length = 0

    @property
    def stored(self):
        return self._stored

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

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if 'CEO' == value:
            self._length = 15
        elif 'CEO-Futura' == value:
            self._length = 15
        elif 'HUB-DPR' == value:
            self._length = 15
        elif 'Reserva' == value:
            rt = re.compile("[0-9]{2,3}")
            search = rt.search(self.name)
            self._length = int(search.group())
        elif 'CTO-HUB' == value:
            self._length = 10
        elif 'CTO-HUB-Futura' == value:
            self._length = 10
        elif 'CTO' == value:
            self._length = 10
        elif 'CTO-Indoor' == value:
            self._length = 50
        elif 'CTO-Futura' == value:
            self._length = 10
        elif 'POP' == value:
            self._length = 80

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if self._type == '':
            for i in value:
                if self._style == i.identifier:
                    self._type = i.type
                    self.length = i.type

    @property
    def pole(self):
        return self._pole

    @pole.setter
    def pole(self, value):
        if self._pole == '':
            for i in value:
                if meter(i.coordinates, self._coordinates) < 2:
                    i.eq = self
                    self._pole = i
