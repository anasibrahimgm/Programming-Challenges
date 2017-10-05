#
# As technologies develop, manufacturers are making the process of unlocking a phone as user-friendly as possible. To unlock its new phone, Arkady's pet dog Mu-mu has to bark the password once. The phone represents a password as a string of two lowercase English letters.
#
# Mu-mu's enemy Kashtanka wants to unlock Mu-mu's phone to steal some sensible information, but it can only bark n distinct words, each of which can be represented as a string of two lowercase English letters. Kashtanka wants to bark several words (not necessarily distinct) one after another to pronounce a string containing the password as a substring. Tell if it's possible to unlock the phone in this way, or not.
#
# Input
# The first line contains two lowercase English letters — the password on the phone.
#
# The second line contains single integer n (1 ≤ n ≤ 100) — the number of words Kashtanka knows.
#
# The next n lines contain two lowercase English letters each, representing the words Kashtanka knows. The words are guaranteed to be distinct.
#
# Output
# Print "YES" if Kashtanka can bark several words in a line forming a string containing the password, and "NO" otherwise.
#
# You can print each letter in arbitrary case (upper or lower).
#
#
# //SOLUTION
#
# to have the password, there should be the first char of the passowrd at the end of a string and the second char of password at the beginning
#

password = input()

n = int(input())

firstLetter = 0
secondLetter = 0
found = 0

for i in range(n):
    inputStr = input()

    if inputStr == password:
        found = 1

    if inputStr[1] == password[0]:
        firstLetter = 1

    if inputStr[0] == password[1]:
        secondLetter = 1


if ( found or (firstLetter and secondLetter) ):
    print('YES')
else:
    print('NO')
