population = list(map(int, input().split(", ")))
minimum_wealth = int(input())


distribution = True
for index in range(len(population)):

    wealthiest = max(population)
    if wealthiest == minimum_wealth and index != len(population) - 1:
        distribution = False
        break

    max_number_index = population.index(wealthiest)

    if population[index] < minimum_wealth:
        needed_values = minimum_wealth - population[index]
        population[index] += needed_values
        population[max_number_index] -= needed_values


if distribution:
    print(population)
else:
    print("No equal distribution possible")
