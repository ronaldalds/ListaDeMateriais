from equipamento import Equipamento
equipamento = Equipamento('Projeto.kml')


# for i in equipamento.somador(equipamento.tipo_fibras(), equipamento.comprimento_cabo()):
#     print(f'Cabo {i} - {equipamento.somador(equipamento.tipo_fibras(), equipamento.comprimento_cabo())[i]:.2f} m')
# for i in equipamento.somador(equipamento.tipo_fibras(), equipamento.alca):
#     print(f'Alça {i} - {equipamento.somador(equipamento.tipo_fibras(), equipamento.alca)[i]} und')
# for i in equipamento.somador(equipamento.tipo_fibras(), equipamento.laco):
#     print(f'Laço {i} - {equipamento.somador(equipamento.tipo_fibras(), equipamento.laco)[i]} und')
# print(f'BRAÇADEIRA AJUSTÁVEL BAP4 (1000MM) C/ PARAFUSO - {len(equipamento.bap_lancamento())} und')
# print(f'SUPORTE PARA CABOS ÓPTICOS SCO1 - {len(set(equipamento.sco()))} und')
# print(f'PLAQUETA DE IDENTIFICAÇÃO DE CABO ÓPTICO ONLINE TELECOM - {equipamento.plaqueta_lancamento} und')
# print(f'FIO DE ESPINAR ISOLADO FEI-125 - 0 RL') # falta cálculos
# print(f'RESERVA TÉCNICA - {equipamento.contador("Reserva")} und')
# print(f'DERIVAÇÃO PREFORMADA P/ CORDOALHA DIELÉTRICA (6,4MM) - 0 und') # falta cálculos
# print('==============================================================================')
# print(f'CAIXA DE EMENDA ÓPTICA AÉREA 24F C/ SUPORTE RESERVA DPR - {equipamento.contador("CEO") + equipamento.contador("HUB-DPR")}')
# print(f'CAIXA DE DISTRIBUIÇÃO ÓPTICA CTO PRESLEY - {equipamento.contador("CTO-HUB")}')
# print(f'BANDEJA PARA CAIXA DE EMENDA ÓPTICA DPR - 0 und')# falta cálculos
# print(f'BANDEJA INFERIOR PARA CTO PRESLEY - 0 und')# falta cálculos
# print(f'KIT DE DERIVAÇÃO PARA CAIXA DE EMENDA ÓPTICA - 0 und')# falta cálculos
# print(f'CAIXA DE DISTRIBUIÇÃO OPTICA CTO MINI PRESLEY - {equipamento.contador("CTO")}')
# print(f'CAIXA TERMINAL ÓPTICA INDOOR CONECTORIZADA C/ SPLITTER 1X8 SMAP - {equipamento.contador("CTO-Indoor")}')
# for i in equipamento.spliter():
#     print(f'{i[0]} - {i[1]} und')

print(equipamento.bandeja_cto())