from helpers import meter


class Fiber:
    def __init__(self, stored=None, description=None, style=None, tp=None):
        self._stored = stored
        self._description = description
        self._type = tp
        self._style = style
        self._name = self.processing()
        self._route_fiber = []
        self._route_pole = []
        self._length = 0.0
        self._sco = []

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
            return f'Folder {self._stored[-2]} {self._stored[-3]} non default'

    @property
    def route_fiber(self):
        return self._route_fiber

    @route_fiber.setter
    def route_fiber(self, route):
        p = 0
        for i in route.split(' '):
            self._route_fiber.append(i.split(','))
        for i in self.route_fiber:
            if p == 0:
                p = i
                continue
            self._length += meter(i, p)
            p = i

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
        return self._length

    @length.setter
    def length(self, value):
        self._length += value

    @property
    def pole(self):
        return self._route_pole

    @pole.setter
    def pole(self, value):
        if not self._route_pole:
            p0 = 0
            for i in self._route_fiber:
                self._route_pole.append(i)
                for t in value:
                    if meter(t.coordinates, i) < 2:
                        self._route_pole.pop()
                        self._route_pole.append(t)
                        t.user = True
            for c, p in enumerate(self._route_pole):
                try:
                    p1 = p.coordinates
                except:
                    p1 = p
                if p0 == 0:
                    p0 = p1
                elif p1[0] < p0[0] and p1[1] > p0[1]:
                    self._sco.append(f'{self._route_pole[c - 1]};Q4')
                    self._sco.append(f'{p};Q1')
                elif p1[0] > p0[0] and p1[1] > p0[1]:
                    self._sco.append(f'{self._route_pole[c - 1]};Q3')
                    self._sco.append(f'{p};Q2')
                elif p1[0] < p0[0] and p1[1] < p0[1]:
                    self._sco.append(f'{self._route_pole[c - 1]};Q2')
                    self._sco.append(f'{p};Q3')
                elif p1[0] > p0[0] and p1[1] < p0[1]:
                    self._sco.append(f'{self._route_pole[c - 1]};Q1')
                    self._sco.append(f'{p};Q4')

    @property
    def sco(self):
        return self._sco
