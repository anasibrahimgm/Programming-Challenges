# problem
#
#
# In the popular spreadsheets systems (for example, in Excel) the following numeration of columns is used. The first column has number A, the second — number B, etc. till column 26 that is marked by Z. Then there are two-letter numbers: column 27 has number AA, 28 — AB, column 52 is marked by AZ. After ZZ there follow three-letter numbers, etc.
#
# The rows are marked by integer numbers starting with 1. The cell name is the concatenation of the column and the row numbers. For example, BC23 is the name for the cell that is in column 55, row 23.
#
# Sometimes another numeration system is used: RXCY, where X and Y are integer numbers, showing the column and the row numbers respectfully. For instance, R23C55 is the cell from the previous example.
#
# Your task is to write a program that reads the given sequence of cell coordinates and produce each item written according to the rules of another numeration system.
#
# Input
# The first line of the input contains integer number n (1 ≤ n ≤ 105), the number of coordinates in the test. Then there follow n lines, each of them contains coordinates. All the coordinates are correct, there are no cells with the column and/or the row numbers larger than 106 .
#
# Output
# Write n lines, each line should contain a cell coordinates in the other numeration system.
#

import re
import math

n = int(input())
inputList = []
outputList = []

#print(ord('A'))#65
#print(chr(98))#b

for i in range(n):#n iputs
    inputList.append(input())

    #CASE ONE:
    #if it has two letters and the second char is a number
    #that is an RXCY type

    #RC245 is not our case
    #R23C4 is
    #R234C765 is
    str1 = inputList[i]

    if (len(re.findall('[A-Z]', str1)) == 2) and (re.findall('\d', str1[1])):#two capital letters && the nd char is a number
        firstNum = str1[1: str1.find("C")]#extract the X number in RXCY
        secondNum = int(str1[str1.find("C") + 1:])#extract the Y number in RXCY

        resultStr1 = ''

        while secondNum > 0:
            remaining = (secondNum % 26)

            if remaining == 0:#Z as in R228C494
                remaining = 26

            secondNum = ((secondNum - remaining) / 26)

            resultStr1 = chr(int(remaining + ord('A') - 1)) + resultStr1#add the letter to the beginning of the string

        resultStr1 += firstNum#add the X number to the end of the string

        outputList.append(resultStr1)

    #CASE TWO
    else:
        str2 = inputList[i]
        searchList = re.findall('[A-Z]', str2)#the letters
        sum = 0

        for k in range(len(searchList)):#loop through the letters
            m = len(searchList) - k -1 #n - index - 1
            sum += (ord(searchList[k]) - 64) * (math.pow(26, m)) #char * 26^(n-1-index) where n is the total number of letter ( len(searchList) )

        resultStr2 = "R" + ( ''.join(re.findall('\d', str2)) ) + "C" # R + the numbers in the string + C
        resultStr2 += str(int(sum)) # the string value of the sum

        outputList.append(resultStr2)

for i in outputList:
    print(i)
