import os
from utils import read_data


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
    tab = read_data(os.path.join(os.path.dirname(__file__), "data.txt"))

    return compute_total_fuel(tab)


if __name__ == "__main__":
    print(test())
