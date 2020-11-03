def swap(i_1, i_2, s_tring):
    s_tring[i_1], s_tring[i_2] = s_tring[i_2], s_tring[i_1]
    return s_tring


def multiply(i_1, i_2, s):
    result = s[i_1] * s[i_2]
    s[i_1] = result
    return s


string = [int(i) for i in input().split()]


while True:
    command = input()
    if command == "end":
        break

    token = command.split()
    operation = token[0]

    if operation == "swap":
        index_1 = int(token[1])
        index_2 = int(token[2])
        string = swap(index_1, index_2, string)

    elif operation == "multiply":
        index_1 = int(token[1])
        index_2 = int(token[2])
        string = multiply(index_1, index_2, string)

    else:
        string = [i - 1 for i in string]

print(", ".join([str(i) for i in string]))
