def find_digit(string):
    digit = ""
    for element in string:
        if element.isdigit():
            digit += element
    return int(digit)


def swapping_letters(string):
    swapped = [c for c in string if c.isalpha()]
    swapped[0], swapped[-1] = swapped[-1], swapped[0]
    return swapped


def word_decipher(string):
    first_letter = chr(find_digit(string))
    return first_letter + "".join(swapping_letters(string))


words = input().split()

print(" ".join([word_decipher(word) for word in words]))
