def bubbleSort(array):
    is_swaped = True 
    while is_swaped : 
        is_swaped = False
        for i in range(len(array) - 1):
            if array[i+1] < array[i]: 
                array[i],array[i+1] = array[i+1], array[i]
                is_swaped = True
    return array
array = [8, 5, 2, 9, 5, 6, 3]
print(bubbleSort(array))           