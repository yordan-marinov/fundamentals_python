string = input()

print(
    "".join(
        [
            symbol
            for index, symbol in enumerate(string)
            if index == 0 or symbol != string[index - 1]
        ]
    )
)
# result = ""
# for index, letter in enumerate(string):
#     if index == 0 or letter != string[index - 1]:
#         result += letter
#
# print(result)
