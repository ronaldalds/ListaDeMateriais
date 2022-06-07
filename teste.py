import xml.etree.ElementTree as Et

doc = Et.parse('Projeto.kml')
root = doc.getroot()
pasta = '{http://www.opengis.net/kml/2.2}Folder'
name = '{http://www.opengis.net/kml/2.2}name'
placemark = '{http://www.opengis.net/kml/2.2}Placemark'
ponto = '{http://www.opengis.net/kml/2.2}Point'
coordenada = '{http://www.opengis.net/kml/2.2}coordinates'
line = '{http://www.opengis.net/kml/2.2}LineString'
style = '{http://www.opengis.net/kml/2.2}styleUrl'
poly = '{http://www.opengis.net/kml/2.2}Polygon'

nome_elemento = {}
tipo_elemento = {}
coordenada_elemento = {}

nome_fibra = {}
tipo_fibra = {}
coordenada_fibra = {}

nome_polygono = {}
coordenada_polygono = {}
# c = 0

for ro in root.findall('Rede'):
    print(ro.tail)
