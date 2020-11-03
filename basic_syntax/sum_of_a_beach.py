string = input().lower()

searched_words = ["sand", "water", "fish", "sun"]
counter = 0
for searched_word in searched_words:
    while searched_word in string:
        counter += 1
        string = string.replace(searched_word, "", 1)

print(counter)
