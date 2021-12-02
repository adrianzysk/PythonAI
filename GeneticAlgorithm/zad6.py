import random
import math

def generate_population(size, x, y):
    lower_x, upper_x = x
    lower_y, upper_y = y

    population = []
    for i in range(size):
        one = {
            "x": random.uniform(lower_x, upper_x),
            "y": random.uniform(lower_y, upper_y),
        }
        population.append(one)

    return population

def apply_function(one):
    x = one["x"]
    y = one["y"]
    return math.sin(x*0.05)+math.sin(y*0.05)+(0.4*math.sin(x*0.15))+math.sin(y*0.15)


def sort_population(population):
    return sorted(population, key=apply_function)

def mutate(individual):
    x = one["x"] + random.uniform(-0.1, 0.1)
    y = one["y"] + random.uniform(-0.1, 0.1)

    lower, upper = (0, 100)

    x = min(max(x, lower), upper)
    y = min(max(y, lower), upper)

    return {"x": x, "y": y}

def tournament(population):
    next_generation = population
    x = random.randrange(-13,-1)
    y = random.randrange(-13,-1)
    if(apply_function(next_generation[x])>apply_function(next_generation[y])):
        next_generation.append(next_generation[x])
    else:
        next_generation.append(next_generation[y])
    del next_generation[x] 
    del next_generation[y]
    return next_generation

def make_next_generation(previous_population):
    next_generation = tournament(previous_population)
    best_one = sort_population(previous_population)[-1]
    population_size = len(next_generation)
    for i in range(population_size):             
        next_generation[i] = mutate(next_generation[i])
    next_generation.append(best_one)
    return next_generation

generations = 30

population = generate_population(size=13, x = (0, 100), y = (0, 100))

i = 1

while True:
    print(" Generation {i}")
    for one in population:
        print(one, apply_function(one))
    if i == generations:
        break
    i += 1
    population = make_next_generation(population)
    print("Average apply function:")
    print(sum(apply_function(individual) for individual in population)/13)
    print("Best one:")
    best_one = sort_population(population)[-1]
    print(best_one, apply_function(best_one))

best_one = sort_population(population)[-1]
print("Best one:")
print(best_one, apply_function(best_one))