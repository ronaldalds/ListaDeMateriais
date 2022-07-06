class Pole:
    def __init__(self, stored=None, style=None):
        self._stored = stored
        self._name = ''
        self._coordinates = []
        self._type = ''
        self._style = style
        self._height = 9
        self._effort = 300
        self._electric = ''
        self._house = 0
        self._business = 0
        self._apartments = ''
        self._equipment = ''
        self._code = ''
        self._occupation = ''
        self._pictures = ''
        self._client = 0
        self._user = False

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value):
        self._coordinates = value.split(',')

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, value):
        self._style = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def effort(self):
        return self._effort

    @effort.setter
    def effort(self, value):
        self._effort = value

    @property
    def electric(self):
        return self._electric

    @electric.setter
    def electric(self, value):
        self._electric = value

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, value):
        self._house = value

    @property
    def business(self):
        return self._business

    @business.setter
    def business(self, value):
        self._business = value

    @property
    def apartments(self):
        return self._apartments

    @apartments.setter
    def apartments(self, value):
        self._apartments = value

    @property
    def equipment(self):
        return self._equipment

    @equipment.setter
    def equipment(self, value):
        self._equipment = value

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, value):
        self._occupation = value

    @property
    def pictures(self):
        return self._pictures

    @pictures.setter
    def pictures(self, value):
        self._pictures = value
