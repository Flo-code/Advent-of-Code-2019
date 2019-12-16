def read_data(filename):
    data = []
    with open(filename, "r") as f:
        for ligne in f:
            data.append(int(ligne))

    return data
