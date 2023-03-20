def findThreeLargestNumbers(array):
    infinty = float('-inf')
    arr = [infinty,infinty,infinty]
    for i in array:
        if i > arr[-1] : 
            arr[-3] = arr[-2]           
            arr[-2] = arr[-1]
            arr[-1] = i 
        elif i > arr[-2] : 
            arr[-3] = arr[-2] 
            arr[-2] = i
        elif i > arr[-3] :
            arr[-3] = i
        # print(arr)
    return arr
        

array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
array2 =  [10,5,9,10,12]
print(findThreeLargestNumbers(array2))
         