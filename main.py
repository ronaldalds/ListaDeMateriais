from projeto import Projeto
from cabo import Cabo
from poste import Poste
from math import sqrt
arquivo = Poste('Coreaú.kml')
arquivo2 = Cabo('Coreaú.kml')
coord_poste = arquivo.coordanada_poste
coord_cabo = arquivo2.percuso
# dis = arquivo2.distancia(coord_poste[1],coord_cabo[1][0])
# print(len(teste))
# print(teste[313][0])
a = 2
print(coord_poste[1],coord_cabo[a][0])
x = coord_poste[1]
y = coord_cabo[a][0]

cat1 = ((float(x[0])) - (float(y[0]))) * 1852 * 60
cat2 = ((float(x[1])) - (float(y[1]))) * 1852 * 60

h = sqrt((cat1 * cat1) + (cat2 * cat2))

print(h)