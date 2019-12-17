# Mon code
"""def counter_password(start, end):
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

           
        if previous.count(cpt) < 2 :
            no_triple = True

        if increasing and double and no_triple:
            nb_password += 1

    print(nb_password)


counter_password(256310, 732736)
"""
# Internet


def check_ascending(n):
    return "".join(sorted(n)) == n


def check_repeat(n):
    for digit1, digit2 in zip(n, n[1:]): 
        if digit1 == digit2:
            return True
            


def check_two_consecutive_digits(n):
    repeat_count = 0
    for n1, n2 in zip(n, n[1:]):
        if n1 == n2:
            repeat_count += 1
        else:
            if repeat_count == 1:
                return True
            repeat_count = 0
    return repeat_count == 1


p1_count = 0
p2_count = 0

for n in range(256310, 732736):
    n = str(n)
    if check_ascending(n):
        if check_repeat(n):
            p1_count += 1
        if check_two_consecutive_digits(n):
            p2_count += 1

print(f"Part 1: {p1_count}")
print(f"Part 2: {p2_count}")
