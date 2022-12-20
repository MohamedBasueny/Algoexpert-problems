def nonConstructibleChange(coins):
    """ # the next change we can make is cum_sum + 1
        # if we couldn't find that element 
        # then return that minum value
        #incase of the aray coins was exahusted 
        #the min change to return is the last element + 1
    """
    cum_sum = 0 
    coins.sort() #O(1)space sorts in place | O(nlogn) for sorting algoritm
    for i in coins: # o(N) for loop 
        if i > cum_sum + 1 : 
            return cum_sum +1 
        cum_sum += i           

    return cum_sum + 1 
print( nonConstructibleChange([1,2,5]) )




    # while current_sum == cum_sum or current_sum ==coins[i] : 
    #     current_sum += 1
    #     cum_sum += coins[i]
    #     i += 1
    #     # print("i = " , coins[i])
    #     print("current_sum = " , current_sum)
    #     print("cum_sum = " , cum_sum)
    #     print("*" * 5)
        
    #     if i == len(coins) :
    #         print(i,"**")
    #         return current_sum 



    # def nonConstructibleChange(coins):
#     current_sum  = 0
#     cum_sum = 0 
#     coins.sort()
#     for i in coins:
         
#         cum_sum += i

#         print("i = " , i)
#         print("current_sum = " , current_sum)
#         print("cum_sum = " , cum_sum)
#         print("*" * 5)
#         if cum_sum != current_sum   and  i != current_sum  :
#             print(current_sum != cum_sum )
#             print(current_sum != i)
#             print(current_sum != cum_sum   and  current_sum != i )
#             return current_sum +1
#         current_sum += 1
#     return 1
# print( nonConstructibleChange([1 ,5,1]) )