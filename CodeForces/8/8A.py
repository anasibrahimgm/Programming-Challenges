"""
Peter likes to travel by train. He likes it so much that on the train he falls asleep.

Once in summer Peter was going by train from city A to city B, and as usual, was sleeping. Then he woke up, started to look through the window and noticed that every railway station has a flag of a particular colour.

The boy started to memorize the order of the flags' colours that he had seen. But soon he fell asleep again. Unfortunately, he didn't sleep long, he woke up and went on memorizing the colours. Then he fell asleep again, and that time he slept till the end of the journey.

At the station he told his parents about what he was doing, and wrote two sequences of the colours that he had seen before and after his sleep, respectively.

Peter's parents know that their son likes to fantasize. They give you the list of the flags' colours at the stations that the train passes sequentially on the way from A to B, and ask you to find out if Peter could see those sequences on the way from A to B, or from B to A. Remember, please, that Peter had two periods of wakefulness.

Peter's parents put lowercase Latin letters for colours. The same letter stands for the same colour, different letters — for different colours.

Input
The input data contains three lines. The first line contains a non-empty string, whose length does not exceed 105, the string consists of lowercase Latin letters — the flags' colours at the stations on the way from A to B. On the way from B to A the train passes the same stations, but in reverse order.

The second line contains the sequence, written by Peter during the first period of wakefulness. The third line contains the sequence, written during the second period of wakefulness. Both sequences are non-empty, consist of lowercase Latin letters, and the length of each does not exceed 100 letters. Each of the sequences is written in chronological order.

Output
Output one of the four words without inverted commas:

«forward» — if Peter could see such sequences only on the way from A to B;
«backward» — if Peter could see such sequences on the way from B to A;
«both» — if Peter could see such sequences both on the way from A to B, and on the way from B to A;
«fantasy» — if Peter could not see such sequences.
"""


x = input()
x_reversed = ''.join(list(reversed(x)))

seq1 = input()
seq2 = input()

if len(seq1) + len(seq2) > len(x): # if sum of peter's colors exceed the whole number of colors
	print('fantasy')
else:
	forward = False
	backward = False

	x_find_seq1 = x.find(seq1)
	if x_find_seq1 > -1:
		x_find_seq2 = x[x_find_seq1 + len(seq1):].find(seq2) # start searching after seq1 ends in the colors string
		if x_find_seq2 > -1:
			x_find_seq2 += x_find_seq1 + len(seq1) # add the margin
	else:
		x_find_seq2 = -1

	x_reversed_find_seq1 = x_reversed.find(seq1)
	if x_reversed_find_seq1 > -1:
		x_reversed_find_seq2 = x_reversed[x_reversed_find_seq1 + len(seq1):].find(seq2)
		if x_reversed_find_seq2 > -1:
			x_reversed_find_seq2 += x_reversed_find_seq1 + len(seq1)
	else:
		x_reversed_find_seq2 = -1

	if (x_find_seq1 != -1 and x_find_seq1 != -1):
		if x_find_seq1 <= x_find_seq2:
			forward = True

	if (x_reversed_find_seq1 != -1 and x_reversed_find_seq1 != -1):
		if x_reversed_find_seq1 <= x_reversed_find_seq2:
			backward = True

	if forward and backward:
		print('both')
	elif forward:
		print("forward")
	elif backward:
		print("backward")
	else:
		print('fantasy')