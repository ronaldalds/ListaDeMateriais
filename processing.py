from math import sqrt, ceil
from functools import reduce

import pole
from upload_file import UploadFile
import re
from rede import Rede


def meter(x, y):
    cat1 = ((float(x[0])) - (float(y[0]))) * 1852 * 60
    cat2 = ((float(x[1])) - (float(y[1]))) * 1852 * 60
    h = sqrt((cat1 * cat1) + (cat2 * cat2))
    return ceil(h)


def element(icon=None, color=None):
    if 'shapes/donut.png' in icon and 'ff00ff00' in color:
        return 'CEO'
    elif 'shapes/donut.png' in icon and 'ff00ffff' in color:
        return 'CEO-Futura'
    elif 'shapes/donut.png' in icon and 'ff0000ff' in color:
        return 'HUB-DPR'
    elif 'shapes/polygon.png' in icon:
        return 'Reserva'
    elif 'shapes/square.png' in icon and 'ff0000ff' in color:
        return 'CTO-HUB'
    elif 'shapes/square.png' in icon and 'ff00ffff' in color:
        return 'CTO-HUB-Futura'
    elif 'paddle/red-diamond.png' in icon:
        return 'CTO'
    elif 'paddle/ltblu-diamond.png' in icon:
        return 'CTO-Indoor'
    elif 'paddle/ylw-diamond.png' in icon:
        return 'CTO-Futura'
    elif 'shapes/ranger_station.png' in icon:
        return 'POP'
    else:
        return 'non default'


def osnap(value, pole):
    for i in value:
        i.pole = pole


def tp(value, style):
    for i in value:
        i.type = style


def list_fiber(value):
    lines = {}
    for i in value:
        if i.length != 0:
            if i.name not in lines:
                lines[i.name] = i.length
            else:
                lines[i.name] += i.length
    return lines


def list_strap(value):
    strap = {}
    for i in value:
        if i.strap != 0:
            if i.name not in strap:
                strap[i.name] = i.strap
            else:
                strap[i.name] += i.strap
    return strap


def list_tie(value):
    tie = {}
    for i in value:
        if i.tie != 0:
            if i.name not in tie:
                tie[i.name] = i.tie
            else:
                tie[i.name] += i.tie
    return tie


def list_sco(value):
    sco = []
    for i in value:
        for t in i.sco:
            sco.append(t)
    return set(sco)


def pole_user(value):
    c = 0
    for i in value:
        if i.user:
            c += 1
    return c


def platelet_fusion(value):
    c = 0
    for i in value:
        c += i.platelet_fusion
    return c


def platelet_launch(value):
    c = 0
    for i in value:
        c += i.platelet_launch
    return c


def wire_la(value):
    c = 0
    for i in value:
        c += i.wire_launch
    return ceil(c / 130)


def wire_fus(value):
    c = 0
    for i in value:
        c += i.wire_fusion
    return ceil(c / 130)


def load_file(file):
    return UploadFile(file)


def rt(value):
    c = 0
    for i in value:
        if 'Reserva' in i.type:
            c += 1
    return c


def rede_project(point):
    list_hub = [i for i in point if i.type == 'CTO-HUB' or i.type == 'HUB-DPR']
    list_cto = [i for i in point if i.type == 'CTO' or i.type == 'CTO-Futura' or i.type == 'CTO-Indoor']
    list_rede = []
    hub = re.compile("([A-Z]{2})"
                     "[.]"
                     "([0-9]{1,2})"
                     "[']?"
                     "[1-2]?"
                     "[-]?"
                     "([0-9]{1,2})?"
                     "[']?"
                     "[1-2]?"
                     "[-]?"
                     "([0-9]{1,2})?"
                     "[']?"
                     "[1-2]?"
                     "([0-9]{1,2})?"
                     "[']?"
                     "[1-2]?"
                     )
    for i in list_hub:
        search = hub.search(i.name).groups()
        for p in search[1:-1]:
            if p is not None:
                name = f'{i.type};{search[0]}-{p}'
                rede = Rede(name=name)
                for cto in list_cto:
                    sector = cto.name.split('.')[0]
                    pon = cto.name.split('.')[1]
                    if search[0] == sector and p == pon:
                        rede.cto = cto
                list_rede.append(rede)
    return list_rede


def spliter(point):
    redes = rede_project(point)
    cont = {}
    for i in redes:
        for sp in i.spl_rede:
            if sp not in cont:
                cont[sp] = 1
            else:
                cont[sp] += 1
    return cont


def bap_fusion(point):
    bap = [i for i in point if i.type == 'CTO' or i.type == 'CTO-HUB']
    return len(bap) * 2


def prensa_fiber(point):
    prensa = [i for i in point if i.type == 'Reserva' or i.type == 'CEO' or i.type == 'HUB-DPR']
    return len(prensa) * 2


def tube_60(elemento):
    redes = rede_project(elemento[1])
    spl = spliter(elemento[1])
    feeder = [i for i in elemento[0] if i.type == 'AP' or i.type == 'AS']
    tube = 0
    for i in feeder:
        if type(i.pole[0]) == pole.Pole:
            if i.pole[0].eq[0].type == 'CTO-HUB':
                tube += i.qnt_fiber
        if type(i.pole[-1]) == pole.Pole:
            if i.pole[-1].eq[0].type == 'CTO-HUB':
                tube += i.qnt_fiber
    nc_1x8 = [spl[i] * 8 for i in spl if '1X8 G.657A NC-NC 250UM 2M/2M' in i]
    tube += reduce(lambda x, y: x + y, spl.values())
    tube += nc_1x8[0]
    tube += len([i for i in redes if i.activated is True])
    tube += len([i for i in elemento[1] if i.type == 'CTO'])
    return tube


def tube_45(elemento):
    feeder = [i for i in elemento[0] if i.type == 'AP' or i.type == 'AS']
    tube = 0
    for i in feeder:
        if type(i.pole[0]) == pole.Pole:
            if i.pole[0].eq[0].type == 'HUB-DPR' or i.pole[0].eq[0].type == 'CEO':
                tube += i.qnt_fiber
        if type(i.pole[-1]) == pole.Pole:
            if i.pole[-1].eq[0].type == 'HUB-DPR' or i.pole[-1].eq[0].type == 'CEO':
                tube += i.qnt_fiber
    return tube


def box(value):
    b = {}
    boxes = list(map(lambda x: x,
                     list(filter(lambda x: x.type == 'CEO' or
                                           x.type == 'HUB-DPR' or
                                           x.type == 'CTO-HUB' or
                                           x.type == 'CTO' or
                                           x.type == 'CTO-Indoor', value
                                 )
                          )
                     )
                 )

    for i in boxes:
        if i.description not in b:
            b[i.description] = 1
        else:
            b[i.description] += 1
    return b


def tray_presley(point):
    redes = rede_project(point)
    c = 0
    for i in redes:
        if i.activated and "CTO-HUB" in i.name:
            c += 1
    return c
