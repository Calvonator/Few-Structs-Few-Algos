import random
toSearch = [random.randint(1, 10) for _ in range(10)]

print(toSearch)

def linear_search(option, xs):

    if option == "max":
        max = linear_search_max(xs)
        return max

    elif option == "min":
        min = linear_search_min(xs)
        return min


def linear_search_max(xs):
    max = xs[0]

    for x in xs:
        if x > max:
            max = x

    return max

def linear_search_min(xs):
    min = xs[0]

    for x in xs:
        if x < min:
            min = x

    return min

def linear_search_min_max(xs):
    min = xs[0]
    max = xs[1]

    for x in xs:
        if x < min:
            min = x 
        elif x > max:
            max = x 
    return min, max
    
#value_index_max = linear_search("max", toSearch)
#value_index_min = linear_search("min", toSearch)
value_index_min, value_index_max = linear_search_min_max(toSearch)


print(f"Max: {value_index_max} Min: {value_index_min}")