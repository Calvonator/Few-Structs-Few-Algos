import random
toSort = [random.randint(1, 10) for _ in range(10)]
#toSort = [i for i in range(10, 0, -1)]
print(toSort)


def deprecated_partition(array, pivot):            #Partitioning algorithm for creating two sub-arrays that are greater and less than the pivot.

    leftArr = []
    rightArr = []

    for num in array:
        if num < array[pivot]:
            leftArr.append(num)
        elif num > array[pivot]:
            rightArr.append(num)
           

def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)


def quick_sort_helper(array, left, right):
    if left < right:
        pivot_index = partition(array, left, right)
        quick_sort_helper(array, left, pivot_index - 1)
        quick_sort_helper(array, pivot_index + 1, right)


def partition(array, left, right):
    pivot = array[left]
    pivot_index = left

    for num in range(left + 1, right + 1):
        if array[num] < pivot:

            #array[num], array[pivot_index] = array[pivot_index], array[num]
            #array[num], array[pivot_index + 1] = array[pivot_index + 1], array[num]
            array[pivot_index] = array[num]
            array[num] = array[pivot_index + 1]
            
            array[pivot_index + 1] = pivot 
            
            pivot_index += 1

    return pivot_index

#p = partition(toSort, 0, len(toSort) - 1)
quick_sort(toSort)
print(toSort)
