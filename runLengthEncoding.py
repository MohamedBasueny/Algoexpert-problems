def runLengthEncoding(string):
    prevLetter = string[0]
    letterList = []
    counter = 0
    for i , letter in enumerate(string):
        if letter == prevLetter :
            if counter==9:
                letterList.append(f"{counter}{prevLetter}") 
                counter = 0
            counter += 1 
        if letter != prevLetter :
            letterList.append(f"{counter}{prevLetter}") 
            counter = 1
        if (i == len(string)-1 and letter==prevLetter):
            letterList.append(f"{counter}{prevLetter}") 
        if (i == len(string)-1 and letter!=prevLetter):
            letterList.append(f"{counter}{letter}") 
        prevLetter = letter

    return "".join(letterList)
s = "f"
print(runLengthEncoding(s))

