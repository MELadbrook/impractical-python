import time
import random
import statistics

# CONSTANTS (weights in grams)
GOAL = 50000
NUM_RATS = 20
INITIAL_MIN_WT = 200
INITIAL_MAX_WT = 600
INITIAL_MODE_WT = 300
MUTATE_ODDS = 0.01
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
LITTER_SIZE = 8
LITTERS_PER_YEAR = 10
GENERATION_LIMIT = 500

# ensure even-number of rats for breeding pairs:
if NUM_RATS % 2 != 0:
    NUM_RATS += 1


def populate(num_rats, min_wt, max_wt, mode_wt):
    """Initialise a population with a trinagular distribution of weights."""
    return [int(random.triangular(min_wt, max_wt, mode_wt))\
            for i in range(num_rats)]


def fitness(population, goal):
    """Measure population fitness based on an attribute mean vs target."""
    ave = statistics.mean(population)
    return ave / goal


def select(population, to_retain):
    """Cull a population to retain only a specified number of members."""
    sorted_population = sorted(population)
    to_retain_by_sex = to_retain//2
    members_per_sex = len(sorted_population)//2
    females = sorted_population[:members_per_sex]
    males = sorted_population[members_per_sex:]
    selected_females = females[-to_retain_by_sex:]
    selected_males = males[-to_retain_by_sex:]
    return selected_males, selected_females


def breed(males, females, litter_size):
    """Crossover genes among members (weights) of a population."""
    random.shuffle(males)
    random.shuffle(females)
    children = []
    for male, female in zip(males, females):
        for child in range(litter_size):
            child = random.randint(female, male)
            children.append(child)
    return children


def mutate(children, mutate_odds, mutate_min, mutate_max):
    """Randomly alter rate weights using input odds & fractional changes."""
    for index, rate in enumerate(children):
        if mutate_odds >= random.random():
            children[index] = round(rat * random.uniform(mutate_min,
                                                         mutate_max))
    return children


