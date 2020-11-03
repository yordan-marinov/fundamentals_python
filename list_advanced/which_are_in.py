substrings = input().split(", ")
strings = input()

print(
    [
        substring for substring in substrings
        if substring in strings
    ]
)
