//problem

/*
In the popular spreadsheets systems (for example, in Excel) the following numeration of columns is used. The first column has number A, the second — number B, etc. till column 26 that is marked by Z. Then there are two-letter numbers: column 27 has number AA, 28 — AB, column 52 is marked by AZ. After ZZ there follow three-letter numbers, etc.

The rows are marked by integer numbers starting with 1. The cell name is the concatenation of the column and the row numbers. For example, BC23 is the name for the cell that is in column 55, row 23.

Sometimes another numeration system is used: RXCY, where X and Y are integer numbers, showing the column and the row numbers respectfully. For instance, R23C55 is the cell from the previous example.

Your task is to write a program that reads the given sequence of cell coordinates and produce each item written according to the rules of another numeration system.

Input
The first line of the input contains integer number n (1 ≤ n ≤ 105), the number of coordinates in the test. Then there follow n lines, each of them contains coordinates. All the coordinates are correct, there are no cells with the column and/or the row numbers larger than 106 .

Output
Write n lines, each line should contain a cell coordinates in the other numeration system.
*/
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>

using namespace std;

int numberCharToInt(char a);
char intToNumberChar(int b);

int main(int argc, char const *argv[])
{
	int n;
	cin >> n;

	string inputList[n];
	string outputList[n];

	for (int i = 0; i < n; i++)
	{
		cin >> inputList[i];
		//For the RXCY type
		/*
		the string is at least 4 digits RXCY
		AND
		the first char is an 'R'
		AND
		the second char is a number
		AND
		the string has a 'C'

		if (len >= 4 && inputList[i][0] == 'R' && inputList[i][1] >= 48 && inputList[i][1] <= 57){//48 is ascii for the number 0 and 57 is ascii for the number 9
		*/

		//ANOTHER IDEA
		/*
		Starting from index 2 , If it has a 'C' and the digit before 'C' is a a number, then it is RXCY type
		*/

		int strLen = inputList[i].size();

		int cIndex = 0, firstIntIndex = 0;

		for (int j = 1; j < strLen; j++)//no need to check the first one
		{
			if (inputList[i][j] == 'C' && inputList[i][j-1] >= 48 && inputList[i][j-1] <= 57 )
			{
				cIndex = j;
			}

			if (!firstIntIndex)//if firstIntIndex is not discovered yet
				if (inputList[i][j] >= 48 && inputList[i][j] <= 57)//check if it is a number
					firstIntIndex = j;
		}

		if (cIndex) {//RXCY type
			int Ysum = 0;

			////Extracting the Y number value in the string RXCY
			for (int k = strLen - 1; k > cIndex; k--)
				Ysum += pow(10, strLen-1-k) * numberCharToInt(inputList[i][k]);//mutiply the number according to its decimal place
			////

			int remaining;
			string resultStr1 = "";

			while (Ysum > 0) {
				remaining = Ysum % 26;

				if (remaining == 0)//Z as in R228C494
					remaining = 26;

				Ysum = ((Ysum - remaining) / 26);

				resultStr1 = char(remaining + 64) + resultStr1;//add the letter to the beginning of the string
			}

			////adding the X number in RXCY to the string which is between R and C i.e. btn from index 1 to (cIndex - 1)
			for (int l = 1; l < cIndex; l++)
			{
				resultStr1 += inputList[i][l];
			}
			////

			outputList[i] = resultStr1;
		}

		else{
			//convert the letters from the beginning of the string to firstIntIndex - 1
			int sum = 0;
			for (int m = 0; m < firstIntIndex; m++)//loop through the letters
			{
				// the letters in in a hypothetical array of length = firstIntIndex starting from index 0 to firstIntIndex-1
				sum += (inputList[i][m] - 64) * pow(26, (firstIntIndex - 1 - m));
			}

			// R + the numbers in the string + C + sum
			string resultStr2 = "R";

			for (int m = firstIntIndex; m < inputList[i].size(); m++)
			{
				resultStr2 += inputList[i][m];
			}

			resultStr2 += "C";

			string resultStr2_1 = "";
			int rem;

			//convert the sum into a string
			while (sum > 0) {
				rem = sum % 10;
				sum = ((sum - rem) / 10);

				resultStr2_1 = intToNumberChar(rem) + resultStr2_1;//add the letter to the beginning of the string
			}

			resultStr2 += resultStr2_1;

			outputList[i] = resultStr2;
		}

	}

	for (int i = 0; i < n; i++) {//print out the result
		cout << outputList[i] << endl;
	}
	return 0;
}

int numberCharToInt(char a) {//converts the number chars '0', '1', ... to their respective integers 0, 1, ...
	return int(a) - 48;
}

char intToNumberChar(int b) {
	return char(b + 48);
}
