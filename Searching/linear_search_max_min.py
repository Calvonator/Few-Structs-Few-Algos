import random
toSearch = [random.randint(1, 1000) for _ in range(50)]

print(toSearch)

def linear_search(option, array):

    if option == "max":
        max = linear_search_max(array)
        return max

    elif option == "min":
        min = linear_search_min(array)
        return min

def linear_search_max(array):
    max = array[0]

    for item in array:
        if item > max:
            max = item

    return max

def linear_search_min(array):
    min = array[0]

    for item in array:
        if item < min:
            min = item

    return min

value_index_max = linear_search("max", toSearch)
value_index_min = linear_search("min", toSearch)

print(f"Max: {value_index_max} Min: {value_index_min}")