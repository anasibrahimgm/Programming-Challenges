#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	char name[1000];
	cin >> name;

	char firstLetter = name[0];
	
	int x = (int)firstLetter;

	if( x >= 97 && x <= 122)//small letter a:z
	{
		name[0] -=(97-65);
	}

	cout << name << endl;

	return 0;
}

