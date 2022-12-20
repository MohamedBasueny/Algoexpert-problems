def tournamentWinner(competitions, results):
    d = {}
    high = ['',0]
    for i in range(len(competitions)):
        if results[i] == 1 : 
            if d.get(competitions[i][0]) == None :
               d[competitions[i][0]] = 3 
            else : 
               d[competitions[i][0]] += 3
            if d[competitions[i][0]] > high[1] :
                high[0],high[1] = competitions[i][0] ,  d[competitions[i][0]] 
        else : 
            if d.get(competitions[i][1]) == None :
                d[competitions[i][1]]  = 3
            else : 
               d[competitions[i][1]] += 3     

            if d[competitions[i][1]] > high[1] :
                high[0],high[1] = competitions[i][1] ,  d[competitions[i][1]] 
    return high[0]
    # return max(d, key=d.get )

competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"] ]
  
results =  [0, 0, 1]
print(tournamentWinner(competitions, results) )