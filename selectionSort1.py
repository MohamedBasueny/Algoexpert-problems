def selectionSort(array):
    for i in range(len(array)):
        smallest = i
        for j in range(i+1,len(array)):
            if array[j] < array[smallest] : 
                smallest  = j
        array[i] , array[smallest] = array[smallest] , array[i]
    return array

array = [8,5,2,9,5,6,3]
print(selectionSort(array))