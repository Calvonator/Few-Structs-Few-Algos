import random
toSearch = [random.randint(1, 50) for _ in range(50)]

print(toSearch)

def linear_search(target, array):
    index = 0
    for item in array:
        if item == int(target):
            return index
        index += 1

targ = input("Please enter a target: ")

value_index = linear_search(targ, toSearch)

print(value_index)