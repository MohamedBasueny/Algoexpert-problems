

def isValidSubsequence(array, sequence):
    arrIndex  = 0
    seqIndex = 0
    while True :
        if arrIndex == len(array) and seqIndex == len(sequence) : return True

        if arrIndex > len(array) - 1 : 
            print(arrIndex)
            return False
        if seqIndex > len(sequence) - 1 : 
            print(seqIndex)
            return True
        if sequence[seqIndex] != array[arrIndex]:
            arrIndex += 1 
        elif sequence[seqIndex] == array[arrIndex]:
            seqIndex += 1
            arrIndex += 1

        print(seqIndex,arrIndex)
        
print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10]) )


# print(isValidSubsequence(  [5,1,22,25,6,-1,8,10],[1, 6, -1, -1, 10] ))



















# def isValidSubsequence(array, sequence):
#     arrayDict = {v : [k,False] for k ,v in enumerate(array)}
#     # sequenceDict = {v : k for k ,v in enumerate(sequence)}
#     prev = [0,0]
#     for i in sequence: 
#         print(i , arrayDict.get(i))
#         if arrayDict[i][1] == True : return False 
#         if arrayDict.get(i) == None: return False
             
#         if arrayDict.get(i)[0] < prev[0]: return False
#         prev = arrayDict[i]
#         arrayDict[i][1] = True
#         print(arrayDict[i])
#         print("****")
#     return True

#     # print( arrayDict ,"\n" ,sequenceDict)
