#Merge two sorted arrays array1(L1, ..., R1), array2(L2, ..., R2) into array3(L3, ..., R3) keeping array3 sorted

def mergeArrays(array1, array2, array3):

    i = 0   #Array1 Index Counter
    j = 0   #Array2 Index Counter
    k = 0   #Array3 Index Counter

    while i < len(array1) and j < len(array2):    #while there is still items in both array1 and array 2. If one is empty, then rest of the other array can be copied over
        if array1[i] <= array2[j]:
            array3.insert(k, array1[i])
            i += 1
            k += 1
        elif array1[i] >= array2[j]:
            array3.insert(k, array2[j])
            j += 1
            k += 1

    if i <= len(array1) - 1:
        array3.append(array1[i:])

    elif j <= len(array2) - 1:
        array3.append(array2[j:])

    print(array3)



array1 = []
array2 = []
array3 = []

array1 = input("Enter values for the first array seperated with commas").split(',')
array2 = input("Enter values for the second array seperated with commas").split(',')

for value in array1:
    array1[array2.index(value)] = int(value)#Sort this shit out

for value in array2:
    array2[array2.index(value)] = int(value)

array1.sort()
array2.sort() #Sort this shit out

mergeArrays(array1, array2, array3)



