############# problem #################

#Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.

#Note, that during capitalization all the letters except the first one remains unchanged.

#Input
#A single line contains a non-empty word. This word consists of lowercase and uppercase English letters. The length of the word will not exceed 103.

#Output
#Output the given word after capitalization.

############# solution #################
#capitalize the 1st char & add it to a new string along with te remaining cars in te input string

str1 = input()
str2 = ''

if (len(str1) <= 1000):
	str2 += str1[0].upper()
	str2 += str1[1:]

	print(str2)
