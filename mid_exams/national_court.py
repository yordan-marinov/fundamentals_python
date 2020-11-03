worker_1 = int(input())
worker_2 = int(input())
worker_3 = int(input())

que = int(input())

serviced_people_per_hour = worker_1 + worker_2 + worker_3

hours = 0
while que > 0:
    hours += 1
    if hours % 4 == 0:
        continue

    que -= serviced_people_per_hour

print(f"Time needed: {hours}h.")
