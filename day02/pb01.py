def assist_program(tab):
    for cpt in range(0, len(tab), 4):
        opcode = tab[cpt]
        value_a = tab[tab[cpt + 1]]
        value_b = tab[tab[cpt + 2]]

        if opcode == 99:
            return tab[0]

        elif opcode == 1:
            tab[tab[cpt + 3]] = value_a + value_b

        elif opcode == 2:
            tab[tab[cpt + 3]] = value_a * value_b

    return tab[0]


def test():
    tab = []
    with open("day02/data.txt", "r") as data_file:
        for ligne in data_file:
            tab = [int(s) for s in ligne.split(",")]
    tab[1] = 12
    tab[2] = 2
    print(assist_program(tab))


test()
