def assist_program(tab):
    tab_test = tab[:]
    for cpt in range(0, len(tab_test), 4):
        opcode = tab_test[cpt]
        value_a = tab_test[tab_test[cpt + 1]]
        value_b = tab_test[tab_test[cpt + 2]]

        if opcode == 99:
            return tab_test[0]

        elif opcode == 1:
            tab_test[tab_test[cpt + 3]] = value_a + value_b

        elif opcode == 2:
            tab_test[tab_test[cpt + 3]] = value_a * value_b

    return tab_test[0]


def research_combination(tab):

    for noun in range(len(tab)):
        for verb in range(len(tab)):
            tab[1] = noun
            tab[2] = verb
            res = assist_program(tab)

            if res == 19690720:
                print(100 * noun + verb)


def test():
    tab = []
    with open("day02/data.txt", "r") as data_file:
        for ligne in data_file:
            tab = [int(s) for s in ligne.split(",")]

    tab[1] = 12
    tab[2] = 2

    research_combination(tab)


test()
