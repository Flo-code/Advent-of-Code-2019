def compute_fuel(mass):
    val = 0
    if mass // 3 > 2:
        val = mass // 3 - 2
    return val


def compute_total_fuel(tab):
    res = 0
    for i in tab:
        res = res + compute_fuel(i)
    return res


def test():
    data_file = open("day01/data.txt", "r")
    tab = []
    for ligne in data_file:
        tab.append(int(ligne))
    data_file.close()

    return compute_total_fuel(tab)


print(test())
