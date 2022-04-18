# from poste import Poste
import xml.etree.ElementTree as Et

doc = Et.parse('Coreaú.kml')
root = doc.getroot()
numero_poste = 1

tipo_poste = {}
latitude = {}
longitude = {}
altura_poste = {}
esforco_poste = {}
rede_eletrica = {}
quantidade_casa = {}
quantidade_comercio = {}
quantidade_apartamento = {}
tipo_equipamento = {}
codigo_poste = {}
ocupacao = {}

for i in root.iter('{http://www.opengis.net/kml/2.2}Folder'):
    if 'Poste' in i.findtext('{http://www.opengis.net/kml/2.2}name'):
        for t in i.iter('{http://www.opengis.net/kml/2.2}Placemark'):
            for coord in t.iter('{http://www.opengis.net/kml/2.2}Point'):

                print(numero_poste,coord.findtext('{http://www.opengis.net/kml/2.2}coordinates'))
            #     break
            numero_poste += 1

# print(tipo_poste)

# arquivo = Poste('Coreaú.kml')
#
#
# print(arquivo.extracao_tipo_poste)
# print(arquivo.extracao_coordenada_poste)
