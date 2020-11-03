def car_time(times_list: list):
    total_time = 0
    for time in times_list:
        if time == 0:
            total_time *= 0.8
        total_time += time
    return total_time


list_of_numbers = list(map(int, input().split()))

finish_line_index = len(list_of_numbers) // 2

left_car_line = list_of_numbers[0:finish_line_index]
right_car_line = list(reversed(list_of_numbers[finish_line_index + 1:]))

left_car_time = car_time(left_car_line)
right_car_time = car_time(right_car_line)

winner = ""
if left_car_time < right_car_time:
    winner_time = left_car_time
    winner = "left"
elif right_car_time < left_car_time:
    winner_time = right_car_time
    winner = "right"


print(f"The winner is {winner} with total time: {winner_time:.1f}")
