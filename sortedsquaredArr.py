
# def sortedSquaredArray(array):
#     sortedArr = [] 
#     prev = 0
#     for i in range(len(array)): #O(N)
#         sortedArr.append(array[i]**2)
#         print(sortedArr)
#         if sortedArr[i]**2 <  sortedArr[prev]**2: 
#             sortedArr[i] ,sortedArr[prev] = sortedArr[prev] , sortedArr[i]
#             print(prev)

#     return sortedArr



def sortedSquaredArray(array):
    sortedArr = [] 
    left = 0
    right = len(array) - 1
    while right >= left :  #O(N) S,T
        if abs(array[left]) > abs(array[right]) : 
            sortedArr.append(array[left]**2)
            left  += 1
        else: 
            sortedArr.append(array[right]**2)
            right -= 1

    return sortedArr[::-1] #Extra traversing operation -> use a fixed array inintialized with zeros
# print(sortedSquaredArray([-5, -4, -3, -2, -1]))

for i in reversed(range(10)): print(i)