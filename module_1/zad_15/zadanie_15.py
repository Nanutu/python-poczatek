from module_1 import math


def avg_spd(time, dst):
    spd = int(dst)/int(time)
    return spd


def przeciwprostokatna(przyp1, przyp2):
    c = math.sqrt(math.pow(przyp1, 2) + math.pow(przyp2, 2))
    return c


print(przeciwprostokatna(4, 3))


def kalk_lokat(kapital, oprocentowanie, okres):
    value = int(kapital) * (1 + int(oprocentowanie)/100)**int(okres)
    return value

