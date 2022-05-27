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

def extracao(item,c, nome=None, tipo=None, coord=None):
    # global c
    if nome is None:
        nome = []
        tipo = []
        coord = []
    for i in item:
        if 'Document' in i.tag:
            extracao(i, nome, tipo, coord)
        elif 'Folder' in i.tag:
            nome.append(f'{i[0].text}')
            extracao(i, nome, tipo, coord)
            nome.pop()
        elif 'Placemark' in i.tag:
            for t in i.iter(line):
                c += 1
                nome.append(f'{i[0].text}')
                nome_fibra[c] = list(nome)
                nome.pop()
                tipo_fibra[c] = i.findtext(style)
                coordenada_fibra[c] = t.findtext(coordenada).strip().split(' ')


for ro in root.iter(pasta):
    if 'REDE FTTH' == ro.findtext(name).upper():
        extracao(ro,int(0))
for i in nome_fibra:
    print(i,nome_fibra[i])
# print(nome_fibra)
# print(tipo_fibra)
# print(coordenada_fibra)