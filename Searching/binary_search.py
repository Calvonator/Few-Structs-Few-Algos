toSearch = []

for x in range(50):
    toSearch.append(x)


def binary_search(target, array):
    left, right = 0, len(array) - 1
    target = int(target)
    while left <= right:
        half = (left + right) // 2

        if target == array[half]:
            return half

        elif target < array[half]:
            right = half - 1
            print("Less than")
        elif target > array[half]:
            left = half + 1
            print("Greater than")


            
targ = input("Please input a target: ")  

target_index = binary_search(targ, toSearch)

print(target_index)