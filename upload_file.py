import xml.etree.ElementTree as Et
from fiber import Fiber
from pole import Pole

c = 0
e = 0
p = 0


class UploadFile:
    def __init__(self, file):
        doc = Et.parse(file)
        self._root = doc.getroot()
        self.site = '{http://www.opengis.net/kml/2.2}'
        self._name_point = {}
        self._type_point = {}
        self._coordinates_point = {}

        self._style = {}
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
                    pole = Pole(stored=list(name))
                    coordinates = t.findtext(f'{self.site}coordinates')
                    pole.coordinates = coordinates
                    pole.style = style
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

                    name.append(f'{i[0].text}')
                    self._name_point[e] = list(name)
                    name.pop()
                    self._type_point[e] = i.findtext(f'{self.site}styleUrl').replace('#', '')
                    self._coordinates_point[e] = t.findtext(f'{self.site}coordinates').split(',')

    def _extractor_style(self):
        for root in self._root.iter(f'{self.site}Style'):
            if 'Style' in root.tag:
                self._style[root.attrib['id']] = ''
                for icon_style in root.iter(f'{self.site}IconStyle'):
                    cor_icon = icon_style.findtext(f'{self.site}color')
                    for icon in icon_style.iter(f'{self.site}Icon'):
                        tipo_icon = icon.findtext(f'{self.site}href').replace('http://maps.google.com/mapfiles/kml/',
                                                                              '')
                        if cor_icon is None:
                            for label in root.iter(f'{self.site}LabelStyle'):
                                cor_icon = label.findtext(f'{self.site}color')
                        self._style[root.attrib['id']] = f'{tipo_icon}{cor_icon}'

                if self._style[root.attrib['id']] == '':
                    for poly in root.iter(f'{self.site}PolyStyle'):
                        cor_poly = poly.findtext(f'{self.site}color')
                        self._style[root.attrib['id']] = cor_poly

                if self._style[root.attrib['id']] == '':
                    for line in root.iter(f'{self.site}LineStyle'):
                        cor_line = line.findtext(f'{self.site}color')
                        self._style[root.attrib['id']] = cor_line

        for root2 in self._root.iter(f'{self.site}StyleMap'):
            for pair in root2.iter(f'{self.site}Pair'):
                if 'normal' in pair.findtext(f'{self.site}key'):
                    trato_url = pair.findtext(f'{self.site}styleUrl').replace('#', '')
                    self._style[root2.attrib['id']] = self._style[trato_url]
