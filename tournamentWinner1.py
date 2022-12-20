Home_Team_Won = 1
def tournamentWinner(competitions, results):
    curentBestTeam = ""
    scores = {curentBestTeam : 0}

    for idx , competiton in enumerate(competitions):
        result = results[idx]
        homeTeam ,awayTeam = competiton
        winningTeam = homeTeam if result == Home_Team_Won else awayTeam
        updateScores(winningTeam, 3 , scores)
        if scores[winningTeam] > scores[curentBestTeam] : 
            curentBestTeam = winningTeam
    return curentBestTeam

def updateScores(team,points,scores):
    if team not in scores: 
        scores[team] = 0 
    scores[team] += points


competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"] ]
  
results =  [0, 0, 1]
print(tournamentWinner(competitions, results) )