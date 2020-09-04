import random
#toSort = [random.randint(1, 50) for _ in range(50)]
toSort = [i for i in range(10, 0, -1)]
print(toSort)


def insertion_sort(array):

    for unsorted_val in range(1, len(array)):
        val = array[unsorted_val]
        val_index = unsorted_val

        while val_index > 0 and array[val_index - 1] > val:
            array[val_index] = array[val_index - 1]
            val_index -= 1
        array[val_index] = val


insertion_sort(toSort)

print(toSort)