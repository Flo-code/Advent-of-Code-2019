def counter_password(start, end):
    nb_password = 0

    for number in range(start, end + 1):
        increasing = True
        double = False
        no_triple = False
        previous = []
        for cpt in str(number):
            if len(previous) > 0:
                if cpt < previous[-1]:
                    increasing = False
                    break
                if previous.count(cpt) > 0:
                    double = True
            previous.append(cpt)

            if str(number).count(cpt) < 2:
                no_triple = True

        if increasing and double and no_triple:
            nb_password += 1

    print(nb_password)


counter_password(256310, 732736)

