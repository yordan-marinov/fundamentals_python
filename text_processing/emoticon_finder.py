string = input()

print(
    '\n'.join(
        [
            element + string[index + 1]
            for index, element in enumerate(string) if element == ":"
        ]
    )
)
