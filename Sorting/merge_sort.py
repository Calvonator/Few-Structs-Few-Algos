import random
#toSort = [random.randint(1, 50) for _ in range(50)]
toSort = [i for i in range(10, 0, -1)]
print(toSort)



def merge_sort(array):
    copy_buffer = [None] * (len(array))
    merge_sort_helper(array, copy_buffer, 0, len(array))


def merge_sort_helper(array, copy_buffer, left, right):
    if left < right:
        middle = (left + right) // 2
        merge_sort_helper(array, copy_buffer, left, middle)
        merge_sort_helper(array, copy_buffer, middle + 1, right)
        merge(array, copy_buffer, left, middle, right)
    
def merge(array, copy_buffer, left, middle, right):
    #Initialise item1, item2 as the first items in each subarray
    item1 = left
    item2 = middle + 1 

    for i in range(left, right + 1):
        if item1 > middle:                      #1st subarry is exhausted
            copy_buffer[i] = array[item2]
            item2 += 1
        
        elif item2 > right:                      #2nd subarray is exhausted
            copy_buffer[i] = array[item1]
            item1 += 1

        elif array[item2] > array[item1]:
            copy_buffer[i] = array[item1]
            item1 += 1

        else:
            copy_buffer[i] = array[item2]
            item2 += 1

    for i in range(left, right + 1):
        array[i] = copy_buffer[i]


merge_sort(toSort)

print(toSort)