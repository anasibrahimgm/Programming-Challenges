#include <iostream>

using namespace std;

int main(int argc, char const* argv[])
{
  int x, y;
  cin >> x >> y;

  int max = x >= y ? x : y;

  switch(max) {
    case 1:
      cout << "1/1";
      break;

    case 2:
      cout << "5/6";
      break;

    case 3:
      cout << "2/3";
      break;

    case 4:
      cout << "1/2";
      break;

    case 5:
      cout << "1/3";
      break;

    case 6:
      cout << "1/6";
      break;
  }

  cout << endl;
}

/*

x = list(map(int, input().split()))
# She wins if she gets a number equal to or higher than the highest number they've got

# create probs dict depending on max
probs = {6: '1/6', 5: '1/3', 4: '1/2', 3: '2/3', 2: '5/6', 1: '1/1'}

print(probs[max(x)])

*/
