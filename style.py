class Style:
    def __init__(self, identifier):
        self._identifier = identifier
        self._icon = ''
        self._color = ''

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
