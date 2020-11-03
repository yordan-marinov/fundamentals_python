def read_string_to_list(separator=", "):
    return [s for s in input().split(separator)]


def is_palindrome(number: str):
    return number == number[::-1]


def palindrome_integer(numbers: list):
    return "\n".join(
        [str(is_palindrome(n)) for n in numbers]
    )


print(palindrome_integer(read_string_to_list()))
