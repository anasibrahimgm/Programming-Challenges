/*
One beautiful July morning a terrible thing happened in Mainframe: a mean virus Megabyte somehow got access to the memory of his not less mean sister Hexadecimal. He loaded there a huge amount of n different natural numbers from 1 to n to obtain total control over her energy.

But his plan failed. The reason for this was very simple: Hexadecimal didn't perceive any information, apart from numbers written in binary format. This means that if a number in a decimal representation contained characters apart from 0 and 1, it was not stored in the memory. Now Megabyte wants to know, how many numbers were loaded successfully.

Input
Input data contains the only number n (1 ≤ n ≤ 10^9).

Output
Output the only number — answer to the problem.

*/

#include <iostream>
#include <string>
#include <cmath>

using namespace std;
int numbers_count(string number_str);

int main(int argc, char const *argv[]) {
  int n;
  cin >> n;

  if (n < 10)
    cout << 1 << endl;
  else
    cout << numbers_count(to_string(n)) << endl;
}

int numbers_count(string number_str) {
  int number_str_len = number_str.length();
  if ((int(number_str[0]) - 48) > 1)
      return pow(2, number_str_len) - 1;

  int number = stoi(number_str);
  if (number <= 1)
      return number;

  // the number_str's length determines
  // len = 1,  2,  3,  4
        // 2^0 2^1 2^2 2^3 .... 2^(len -1)
        // 1   1+2 3+4 7+8 .... 2^(len-1) andd we add the other 0 for ex 100 has the length of 3 and btn 1 and 100 inclusive there are 4 such numbers
  int x = int(number) % int(pow(10, number_str_len - 1));
  return pow(2, number_str_len - 1) + numbers_count(to_string(x));
}
