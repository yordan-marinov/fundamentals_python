events = {"coding": 0, "dog": 0, "cat": 0, "movie": 0}

MAXIMUM_NUMBER = 5

while True:
    command = input()
    if command == "END":
        break

    if command.lower() in events.keys():
        value = 1
        if command.isupper():
            value += 1
        events[command] = value

if sum(events.values()) > MAXIMUM_NUMBER:
    print("You need extra sleep")
else:
    print(sum(events.values()))
