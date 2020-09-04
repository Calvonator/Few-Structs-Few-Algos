import random
toSort = [random.randint(1, 50) for _ in range(50)]
#toSort = [i for i in range(10, 0, -1)]
print(toSort)

#Modified to return an index instead of the value of the min value
def linear_search_min(left, array):
    min = array[left]
    min_index = left

    for item_index in range(left + 1, len(array)):
        if array[item_index] < min:
            min = array[item_index]
            min_index = item_index

    return min_index


def selection_sort(array):    

    for x in range(len(array)):
        min = linear_search_min(x, array)
        #if min + 2 != x:
        array[x], array[min] = array[min], array[x]
    
    #return array

def selection_sort_self_contained(array):    

    for x in range(len(array)):
        min = array[x]
        min_index = x
        for z in range(x + 1, len(array)):
            if min > array[z]:
                min = array[z]
                min_index = z
        array[x], array[min_index] = array[min_index], array[x]

selection_sort_self_contained(toSort)

print(toSort)