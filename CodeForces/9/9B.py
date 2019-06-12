"""
And again a misfortune fell on Poor Student. He is being late for an exam.

Having rushed to a bus stop that is in point (0, 0), he got on a minibus and they drove along a straight line, parallel to axis OX, in the direction of increasing x.

Poor Student knows the following:

during one run the minibus makes n stops, the i-th stop is in point (xi, 0)
coordinates of all the stops are different
the minibus drives at a constant speed, equal to vb
it can be assumed the passengers get on and off the minibus at a bus stop momentarily
Student can get off the minibus only at a bus stop
Student will have to get off the minibus at a terminal stop, if he does not get off earlier
the University, where the exam will be held, is in point (xu, yu)
Student can run from a bus stop to the University at a constant speed vs as long as needed
a distance between two points can be calculated according to the following formula:
Student is already on the minibus, so, he cannot get off at the first bus stop
Poor Student wants to get to the University as soon as possible. Help him to choose the bus stop, where he should get off. If such bus stops are multiple, choose the bus stop closest to the University.

Input
The first line contains three integer numbers: 2 ≤ n ≤ 100, 1 ≤ vb, vs ≤ 1000. The second line contains n non-negative integers in ascending order: coordinates xi of the bus stop with index i. It is guaranteed that x1 equals to zero, and xn ≤ 105. The third line contains the coordinates of the University, integers xu and yu, not exceeding 105 in absolute value.

Output
In the only line output the answer to the problem — index of the optimum bus stop.
"""
from math import *

def get_input_list_ints():
    return list(map(int, input().split()))

def cart_dist(value):
    return sqrt(pow(school_coordinates[0] - value, 2) + pow(school_coordinates[1], 2))

n, vb, vs = get_input_list_ints()
bus_stops = get_input_list_ints()
school_coordinates = get_input_list_ints()

bus_stops_no = len(bus_stops)

min_time = (bus_stops[1]/vb) + (cart_dist(bus_stops[1])/vs)
min_index = 1

if bus_stops_no > 2:
    time = []
    for index, value in enumerate(bus_stops[2:]):
        new_time = (value/vb) + (cart_dist(value)/vs)
        time.append(new_time)
        if new_time <= min_time: # <= bc if there are two stations with the same time, we talk the later so he doesn't run/walk when he could easily ride the bus
            min_time = new_time
            min_index = index + 2 # plus me starting the search from the 2nd stop as he can't get off in the first one

    print(min_index + 1) # the + 1 due to the indices starting with 0
else:
    print(bus_stops_no)
