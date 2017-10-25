##########PROBLEM##############
'''
The winner of the card game popular in Berland "Berlogging" is determined according to the following rules. If at the end of the game there is only one player with the maximum number of points, he is the winner. The situation becomes more difficult if the number of such players is more than one. During each round a player gains or loses a particular number of points. In the course of the game the number of points is registered in the line "name score", where name is a player's name, and score is the number of points gained in this round, which is an integer number. If score is negative, this means that the player has lost in the round. So, if two or more players have the maximum number of points (say, it equals to m) at the end of the game, than wins the one of them who scored at least m points first. Initially each player has 0 points. It's guaranteed that at the end of the game at least one player has a positive number of points.

Input
The first line contains an integer number n (1  ≤  n  ≤  1000), n is the number of rounds played. Then follow n lines, containing the information about the rounds in "name score" format in chronological order, where name is a string of lower-case Latin letters with the length from 1 to 32, and score is an integer number between -1000 and 1000, inclusive.

Output
Print the name of the winner.
'''

############SOLUTION##############
"""first: add scores for every player and get the max number of points
    seperate the name from the score in the input string
    add the input string to inputList to process later
    check if the name exists in the dict.if it does, add the new score value to the old value and if not, add a new name with its score
    after adding the new score to the old one or adding a brand new record, check if the value is greater than the previous maximum value to check who got the maximum number of points first and she/he is the new winner and that's in case we end up with only one person having the max num of points

# second: both cases: if one winner or more than one
    check the max Value in the last stage
    compute the occurances of the maxVal in the scoreDict
    if one occurance, that means no need for looping again and the winner is winner

    if not, generate a list of possible winners, the ones who ended up having maxVal
    then create another dict , resultDict from splitting the values in the previously stored inputList
    search for the first name that has a score >= maxVal and still in the winnersList

    the winner must be someone who ended up having the max number of points not just anyone who got it once down the road
"""
inputList = []
scoreDict = {}
winner = ''
maxValue = -1001 # the score is an integer number between -1000 and 1000, inclusive.

n = int(input())

for i in range(n):
    inputStr = input()
    inputList.append(inputStr)
    name = inputStr[0: inputStr.find(" ")]
    score = int(inputStr[inputStr.find(" ")+1: ])

    if name in scoreDict:
        scoreDict[name] += score
    else:
        scoreDict[name] = score

    if ( (n == 0) or (n > 0 and scoreDict[name] > maxValue) ):
        #we store the first score as the max value and compare to it.
        #it is only > not >= bc we want the winner to be the one who got the max score first
        maxValue = scoreDict[name]
        winner = name

maxVal = max(scoreDict.values())

maxOccurances = list(scoreDict.values()).count(maxVal)#how many people have the maximum number of points
#or just the length of winnersList

if (maxOccurances == 1):
    print(winner)
elif maxOccurances > 1:
    resultDict = {}
    winnersList = []

    for name in scoreDict:
        if scoreDict[name] == maxVal:
            winnersList.append(name)

    for i in range(n):
        list = inputList[i].split()

        name, score = list[0], int(list[1])

        if name in resultDict:
            resultDict[name] += score
        else:
            resultDict[name] = score

        if (resultDict[name] >= maxVal) and (winnersList.count(name) > 0):#and the name already exists in the finalists
            winner = name
            break

    print(winner)
