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
            for d in t.iter('{http://www.opengis.net/kml/2.2}Data'):
                valor_poste = d.findtext('{http://www.opengis.net/kml/2.2}value')
                nome_tipo = str(d.findtext('{http://www.opengis.net/kml/2.2}displayName'))

                if "09" in str(d.findtext('{http://www.opengis.net/kml/2.2}displayName')):
                    tipo_poste[numero_poste] = d.findtext('{http://www.opengis.net/kml/2.2}value')
                    break
                else:
                    tipo_poste[numero_poste] = "========================"

            numero_poste += 1

print(tipo_poste)

# arquivo = Poste('Coreaú.kml')
#
#
# print(arquivo.extracao_tipo_poste)
# print(arquivo.extracao_coordenada_poste)
