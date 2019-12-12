from pb01 import compute_fuel


def extra_fuel(mass):
    if mass <= 0:
        return 0
    return compute_fuel(mass) + extra_fuel(compute_fuel(mass))


def total_extra_fuel(tab):
    res = 0
    for i in tab:
        res = res + extra_fuel(i)
    return res


def test():
    data_file = open("day01/data.txt", "r")
    tab = []
    for ligne in data_file:
        tab.append(int(ligne))
    data_file.close()

    return total_extra_fuel(tab)


print(test())
