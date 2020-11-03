def average_value_numbers(lst):
    return sum(lst) / len(lst)


def filtered_sequence(lst):
    return (
        [i for i in sorted(lst, reverse=True)
         if i > average_value_numbers(lst)]
    )


def final_printing_func(lst):
    if not numbers:
        print("No")
    elif len(numbers) <= 5:
        print(" ".join([str(i) for i in numbers]))
    else:
        print(" ".join([str(numbers[i]) for i in range(5)]))


numbers = [int(n) for n in input().split()]

numbers = filtered_sequence(numbers)

final_printing_func(numbers)
