# Have you ever tried to explain to the coordinator, why it is eight hours to the contest and not a single problem has been prepared yet? Misha had. And this time he has a really strong excuse: he faced a space-time paradox! Space and time replaced each other.
#
# The entire universe turned into an enormous clock face with three hands — hour, minute, and second. Time froze, and clocks now show the time h hours, m minutes, s seconds.
#
# Last time Misha talked with the coordinator at t1 o'clock, so now he stands on the number t1 on the clock face. The contest should be ready by t2 o'clock. In the terms of paradox it means that Misha has to go to number t2 somehow. Note that he doesn't have to move forward only: in these circumstances time has no direction.
#
# Clock hands are very long, and Misha cannot get round them. He also cannot step over as it leads to the collapse of space-time. That is, if hour clock points 12 and Misha stands at 11 then he cannot move to 1 along the top arc. He has to follow all the way round the clock center (of course, if there are no other hands on his way).
#
# Given the hands' positions, t1, and t2, find if Misha can prepare the contest on time (or should we say on space?). That is, find if he can move from t1 to t2 by the clock face.
#
# Input
# Five integers h, m, s, t1, t2 (1 ≤ h ≤ 12, 0 ≤ m, s ≤ 59, 1 ≤ t1, t2 ≤ 12, t1 ≠ t2).
#
# Misha's position and the target time do not coincide with the position of any hand.
#
# Output
# Print "YES" (quotes for clarity), if Misha can prepare the contest on time, and "NO" otherwise.
#
# You can print each character either upper- or lowercase ("YeS" and "yes" are valid when the answer is "YES").

h, m, s, t1, t2 = input().split()
h = int(h)
m = int(m)
s = int(s)
t1 = int(t1)
t2 = int(t2)

mins = m + (s / 60)
hrs = h + (mins / 60)

tmin = min(t1, t2)
tmax = max(t1, t2)

if ( (tmax > hrs and hrs > tmin) and (tmax*5 > mins and mins > tmin*5) and (tmax*5 > s and s > tmin*5) ) or ( not(tmax > hrs and hrs > tmin) and not(tmax*5 > mins and mins > tmin*5) and not(tmax*5 > s and s > tmin*5) ):
    #all three clockhands are between tmax and tmin
    print('YES')
else:
    print('NO')
