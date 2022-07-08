from math import sqrt, ceil
from upload_file import UploadFile


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
        print(i.strap)
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


def load_file(file):
    return UploadFile(file)
