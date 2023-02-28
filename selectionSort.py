def selectionSort(array):
    a = array.copy()

    for i in range(len(array)) : 
        min_i = a[i]
        for j in range(i+1 , len(array)) : 
            if a[j] < min_i: 
                min_i , a[j] = a[j] , min_i
        a[i] = min_i
    return a 

array = [8,5,2,9,5,6,3]
print(selectionSort(array))