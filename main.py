from projeto import Projeto
from elemento import Elemento
from cabo import Cabo
from poste import Poste
from style import Style
from reserva import Reserva
from math import sqrt

cabo = Cabo('Projeto.kml')
poste = Poste('Projeto.kml')
elemento = Elemento('Projeto.kml')
style = Style('Projeto.kml')
projeto = Projeto('Projeto.kml')
reserva = Reserva('Projeto.kml')

# print(projeto.ext_style)
print(elemento.tipo_elemento)
# print(elemento.nome_elemento)
# print(elemento.coordenada_reserva)
# print(elemento.coordenada_elemento)