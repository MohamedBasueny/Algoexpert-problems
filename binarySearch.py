def binarySearch(array, target):
    return binarySearchHelper(array,target,start=0,end=len(array)-1)
def binarySearchHelper(array,target,start,end):
    mid = (start+end) // 2
    if start>end: return -1 
    if array[mid] > target:
        end=mid-1
        return binarySearchHelper(array,target,start,end)
    elif array[mid] < target:
        start=mid+1
        return binarySearchHelper(array,target,start,end)
    elif array[mid] == target : 
        return mid


array= [0,1,21,33,45,45,61,71,72,73]
print(binarySearch(array,target=3))