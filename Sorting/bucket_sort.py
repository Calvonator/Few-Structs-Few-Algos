import random
#toSort = [round(random.uniform(0.10, 0.99), 2) for _ in range(20)]
toSort = [round(random.uniform(0.10, 0.99), 2) for i in range(10, 0, -1)]
print(toSort)

#Optimisation: Once each item is placed into a bucket, place the unsorted buckets back 
#              into the original list/array and insertoin sort that list
#
#Other options for similar algorithms:
#   - Efficient(?) Bucket Sort (That uses K buckets (where K < N))
#   - Proxmap Sort
#   - Histogram Sort
#   - Postman's Sort
#   - Shuffle Sort


def bucket_sort(xs, k):


    



    return






#Generic Bucket Sort that uses N buckets (N = len(input_list)) 
def generic_bucket_sort(xs):

    N = len(xs)

    buckets = [[] for _ in range(N)]
    sorted_buckets = []

    for index in range(N):

        bucket_num = N * xs[index] 
        print(bucket_num)
        buckets[int(bucket_num)].append(xs[index])

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


def insertion_sort(xs):
    #For each item in the array not including the first item (x). 

    for i in range(1, len(xs)):
        #Grab the value of the current item
        x = xs[i]
        
        #While the current item's index is above 0 and the value of the item
        #to the left is greater than the current item's value: swap the two values
        #and decrement i to the next value to the left.

        while i > 0 and xs[i - 1] > x:

            swap(xs, i, i - 1)
            i -= 1

#Swaps the position of the values at indexes y, z in the aray xs
def swap(xs, y, z):
    xs[y], xs[z] = xs[z], xs[y]

toSort = generic_bucket_sort(toSort)

print(toSort)

