""" 
EXPLORER'S DILEMMA - aka the Knapsack Problem

After spending several days exploring a deserted island out in the Pacific,
you stumble upon a cave full of pirate loot! There are coins, jewels, paintings,
and many other types of valuable objects.

However as you begin to explore the cave and take stock of what you've found, 
you hear something. Turning to look, the cave has started to flood! You'll need 
to get to higher ground ASAP.

There IS enough time for you to fill your backpack with some of the items in the
cave. Given that...
- you have 60 seconds until the cave is underwater
- your backpack can hold up to 50 pounds
- you want to maximize the value of the items you retrieve -- you can only make
  one trip

How do you decide what to take?
"""

import random
import time
from itertools import combinations

class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.efficiency = 0

    def __str__(self):
        return f"{self.name}, {self.weight} lbs, ${self.value}"

    

def naive_fill_knapsack(sack, items):
    """
    Put highest value items in the knapsack until full.
    (other basic, naive approaches exist)
    """
    ## TODO - sort items by value
    # sorting on the key value, and reverse ordering them, most to least
    items.sort(key = lambda x: x.value, reverse = True)

    ## TODO - put most valubale items in until full
    # instantiate weight counter
    weight = 0
    # loop over item in items
    for item in items:
        # add item weight to weight counter
        weight += item.weight
        # if the weight exceeds 50
        if weight > 50:
            # return the sack
            return sack
        # else
        else:
            # append item to the sack
            sack.append(item)
    
    return sack


def brute_force_fill_knapsack(sack, items):
    """
    Try every combination to find the best.
    """
    # instantiate empty list
    combos = []

    # loop through all the possible items
    for i in range(1, len(items) + 1):
        # instantiate a list of possible combos using combinations from itertools
        list_of_combos = list(combinations(items, i))
        # loop through the list_of_combos
        for combo in list_of_combos:
            # Make them a list, and append them to empty combos list above
            combos.append(list(combo)) 
    
    # set an impossible best value
    best_value = -1
    # for each combo in the possible combinations
    for combo in combos:
        # value tracker
        value = 0
        # weight tracker
        weight = 0
        # loop through the items in the combo
        for item in combo:
            # add the item.value to the tracker variable
            value += item.value
            # add the item.weight to the tracker variable
            weight += item.weight
        # if the weight is less than or equal to 50
        # AND
        # the value tracker is greater than the best_value tracker
        if weight <= 50 and value > best_value:
            # add the value to the best_value tracker variable
            best_value += value
            # add that specific combo to the knapsack
            sack = combo

    return sack


def greedy_fill_knapsack(sack, items):
    """
    Use the ratio of [value] / [weight] to choose
    knapsack items.
    """
    # TODO - calculate efficiencies
    # loop through items in items
    for item in items:
        # efficiency equals the value to weight ratio
        item.efficiency = item.value / item.weight
    
    # TODO - sort items by efficiency
    items.sort(key = lambda x: x.efficiency, reverse = True)
    
    # TODO - put items in the knapsack until full
    # instantiate weight counter
    weight = 0
    # loop over item in items
    for item in items:
        # add item weight to weight counter
        weight += item.weight
        # if the weight exceeds 50
        if weight > 50:
            # return the sack
            return sack
        # else
        else:
            # append item to the sack
            sack.append(item)

    return sack 





##### TESTING ###### 

# Filling caves with items
small_cave = []
medium_cave = []
large_cave = []


def fill_cave_with_items():
    """
    Randomly generates Item objects and creates caves of differnet sizes for 
    testing.
    """
    names = ["painting", "jewel", "coin", "statue", "treasure chest", "gold",
             "silver", "sword", "goblet", "hat"]

    for _ in range(5):
        name = names[random.randint(0,4)]
        weight = random.randint(1,25)
        value = random.randint(1,100)
        small_cave.append(Item(name, weight, value))

    for _ in range(15):
        name = names[random.randint(0,4)]
        weight = random.randint(1,25)
        value = random.randint(1,100)
        medium_cave.append(Item(name, weight, value))

    for _ in range(25):
        name = names[random.randint(0,4)]
        weight = random.randint(1,25)
        value = random.randint(1,100)
        large_cave.append(Item(name, weight, value))


def print_results(items, knapsack):
    """
    Print out contents of what the algorithm calculated should be added to the 
    knapsack.
    """
    print("\nBest items to put in the knapsack: ")
    for item in knapsack:
        print(f"-{item}")
    print(f"\nResult caluclated in {time.time()-start:.5f} seconds\n")

    print("\n---------------------------------------")


## instantiating environment variables
fill_cave_with_items()
knapsack = []


## TEST 1 - Naive ##
print("\nStarting test 1, naive approach...")
items = large_cave
start = time.time()
knapsack = naive_fill_knapsack(knapsack, items)
print_results(items, knapsack)


# ## TEST 2 - Brute Force ##
# print("\nStarting test 2, brute force approach...")
# items = medium_cave
# start = time.time()
# knapsack = brute_force_fill_knapsack(knapsack, items)
# print_results(items, knapsack)


# ## TEST 3 - Brute Force ##
# print("\nStarting test 3, brute force approach...")
# items = large_cave
# start = time.time()
# knapsack = brute_force_fill_knapsack(knapsack, items)
# print_results(items, knapsack)


## TEST 4 - Greedy ##
print("\nStarting test 4, greedy approach...")
items = large_cave
start = time.time()
knapsack = greedy_fill_knapsack(knapsack, items)
print_results(items, knapsack)