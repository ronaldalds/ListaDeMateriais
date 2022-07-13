from math import sqrt, ceil
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


def box(value):
    c = 0
    for i in value:
        if 'CEO' == i.type or 'HUB-DPR' == i.type:
            c += 1
    return c


def presley(value):
    c = 0
    for i in value:
        if 'CTO-HUB' == i.type:
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
                name = f'{search[0]}-{p}'
                rede = Rede(name=name)
                for cto in list_cto:
                    sector = cto.name.split('.')[0]
                    pon = cto.name.split('.')[1]
                    if search[0] == sector and p == pon:
                        rede.cto = cto
                list_rede.append(rede)
    return list_rede


def rede_activated(point):
    redes = rede_project(point)
    c = 0
    for i in redes:
        if i.activated:
            c += 1
    return c


def rede_cto(point):
    cto_project = {}
    list_cto = [i for i in point if i.type == 'CTO' or i.type == 'CTO-Indoor']
    for i in list_cto:
        if i.description not in cto_project:
            cto_project[i.description] = 1
        else:
            cto_project[i.description] += 1
    return cto_project


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
    # list_spl = [i for i in point if i.type == 'CTO' or i.type == 'CTO-HUB' or i.type == 'HUB-DPR']
