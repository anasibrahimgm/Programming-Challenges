"""
One beautiful July morning a terrible thing happened in Mainframe: a mean virus Megabyte somehow got access to the memory of his not less mean sister Hexadecimal. He loaded there a huge amount of n different natural numbers from 1 to n to obtain total control over her energy.

But his plan failed. The reason for this was very simple: Hexadecimal didn't perceive any information, apart from numbers written in binary format. This means that if a number in a decimal representation contained characters apart from 0 and 1, it was not stored in the memory. Now Megabyte wants to know, how many numbers were loaded successfully.

Input
Input data contains the only number n (1 ≤ n ≤ 10^9).

Output
Output the only number — answer to the problem.

"""
def numbers_count(number_str):
    if int(number_str[0]) > 1:
        return pow(2, len(number_str)) - 1

    number = int(number_str)
    if number <= 1:
        return number

    # the number_str's length determines
    # len = 1,  2,  3,  4
          # 2^0 2^1 2^2 2^3 .... 2^(len -1)
          # 1   1+2 3+4 7+8 .... 2^(len-1) andd we add the other 0 for ex 100 has the length of 3 and btn 1 and 100 inclusive there are 4 such numbers
    return pow(2, len(number_str) - 1) + numbers_count('{}'.format(int(number_str[1:])))

n = input()

if int(n) < 10:
    print(1)
else:
    print(numbers_count(n))
