"""
Tom is interested in power consumption of his favourite laptop. His laptop has three modes. In normal mode laptop consumes P1 watt per minute. T1 minutes after Tom moved the mouse or touched the keyboard for the last time, a screensaver starts and power consumption changes to P2 watt per minute. Finally, after T2 minutes from the start of the screensaver, laptop switches to the "sleep" mode and consumes P3 watt per minute. If Tom moves the mouse or touches the keyboard when the laptop is in the second or in the third mode, it switches to the first (normal) mode. Tom's work with the laptop can be divided into n time periods [l1, r1], [l2, r2], ..., [ln, rn]. During each interval Tom continuously moves the mouse and presses buttons on the keyboard. Between the periods Tom stays away from the laptop. Find out the total amount of power consumed by the laptop during the period [l1, rn].

Input
The first line contains 6 integer numbers n, P1, P2, P3, T1, T2 (1 ≤ n ≤ 100, 0 ≤ P1, P2, P3 ≤ 100, 1 ≤ T1, T2 ≤ 60). The following n lines contain description of Tom's work. Each i-th of these lines contains two space-separated integers li and ri (0 ≤ li < ri ≤ 1440, ri < li + 1 for i < n), which stand for the start and the end of the i-th period of work.

Output
Output the answer to the problem.
"""

n, P1, P2, P3, T1, T2 = list(map(int, input().split()))

e = 0 # e for energy
time_periods = []

for i in range(n):
    li, ri = list(map(int, input().split()))
    time_periods += [li, ri]
    e += (ri - li) * P1

# take out both first and last element
# time_periods.pop(0)
# time_periods.pop(-1)

for j in range(1, (2*n - 1), 2):
    y = time_periods[j + 1] - time_periods[j]
    if y > T1:
        e += T1 * P1
        if (y - T1) > T2:
            e+= T2 * P2 + (y - T1 - T2) * P3
        else:
            e += (y - T1) * P2
    else:
        e += y * P1

print(e)
