"""
Tom is interested in power consumption of his favourite laptop. His laptop has three modes. In normal mode laptop consumes P1 watt per minute. T1 minutes after Tom moved the mouse or touched the keyboard for the last time, a screensaver starts and power consumption changes to P2 watt per minute. Finally, after T2 minutes from the start of the screensaver, laptop switches to the "sleep" mode and consumes P3 watt per minute. If Tom moves the mouse or touches the keyboard when the laptop is in the second or in the third mode, it switches to the first (normal) mode. Tom's work with the laptop can be divided into n time periods [l1, r1], [l2, r2], ..., [ln, rn]. During each interval Tom continuously moves the mouse and presses buttons on the keyboard. Between the periods Tom stays away from the laptop. Find out the total amount of power consumed by the laptop during the period [l1, rn].

Input
The first line contains 6 integer numbers n, P1, P2, P3, T1, T2 (1 ≤ n ≤ 100, 0 ≤ P1, P2, P3 ≤ 100, 1 ≤ T1, T2 ≤ 60). The following n lines contain description of Tom's work. Each i-th of these lines contains two space-separated integers li and ri (0 ≤ li < ri ≤ 1440, ri < li + 1 for i < n), which stand for the start and the end of the i-th period of work.

Output
Output the answer to the problem.
"""

n, P1, P2, P3, T1, T2 = list(map(int, input().split()))
P2 -= P1
P3 -= P1 + P2

e = 0 # e for energy
time_periods = []

time_periods += list(map(int, input().split()))

for i in range(n - 1):
    li, ri = list(map(int, input().split()))
    y = li - time_periods[2*i + 1]
    if y > T1:
        e += (y - T1) * P2
        if (y - T1) > T2:
            e+= (y - T1 - T2) * P3

    time_periods += [li, ri]

e += (time_periods[-1] - time_periods[0]) * P1
print(e)
