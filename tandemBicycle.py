def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest): # complexity ; O(NlogN) + O(N) sorting and traversing the array
    # Write your code here.                                  # space : O(1) sorting in place 
    if fastest: 
        redShirtSpeeds.sort(reverse=True)
        blueShirtSpeeds.sort(reverse=False)
        return calc_accum(redShirtSpeeds,blueShirtSpeeds)
    else : 
        redShirtSpeeds.sort(reverse=True)
        blueShirtSpeeds.sort(reverse=True)
        return calc_accum(redShirtSpeeds,blueShirtSpeeds)
   
def calc_accum(red,blue):
    total_speed = 0
    for i in range(len(red) ) : 
        red_i = red[i]
        blue_i = blue[i] 
        max_i = red_i if red_i > blue_i else blue_i
        total_speed += max_i
    return total_speed

red = [5,5,3,9,2]
blue = [3,6,7,2,1]
print(tandemBicycle(red, blue, True))