def electron_distribution(electrons_count: int):
    electrons = []
    distribution = 1
    while electrons_count > 0:

        electron = 2 * distribution ** 2

        if electrons_count < electron:
            electron = electrons_count

        distribution += 1
        electrons_count -= electron
        electrons.append(electron)

    print(electrons)


electron_distribution(int(input()))