from helpers import element
class Style:
    def __init__(self, identifier):
        self._identifier = identifier
        self._icon = ''
        self._color = ''
        self._width = 0.0
        self._type = ''

    @property
    def identifier(self):
        return self._identifier

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value.replace('http://maps.google.com/mapfiles/kml/', '')

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def type(self):
        return self._type

    def types(self):
        self._type = element(icon=self.icon, color=self.color)


class Style_Map:
    def __init__(self, identifier):
        self._identifier = identifier
        self._pair = ''
        self._type = ''

    @property
    def identifier(self):
        return self._identifier

    @property
    def pair(self):
        return self._pair

    @pair.setter
    def pair(self, value):
        self._pair = value.replace('#', '')

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
