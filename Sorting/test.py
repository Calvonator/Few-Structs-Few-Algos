import random
toSort = [random.randint(1, 50) for _ in range(50)]
#toSort = [i for i in range(10, 0, -1)]
#print(toSort)

ar = [1, 2, 3, 4, 5]

def swap(xs, y, z):
    xs[y], xs[z] = xs[z], xs[y]
    

swap(ar, 1, 2)

print(ar)