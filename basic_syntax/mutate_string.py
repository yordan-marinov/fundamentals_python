first_string = input()
second_string = input()

for i in range(len(first_string)):

    counter = 0
    mutated_sting = ""
    for c1, c2 in zip(first_string, second_string):
        if c1 != c2 and counter <= i:
            mutated_sting += c2
            counter += 1
            continue

        mutated_sting += c1

    print(mutated_sting)

    if second_string == mutated_sting:
        break
