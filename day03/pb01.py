# tab[[], [], []]
def trace(x, y, dir, val, tab):

    if dir == "U":
        for i in range(val):
            tab[x, y + i] = 1
    if dir == "D":
        for i in range(val):
            tab[x, y - i] = 1
    if dir == "L":
        for i in range(val):
            tab[x - i, y] = 1
    if dir == "R":
        for i in range(val):
            tab[x + i, y] = 1
    return tab


def compare(tab1, tab2):
    tab = [[], []]
    for i in range(len(tab1)):
        for j in range(len(tab1[i])):
            if tab1[[i], [j]] == 1 and tab2[[i], [j]] == 1:
                return tab[[i], [j]]


def test():
    trace(0, 0, "U", 10, tab)
    print(tab)

