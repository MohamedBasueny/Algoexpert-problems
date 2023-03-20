def isPalindrome(string):#O(N)T & O(1)S
    if len(string) == 1: return True
    left = 0 
    right = len(string) - 1 
    while string[left] == string[right] and left<= right :
        left += 1
        right -= 1
    if left > right : return True 
    return False 
print(isPalindrome("a"))