def max_sequence_equal_elements(list_elements):
    longest_sequence = []
    current_sequence = []

    for index, element in enumerate(list_elements):

        if not current_sequence or element == list_elements[index - 1]:
            start_sequence = True
        else:
            start_sequence = False

        if start_sequence:
            current_sequence.append(element)
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence.clear()
                longest_sequence.extend(current_sequence)

            current_sequence.clear()
            current_sequence.append(element)

    if len(longest_sequence) >= len(current_sequence):
        return " ".join(str(e) for e in longest_sequence)
    else:
        return " ".join(str(e) for e in current_sequence)


elements = [int(i) for i in input().split()]

print(max_sequence_equal_elements(elements))
