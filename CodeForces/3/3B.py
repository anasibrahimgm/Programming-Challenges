""""
A group of tourists is going to kayak and catamaran tour. A rented lorry has arrived to the boat depot to take kayaks and catamarans to the point of departure. It's known that all kayaks are of the same size (and each of them occupies the space of 1 cubic metre), and all catamarans are of the same size, but two times bigger than kayaks (and occupy the space of 2 cubic metres).

Each waterborne vehicle has a particular carrying capacity, and it should be noted that waterborne vehicles that look the same can have different carrying capacities. Knowing the truck body volume and the list of waterborne vehicles in the boat depot (for each one its type and carrying capacity are known), find out such set of vehicles that can be taken in the lorry, and that has the maximum total carrying capacity. The truck body volume of the lorry can be used effectively, that is to say you can always put into the lorry a waterborne vehicle that occupies the space not exceeding the free space left in the truck body.

Input
The first line contains a pair of integer numbers n and v (1 ≤ n ≤ 105; 1 ≤ v ≤ 109), where n is the number of waterborne vehicles in the boat depot, and v is the truck body volume of the lorry in cubic metres. The following n lines contain the information about the waterborne vehicles, that is a pair of numbers ti, pi (1 ≤ ti ≤ 2; 1 ≤ pi ≤ 104), where ti is the vehicle type (1 – a kayak, 2 – a catamaran), and pi is its carrying capacity. The waterborne vehicles are enumerated in order of their appearance in the input file.

Output
In the first line print the maximum possible carrying capacity of the set. In the second line print a string consisting of the numbers of the vehicles that make the optimal set. If the answer is not unique, print any of them.
"""
types = {1: {'name': 'kayak', 'volume': 1}, 2: {'name': 'catamaran', 'volume': 2}}

x, vol = list(map(int, input().split()))

dict1 = {}

list2 = []
inputLine = []
no_ones = 0

for i in range(x):
    inputLine = list(map(int, input().split()))
    list2.append(inputLine[1] * (1.5 - 0.5 * inputLine[0]))# a * (2 - x) + 0.5 * a * (x - 1) = a * (1.5 - 0.5 * x)
    dict1[i + 1] = inputLine

    no_ones = no_ones + (1 if inputLine[0] == 1 else 0)

resultsList = []
capacity = 0

# check if vol > 0
if vol <= 0:
    print(0)
else:
    while vol:
        index_of_max = list2.index(max(list2))
        maximum = dict1[index_of_max + 1]

        if list2[index_of_max]:
            if (maximum[0] <= vol):# list2[index_of_max] != 0
                if not ((maximum[0] == 1) and not (vol % 2) and (no_ones == 1)):# not (vol % 2) is true: vol is an even value
                    vol = vol - maximum[0]
                    capacity = capacity + maximum[1]
                    resultsList.append(index_of_max + 1)

                    no_ones = no_ones - (1 if maximum[0] == 1 else 0)

            list2[index_of_max] = 0
        else:
            break

print(capacity)
for value in resultsList:
    print(value, end = ' ')
