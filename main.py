from projeto import Projeto
from elemento import Elemento
from cabo import Cabo
from poste import Poste
from math import sqrt

cabo = Cabo('Projeto.kml')
# poste = Poste('Projeto.kml')
# elemento = Elemento('Projeto.kml')
# style = Style('Projeto.kml')
# projeto = Projeto('Projeto.kml')
# reserva = Reserva('Projeto.kml')

print(cabo._nome_elemento)
# for i in cabo.somador(cabo.tipo_fibras(),cabo.comprimento_cabo()):
#     print(f'Cabo {i} - {cabo.somador(cabo.tipo_fibras(), cabo.comprimento_cabo())[i]:.2f} m')
# for i in cabo.somador(cabo.tipo_fibras(),cabo.alca):
#     print(f'Alça {i} - {cabo.somador(cabo.tipo_fibras(), cabo.alca)[i]} und')
# for i in cabo.somador(cabo.tipo_fibras(),cabo.laco):
#     print(f'Laço {i} - {cabo.somador(cabo.tipo_fibras(), cabo.laco)[i]} und')
# print(f'Bap - {len(cabo.bap_lancamento())} und')
# print(f'SCO - {len(set(cabo.sco()))} und')
# print(f'Plaqueta Lançamento - {cabo.plaqueta_lancamento} und')
# print(f'Reserva - {cabo.contador("Reserva")} und')
# print('==============================================================================')
# print(f'CEO DPR - {cabo.contador("CEO")+cabo.contador("HUB-DPR")}')
# print(f'CTO PRESLEY - {cabo.contador("CTO-HUB")}')
# print(f'CTO - {cabo.contador("CTO")}')
# print(f'CTO Indoor - {cabo.contador("CTO-Indoor")}')
# print(cabo.nome_por_elemento("CTO"))
# a = ["CTO"]
# print(cabo.nome_por_elemento(a))