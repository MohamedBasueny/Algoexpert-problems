# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array,multiplier=1):
    summ = 0
    for arr in array : 
        if type(arr) == list : 
            summ += productSum(arr,multiplier+1)
        else : 
            summ += arr
    return summ*multiplier
array = [5,2,[7,-1],3]
print(productSum(array))