from projeto import Projeto
from elemento import Elemento
from cabo import Cabo
from poste import Poste
from style import Style
from reserva import Reserva
from math import sqrt

# cabo = Cabo('Projeto.kml')
# poste = Poste('Projeto.kml')
elemento = Elemento('Projeto.kml')
# style = Style('Projeto.kml')
projeto = Projeto('Projeto.kml')
# reserva = Reserva('Projeto.kml')

print(elemento.coordenada_elemento)
print(elemento.nome_elemento)
print(elemento.tipo_elemento)
# print(cabo.comprimento_cabo(4))
# print(cabo.ceo)
# print(cabo.reserva)
# print(projeto.fibra_rede('nome')[49])
# print(projeto.fibra_rede('linha')[49])
# print(cabo.coordenadas)

# print(cabo.tratamento())
# print(cabo.percuso_poste)
# print(poste.coordenada_pop_poste)
# print(poste.foto)
# print(projeto.ext_style)
#
#
# print(elemento.poste_elemento)
# print(elemento.coordenada_por_elemento('Reserva'))
# print(elemento.poste_por_elemento('Reserva'))
# print(f"Reserva = {elemento.contador('Reserva')}")
# print(f"CTO = {elemento.contador('CTO')}")
# print(f" = {elemento.contador('CTO-HUB')}")
# print(elemento.coordenada_elemento)