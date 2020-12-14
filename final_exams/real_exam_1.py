# def main_manipulation_print_func(string: str, commands: dict) -> str:
#     while True:
#
#         data = input()
#         if data == "Sign up":
#             break
#
#         data = data.split(" ")
#         command = data.pop(0)
#
#         string = commands[command](string, *data)
#
#
# def case(string: str, *args) -> str:
#     current_command = args[0]
#
#     if current_command == "lower":
#         string = string.lower()
#         print(string)
#         return string
#     elif current_command == "upper":
#         string = string.upper()
#         print(string)
#         return string
#
#
# def reverse_string(string: str, *args) -> str:
#     start_index = int(args[0])
#     end_index = int(args[1])
#
#     if start_index in range(len(string)) and end_index in range(len(string)):
#         substring = string[start_index: end_index + 1]
#         print(substring[::-1])
#
#     return string
#
#
# def cut(string: str, *args) -> str:
#     substring = args[0]
#
#     if substring in string:
#         string = string.replace(substring, "", 1)
#         print(string)
#         return string
#     else:
#         print(f"The word {string} doesn't contain {substring}.")
#         return string
#
#
# def replace(string: str, *args) -> str:
#     char = args[0]
#
#     string = string.replace(char, "*")
#
#     print(string)
#     return string
#
#
# def check(string: str, *args) -> print:
#     char = args[0]
#     if char in string:
#         print("Valid")
#     else:
#         print(f"Your username must contain {char}.")
#
#
# COMMANDS = {
#     "Case": case,
#     "Reverse": reverse_string,
#     "Cut": cut,
#     "Replace": replace,
#     "Check": check,
# }
#
# raw_data = input()
# main_manipulation_print_func(raw_data, COMMANDS)

=================================================================

string = input()

while True:

    data = input()
    if data == "Sign up":
        break

    data = data.split()
    command = data[0]

    if command == "Case":
        subcommand = data[1]
        if subcommand == "lower":
            string = string.lower()
        else:
            string = string.upper()

        print(string)

    elif command == "Reverse":
        start_index = int(data[1])
        end_index = int(data[2])

        if start_index in range(len(string)) and end_index in range(len(string)):
            substring = string[start_index: end_index + 1]
            print(substring[::-1])

    elif command == "Cut":
        substring_1 = data[1]

        if substring_1 in string:
            string = string.replace(substring_1, "")
            print(string)
        else:
            print(f"The word {string} doesn't contain {substring_1}.")

    elif command == "Replace":
        char = data[1]
        string = string.replace(char, "*")
        print(string)

    elif command == "Check":
        character = data[1]

        if character in string:
            print("Valid")
        else:
            print(f"Your username must contain {character}.")
