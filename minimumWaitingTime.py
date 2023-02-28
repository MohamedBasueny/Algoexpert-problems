def minimumWaitingTime(queries):
    # a single query has to wait 0 time to execute
    if len(queries) == 1 : 
        return 0
    queries.sort()
    total_duration = 0
    print(queries)
    for i,v  in enumerate(queries):
        queriesLeft = len(queries) - (i+1) # i starts at zero 
        total_duration  +=  v * queriesLeft
    return total_duration

def minimumWaitingTime1(queries):
    if len(queries) == 1 : 
        return 0
    queries.sort()
    runningSum = prevTimes = 0 #two pointers 
    print(queries)
    for time in queries : 
        runningSum += prevTimes 
        prevTimes += time 
        print(f"time = {time} , prevTimes = {prevTimes} , runningSum = {runningSum}")
    return runningSum

queries =  [3, 2, 1, 2, 6]
print(minimumWaitingTime1(queries))