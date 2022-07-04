from helpers import meter


class Fiber:
    def __init__(self, stored=None, name=None, style=None, ):
        self._stored = stored
        self._name = name
        self._type = ''
        self._style = style

        self._length = 0.0
        self._route_fiber = []
        self._route_pole = []

    @property
    def route_fiber(self):
        return self._route_fiber

    @route_fiber.setter
    def route_fiber(self, route):
        for i in route.split(' '):
            self._route_fiber.append(i.split(','))

    @property
    def stored(self):
        return self._stored

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def style(self):
        return self._style

    @property
    def length(self):
        p = 0
        for i in self._route_fiber:
            if p == 0:
                p = i
                continue
            self._length += meter(i, p)
            p = i
        return self._length

    @length.setter
    def length(self, amount):
        self._length += amount
