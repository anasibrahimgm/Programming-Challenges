### Problem:
"""
Snark and Philip are preparing the problemset for the upcoming pre-qualification round for semi-quarter-finals. They have a bank of n problems, and they want to select any non-empty subset of it as a problemset.
k experienced teams are participating in the contest. Some of these teams already know some of the problems. To make the contest interesting for them, each of the teams should know at most half of the selected problems.
Determine if Snark and Philip can make an interesting problemset!

#Input
The first line contains two integers n, k (1 ≤ n ≤ 105, 1 ≤ k ≤ 4) — the number of problems and the number of experienced teams.
Each of the next n lines contains k integers, each equal to 0 or 1. The j-th number in the i-th line is 1 if j-th team knows i-th problem and 0 otherwise.

#Output
Print "YES" (quotes for clarity), if it is possible to make an interesting problemset, and "NO" otherwise.
You can print each character either upper- or lowercase ("YeS" and "yes" are valid when the answer is "YES").
"""

### SOLUTION:
"""
    every row has (2^k) possibilities from 0 - (2^k - 1)

    to have at least 2 problems in the problemset:
        - if an input row is all zeros, i.e. there is a problem that nobody knows
        - an input row containing 1's and there is a previous input row in which for every 1 in the input row, there is a zero in the adjacent position. i.e. for every known problem there is a problem that this group doesn't know
            -- Fast solution: if we have a row x and the complement of x, for ex: 101 and 010

    SOLUTION STEPS:
        1- get n, k
        2- create twoPkList: a list of 2^k - 2 rows, (the tow missing rows are the ones containing all 0's and all 1's and there is no need to check against them),
           a (k+1) columns and initialize the values = 0 i.e. FALSE, the (k+1) column is to check if a specific row is already inputted (1:TRUE) or not yes (0:FALSE)
        -- for every row in n input rows:
           3- convert the input elements to binary
              -- if it is a 1:
                    -- add its position in the input string to the onesList
                    -- convert it to its decimal value and add it to the summation
           4- #FAST CASE# if the input is all 0's, make result = YES and break
           5- #FAST CASE# if the input is all 1's, no need to do more check, continue
           6- #FAST CASE# if the complement of summation already exists in the list by i.e. if twoPkList[2**k -2 - summation][k] is set
           7- for each row in twoPkList:
              8- create adjacentZeros to count the number of 0's in the row that are adjacent to the 1's in the input
              9- #FAST CASE# check if the row is already set and it is not the same row as the input:
                 10- for every position containing 1 in the input: check if the same position in the row has a 1:
                    11- if it has, increase adjacentZeros by 1,
              12- if the total number of adjacentZeros == length of the 1's positions list (onesList) i.e. for every 1 in the iput there is an adjacent  zero in the row, set the result = "YES"
                  then a problemset can be created
           13- if the result is set to "YES", break
           14- if the twoPkList[summation - 1][k] is not set
               15- add the binary list of the input to twoPkList[summation - 1]
               16- set the twoPkList[summation - 1][k]

"""
n, k = input().split()
n = int(n)  # no. of problems
k = int(k)  # no. of teams

inputList = [] # input
twoPkList = [] # array to save status for each 2 pow k values
kList = [] # array to save status for each k values in every (2 pow k) row
result = 'NO'
list1 = []
list0 = []

for j in range(k):
    list1.append('1')
    list0.append('0')
    kList.append(0)

onesStr = ' '.join(list1)
zerosStr = ' '.join(list0)
kList.append(0)# initialize elements = FALSE + another column to check the whole number
# case k = 3 :
    # 0 0 1 (1)
    # 0 1 0 (2)
    # 0 1 1 (3)
    # 1 0 0 (4)
    # ........

#for every value btn. parentheses we put a boolean value indicating whether it's already found (TRUE) or not (FALSE)

for i in range(2**k - 2): # all cases except when all 0's and all 1's
    twoPkList.append(list(kList))#initialize elements = FALSE

for i in range(n):
    inputString = input()

    if (inputString == zerosStr): # input is all 0's
        result = "YES"
        break

    if (inputString == onesStr): # all ones, no need to check
        continue

    inputList = inputString.split()# split the input string
    onesList = [] # to save the positions of 1's in the input string

    summation = 0 #initialize summation
    for j in range(k):
        #convert to binary
        inputList[j] = int(inputList[j])# a list of ones and zeros

        if (inputList[j]):# if it is a 1
            onesList.append(j)# keep the position of that 1
            summation += inputList[j] * (2**(k-1-j))

    if (twoPkList[2**k - 2 - summation][k]): # if the complement exists
        result = "YES"
        break

    for index, row in enumerate(twoPkList):# for every row in twoPkList
        adjacentZeros = 0

        if ( row[k] and (not( index == (summation - 1) )) ):# if the row is already set and it isn't the same element #### to not pointlessly check a row
            for position in onesList:# for every position of 1
                if (row[position] == 0):# if the position of a 1 in the input has an adjacent 0
                    adjacentZeros += 1 # increase number of adjacent zeros by 1

        if (adjacentZeros == len(onesList)):# if number of zeros in the row == number of ones in the input in the same positions
            # we can form an interesting problemset
            result = "YES"
            break

    if (result == "YES"):
        break

    if (not twoPkList[summation - 1][k]):#if it is not set
        twoPkList[summation - 1] = list(inputList)
        twoPkList[summation - 1].append(1)

print(result)
