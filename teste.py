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

def extracao(item, a=None):
    if a is None:
        a = []
    for i in item:
        if 'Document' in i.tag:
            extracao(i, a)
        elif 'Folder' in i.tag:
            a.append(f'{i[0].text}')
            extracao(i, a)
            a.pop()
        elif 'Placemark' in i.tag:
            for t in i.iter(line):
                print(f'{a}{i[0].text} {t.findtext(coordenada).strip()}')
            for t in i.iter(ponto):
                print(f'{i.findtext(style)}{i[0].text} {t.findtext(coordenada)}')


for ro in root.iter(pasta):
    if 'REDE FTTH' == ro.findtext(name).upper():
        extracao(ro)
