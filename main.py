# from poste import Poste
import xml.etree.ElementTree as Et

doc = Et.parse('Coreaú.kml')
root = doc.getroot()
numero_poste = 1

percuso = []
comprimento = 0.0
tipo_alca = ""
tipo_laco = ""
quantidade_de_fibra_no_cabo = 0
vao_suportado = 0
peso_do_cabo = 0.0
diametro_externo = 0.0
pressao_do_vento = 0.0
pasta = '{http://www.opengis.net/kml/2.2}Folder'
name = '{http://www.opengis.net/kml/2.2}name'
placemark = '{http://www.opengis.net/kml/2.2}Placemark'
data = '{http://www.opengis.net/kml/2.2}Data'
displayName = '{http://www.opengis.net/kml/2.2}displayName'
value = '{http://www.opengis.net/kml/2.2}value'
point = '{http://www.opengis.net/kml/2.2}Point'
coordinates = '{http://www.opengis.net/kml/2.2}coordinates'
lineString = '{http://www.opengis.net/kml/2.2}LineString'

for i in root.iter(placemark):
    for t in i.iter(lineString):
        print(i.findtext(name),t.findtext(coordinates).strip())
    # for t in i.iter(lineString):
    #     print(i.findtext(name))
    #     break