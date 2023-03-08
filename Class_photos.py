def classPhotos(redShirtHeights, blueShirtHeights):
    #choose the red and blue teams   #O(nlogn)
    max_1 = max(redShirtHeights) 
    max_2 = max(blueShirtHeights)
    if max_1 == max_2 : return False 

    elif max_1 > max_2 : 
        taller = redShirtHeights
        shorter = blueShirtHeights

    else : 
        taller = blueShirtHeights
        shorter = redShirtHeights
    #by sorting we make sure that evey pair can be coupled together    
    taller.sort()
    shorter.sort()
    for i,j in zip(taller,shorter) :  #O(nlogn) + o(n)
        if i <= j : return False 

    return True 

   

red = [5,8,1,3,4]
blue = [6,9,2,4,5]
print(classPhotos(red,blue))