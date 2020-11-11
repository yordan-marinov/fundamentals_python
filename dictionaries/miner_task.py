from collections import defaultdict

miner_task = defaultdict(int)

while True:
    key = input()

    if key == "stop":
        [print(f"{k} -> {v}") for k, v in miner_task.items()]
        break

    quantity = int(input())
    miner_task[key] += quantity
