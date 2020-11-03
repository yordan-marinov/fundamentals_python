year = int(input())


flag = False
while True:
    year += 1
    happy_year = ""
    for i in str(year):
        if i in happy_year:
            break
        happy_year += i
        if len(happy_year) == len(str(year)):
            flag = True

    if flag:
        break


print(year)
