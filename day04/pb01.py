def count_password(start, end):
    nb_password = 0

    for number in range(start, end + 1):
        increasing = True
        double = False

        previous = []

        for cpt in str(number):
            if len(previous) > 0:
                if cpt < previous[-1]:
                    increasing = False
                    break
                if previous.count(cpt) > 0:
                    double = True

            previous.append(cpt)

        if increasing and double:
            nb_password += 1

    return(nb_password)


print(count_password(256310, 732736))

