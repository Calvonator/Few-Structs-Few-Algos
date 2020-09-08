import random
#toSort = [round(random.uniform(0.10, 0.99), 2) for _ in range(20)]
toSort = [round(random.uniform(0.10, 0.99), 2) for i in range(10, 0, -1)]
print(toSort)



def bucket_sort(array):
    buckets = [[] for i in range(len(array))]
    sorted_buckets = []

    for index in range(len(array)):
        bucket_num = len(array) * array[index] 
        print(bucket_num)
        buckets[int(bucket_num)].append(array[index])

    for bucket in buckets:
        insertion_sort(bucket)
    
    for bucket in buckets:

        if len(bucket) == 0:
            continue

        elif len(bucket) > 1:
            for num in bucket:
                sorted_buckets.append(num)
        else:
            sorted_buckets.append(bucket[0])

    return sorted_buckets


def insertion_sort(array):

    for unsorted_val in range(1, len(array)):
        val = array[unsorted_val]
        val_index = unsorted_val

        while val_index > 0 and array[val_index - 1] > val:
            array[val_index] = array[val_index - 1]
            val_index -= 1
        array[val_index] = val


toSort = bucket_sort(toSort)

print(toSort)

