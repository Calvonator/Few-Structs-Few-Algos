import random
#toSort = [random.randint(1, 50) for _ in range(50)]
toSort = [i for i in range(10, 0, -1)]
print(toSort)


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


insertion_sort(toSort)

print(toSort)