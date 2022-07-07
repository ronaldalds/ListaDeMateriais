from helpers import meter


class Fiber:
    def __init__(self, stored=None, description=None, style=None, tp=None):
        self._stored = stored
        self._description = description
        self._type = tp
        self._style = style
        self._name = self.processing()

        self._length = 0.0
        self._route_fiber = []
        self._route_pole = []



    def processing(self):
        if self._type.upper() == 'RA':
            if '12F' in self._description.split('-')[1]:
                return 'CFOA-SM-ASU80-S 12F MINI-RA'
            if '06F' in self._description.split('-')[1]:
                return 'CFOA-SM-ASU80-S 06F MINI-RA'
            return 'CFOA-SM-ASU80-S 12F MINI-RA'
        elif self._type == 'AP' or self._type == 'AS':
            return self._description.split('|')[2].strip()
        elif 'CORDOALHA' in self._type:
            return 'CORDOALHA'
        else:
            return 'Pasta fora do padrão'

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
    def description(self):
        return self._description

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

    def route_pole(self, value):
        if not self._route_pole:
            for i in self._route_fiber:
                self._route_pole.append(i)
                for t in value.values():
                    if meter(t.coordinates, i) < 1:
                        self._route_pole.pop()
                        self._route_pole.append(t)
            return self._route_pole
