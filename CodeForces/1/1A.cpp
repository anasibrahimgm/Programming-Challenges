//problem
/*
Theatre Square in the capital city of Berland has a rectangular shape with the size n × m meters. On the occasion of the city's anniversary, a decision was taken to pave the Square with square granite flagstones. Each flagstone is of the size a × a.

What is the least number of flagstones needed to pave the Square? It's allowed to cover the surface larger than the Theatre Square, but the Square has to be covered. It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the Square.
*/

//idea
/*
cover the Square with k*l flagstones of size a^2 such that ka >= n && la >= m
*/

#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char const *argv[])
{	

	double n, m, a;

	cin >> n >> m >> a;

	if (!(n >= 1 && m >= 1 && a >=1 && a <= 10^9))
	{
		cout << "Wrong Input!" << endl;
		return 0;
	}

	//number of flagstones = ceil(n/a) * ceil(m/a)
	long long int num = ceil(n/a) * ceil(m/a);

	cout << num <<endl;

	return 0;
}