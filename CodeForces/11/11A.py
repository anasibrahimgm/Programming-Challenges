"""
A sequence a0, a1, ..., at - 1 is called increasing if ai - 1 < ai for each i: 0 < i < t.

You are given a sequence b0, b1, ..., bn - 1 and a positive integer d. In each move you may choose one element of the given sequence and add d to it. What is the least number of moves required to make the given sequence increasing?

Input
The first line of the input contains two integer numbers n and d (2 ≤ n ≤ 2000, 1 ≤ d ≤ 106). The second line contains space separated sequence b0, b1, ..., bn - 1 (1 ≤ bi ≤ 106).

Output
Output the minimal number of moves needed to make the sequence increasing.
"""

from math import *

n, d = list(map(int, input().split()))
b = list(map(int, input().split()))

no_moves = 0

for index, elm in enumerate(b[1:]):
    diff = b[index] - elm
    if diff >= 0:
        if diff == 0:
            moves = 1

        else:
            moves = floor(diff/d) + 1 # in case both are equal!

        no_moves += moves
        b[index+1] += moves*d

print(no_moves)
