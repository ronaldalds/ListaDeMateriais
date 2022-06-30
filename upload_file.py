import xml.etree.ElementTree as Et
c = 0
e = 0
class UploadFile():
    def __init__(self,file):
        doc = Et.parse(file)
        self.root = doc.getroot()
        self.site = '{http://www.opengis.net/kml/2.2}'



    def line(self, item, name=None, type=None, coordinates=None):
        pass



    def point(self, item, name=None, type=None, coordinates=None):
        pass



    def style(self):
        pass
