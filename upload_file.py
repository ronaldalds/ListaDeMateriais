import xml.etree.ElementTree as Et
from fiber import Fiber
from pole import Pole
from point import Point
from style import Style, Style_Map

c = 0
e = 0
p = 0


class UploadFile:
    def __init__(self, file):
        doc = Et.parse(file)
        self._root = doc.getroot()
        self.site = '{http://www.opengis.net/kml/2.2}'  # 'http://maps.google.com/mapfiles/kml/'
        self._name_point = {}
        self._type_point = {}
        self._coordinates_point = {}

        self._style = []
        self._pole = {}
        self.fiber = {}
        self.element = {}

    def data_pole(self):
        for ro in self._root.iter(f'{self.site}Folder'):
            if 'POSTE' in ro[0].text.upper():
                self._extractor_pole(ro)
                return self._pole

    def fiber_rede(self):
        for ro in self._root.iter(f'{self.site}Folder'):
            if 'REDE FTTH' == ro[0].text.upper():
                self._extractor_line(ro)
                return self.fiber

    def placemark_rede(self):
        for ro in self._root.iter(f'{self.site}Folder'):
            if 'REDE FTTH' == ro[0].text.upper():
                self._extractor_element(ro)
                return self.element

    def data_expansion(self, file):
        pass

    def _extractor_pole(self, item, name=None):
        global p
        if name is None:
            name = []
        for i in item:
            if 'Document' in i.tag:
                self._extractor_pole(i, name)
            elif 'Folder' in i.tag:
                name.append(f'{i[0].text}')
                self._extractor_pole(i, name)
                name.pop()
            elif 'Placemark' in i.tag:
                for t in i.iter(f'{self.site}Point'):
                    style = i.findtext(f'{self.site}styleUrl').replace('#', '')
                    p += 1
                    pole = Pole(stored=list(name), style=style)
                    coordinates = t.findtext(f'{self.site}coordinates')
                    pole.coordinates = coordinates
                    for data in i.iter(f'{self.site}Data'):
                        if '00' in data.attrib['name']:
                            pole.type = data.findtext(f'{self.site}value')
                        elif '01' in data.attrib['name']:
                            pole.height = data.findtext(f'{self.site}value')
                        elif '02' in data.attrib['name']:
                            pole.effort = data.findtext(f'{self.site}value')
                        elif '03' in data.attrib['name']:
                            pole.electric = data.findtext(f'{self.site}value')
                        elif '04' in data.attrib['name']:
                            pole.house = data.findtext(f'{self.site}value')
                        elif '05' in data.attrib['name']:
                            pole.business = data.findtext(f'{self.site}value')
                        elif '06' in data.attrib['name']:
                            pole.apartments = data.findtext(f'{self.site}value')
                        elif '07' in data.attrib['name']:
                            pole.equipment = data.findtext(f'{self.site}value')
                        elif '08' in data.attrib['name']:
                            pole.code = data.findtext(f'{self.site}value')
                        elif '09' in data.attrib['name']:
                            pole.occupation = data.findtext(f'{self.site}value')
                        elif 'pictures' in data.attrib['name']:
                            pole.pictures = data.findtext(f'{self.site}value')
                    name.append(f'{i[0].text}')
                    name.pop()
                    self._pole[p] = pole

    def _extractor_line(self, item, name=None):
        global c
        if name is None:
            name = []
        for i in item:
            if 'Document' in i.tag:
                self._extractor_line(i, name)
            elif 'Folder' in i.tag:
                name.append(f'{i[0].text}')
                self._extractor_line(i, name)
                name.pop()
            elif 'Placemark' in i.tag:
                for t in i.iter(f'{self.site}LineString'):
                    c += 1
                    style = i.findtext(f'{self.site}styleUrl').replace('#', '')
                    coordinates = t.findtext(f'{self.site}coordinates').strip()
                    fiber = Fiber(stored=list(name), name=i[0].text, style=style)
                    fiber.route_fiber = coordinates
                    fiber.type = name[-1]
                    name.append(f'{i[0].text}')
                    name.pop()
                    self.fiber[c] = fiber

    def _extractor_element(self, item, name=None):
        global e
        if name is None:
            name = []
        for i in item:
            if 'Document' in i.tag:
                self._extractor_element(i, name)
            elif 'Folder' in i.tag:
                name.append(f'{i[0].text}')
                self._extractor_element(i, name)
                name.pop()
            elif 'Placemark' in i.tag:
                for t in i.iter(f'{self.site}Point'):
                    e += 1
                    style = i.findtext(f'{self.site}styleUrl').replace('#', '')
                    coordinates = t.findtext(f'{self.site}coordinates')
                    point = Point(stored=list(name), name=i[0].text, style=style)
                    point.coordinates = coordinates
                    name.append(f'{i[0].text}')
                    name.pop()
                    self.element[e] = point

    def extractor_style(self):
        for root in self._root.iter(f'{self.site}Style'):
            style = Style(identifier=root.attrib['id'])
            for styles in root:
                if 'IconStyle' in styles.tag:
                    for icon_style in styles:
                        if 'color' in icon_style.tag:
                            style.color = icon_style.text
                        if f'{self.site}Icon' == icon_style.tag:
                            style.icon = icon_style.findtext(f'{self.site}href')
                if 'LineStyle' in styles.tag:
                    for line_style in styles:
                        if 'color' in line_style.tag:
                            style.color = line_style.text
                        if 'width' in line_style.tag:
                            style.width = line_style.text
                if 'PolyStyle' in styles.tag:
                    for poly_style in styles:
                        if 'color' in poly_style.tag:
                            style.color = poly_style.text
            style.types()
            self._style.append(style)
        for root in self._root.iter(f'{self.site}StyleMap'):
            style_map = Style_Map(identifier=root.attrib['id'])
            for pair in root.iter(f'{self.site}Pair'):
                if 'normal' in pair.findtext(f'{self.site}key'):
                    style_map.pair = pair.findtext(f'{self.site}styleUrl')
                    for i in self._style:
                        if style_map.pair == i.identifier:
                            style_map.type = i.type

            self._style.append(style_map)
        return self._style
