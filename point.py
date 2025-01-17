import processing
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
        self._platelet_fusion = 0
        self._platelet_launch = 0
        self._wire_fusion = 0
        self._wire_launch = 0
        self._description = ''

    @property
    def description(self):
        return self._description

    @property
    def wire_fus(self):
        return self._wire_fusion

    @property
    def wire_la(self):
        return self._wire_launch

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
    def platelet_fus(self):
        return self._platelet_fusion

    @property
    def platelet_la(self):
        return self._platelet_launch

    @property
    def name(self):
        return self._name

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if 'CEO' == value:
            self._wire_launch = 2
            self._platelet_fusion = 1
            self._platelet_launch = 1
            self._length = 15
            self._description = 'CAIXA DE EMENDA ÓPTICA AÉREA 24F C/ SUPORTE RESERVA DPR'
        elif 'CEO-Futura' == value:
            self._platelet_fusion = 1
            self._platelet_launch = 1
            self._length = 15
            self._description = 'CAIXA DE EMENDA ÓPTICA AÉREA 24F C/ SUPORTE RESERVA DPR'
        elif 'HUB-DPR' == value:
            self._wire_launch = 2
            self._platelet_fusion = 1
            self._platelet_launch = 1
            self._length = 15
            self._description = 'CAIXA DE EMENDA ÓPTICA AÉREA 24F C/ SUPORTE RESERVA DPR'
        elif 'Reserva' == value:
            rt = re.compile("[0-9]{2,3}")
            search = rt.search(self.name)
            self._length = int(search.group())
            self._wire_launch = 2
            self._platelet_launch = 1
        elif 'CTO-HUB' == value:
            self._platelet_fusion = 1
            self._platelet_launch = 1
            self._length = 10
            self._description = 'CAIXA DE DISTRIBUIÇÃO ÓPTICA CTO PRESLEY'
        elif 'CTO-HUB-Futura' == value:
            self._platelet_fusion = 1
            self._platelet_launch = 1
            self._length = 10
            self._description = 'CAIXA DE DISTRIBUIÇÃO ÓPTICA CTO PRESLEY'
        elif 'CTO' == value:
            self._wire_fusion = 1
            self._platelet_fusion = 1
            self._length = 10
            self._description = 'CAIXA DE DISTRIBUIÇÃO OPTICA CTO MINI PRESLEY'
        elif 'CTO-Indoor' == value:
            self._length = 50
            self._description = 'CAIXA TERMINAL ÓPTICA INDOOR CONECTORIZADA C/ SPLITTER 1X8 SMAP'
        elif 'CTO-Futura' == value:
            self._platelet_fusion = 1
            self._length = 10
            self._description = 'CAIXA DE DISTRIBUIÇÃO OPTICA CTO MINI PRESLEY'
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
                if processing.meter(i.coordinates, self._coordinates) < 4:
                    i.eq = self
                    self._pole = i
