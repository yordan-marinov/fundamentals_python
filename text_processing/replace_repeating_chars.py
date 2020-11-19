string = input()

print(
    "".join(
        [
            e
            for i, e in enumerate(string)
            if i == 0 or e != string[i-1]
        ]
    )
)
# result = ""
# for index, letter in enumerate(string):
#     if index == 0 or letter != string[index - 1]:
#         result += letter
#
# print(result)
