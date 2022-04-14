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
                tipo_dado = str(d.findtext('{http://www.opengis.net/kml/2.2}displayName'))
                dado_poste = str(d.findtext('{http://www.opengis.net/kml/2.2}value'))
                # if "00" in str(d.findtext('{http://www.opengis.net/kml/2.2}displayName')):
                #     tipo_poste[numero_poste] = d.findtext('{http://www.opengis.net/kml/2.2}value')
                # else:
                #     "tem nao"
                tipo_poste[numero_poste] = tipo_dado if '00' in dado_poste else "tem nao"
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
                # print(tipo_dado, tipo_poste)
            numero_poste += 1

# print(tipo_poste)
