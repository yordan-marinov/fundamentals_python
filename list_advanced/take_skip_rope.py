from collections import deque


def all_digits_list(string):
    digits = [d for d in string if d.isdigit()]
    non_digits = [e for e in encrypted_massage if not e.isdigit()]
    return digits, non_digits


def take_skip_lists_filter(lst):
    take = [int(lst[i]) for i in range(len(lst)) if i % 2 == 0]
    skip = [int(numbers[i]) for i in range(len(numbers)) if i % 2 != 0]
    return take, skip


def take_skip_indexes(lst_take, lst_skip):
    return [
        num
        for pair in zip(lst_take, lst_skip)
        for num in pair
    ]


def decrypter(lst):
    decrypted_massage = []
    for index in range(len(lst)):
        for j in range(lst[index]):

            if not non_numbers:
                break

            if index % 2 == 0:
                decrypted_massage.append(non_numbers.popleft())
            else:
                non_numbers.popleft()

    return "".join(decrypted_massage)


encrypted_massage = input()

numbers, non_numbers = all_digits_list(encrypted_massage)
non_numbers = deque(non_numbers)

take_list, skip_list = take_skip_lists_filter(numbers)
take_skip_list = take_skip_indexes(take_list, skip_list)

print(decrypter(take_skip_list))
