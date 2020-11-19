def get_letter_position(letter: str):
    letter = letter.lower()
    return ord(letter) - 96


def string_number(lst):
    res = ""
    for num in lst:
        res += num

    return int(res)


def left_letter(letter, num):
    if letter.isupper():
        return num / get_letter_position(letter)
    return num * get_letter_position(letter)


def right_letter(letter_2, letter_1, num):
    if letter_2.isupper():
        return left_letter(letter_1, num) - get_letter_position(letter_2)
    return get_letter_position(letter_2) + left_letter(letter_1, num)


line = input().split()
sum_strings = 0
for string in line:
    string = list(string)
    first_letter = string.pop(0)
    second_letter = string.pop(-1)
    number = string_number(string)

    sum_strings += right_letter(second_letter, first_letter, number)

print(f"{sum_strings:.2f}")
