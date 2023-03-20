def getNthFib(n):#O(2**n)T , O(n)S
    #base case 
    if n==0 or n==1: return 0
    elif  n==2  :    return 1
    else:            return getNthFib(n-1) + getNthFib(n-2)
         

def getNthFibIterative(n):
    if n==0 or n==1: return 0
    elif  n==2  :    return 1
    else :#n>2
        i = 2
        fibn_1 = 0
        fibn_2 = 1
        fibn = 0
        while i < n : 
            fibn = fibn_1+fibn_2
            i += 1
            fibn_1 = fibn_2
            fibn_2 = fibn
        return fibn

print(getNthFib(2))

print(getNthFibIterative(2))