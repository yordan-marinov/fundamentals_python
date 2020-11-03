string = input().split(", ")

for index, word in enumerate(string[::-1], 1):
    if word == "wolf" and index == 1:
        print("Please go away and stop eating my sheep")
        break
    elif word == "wolf":
        print(f"Oi! Sheep number {index - 1}! You are about to be eaten by a wolf!")
        break
