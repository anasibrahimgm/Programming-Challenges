#include <iostream>

using namespace std;

int main(int argc, char const* argv[])
{
  int x, y;
  cin >> x >> y;

  int max = x >= y ? x : y;

  const char *probs[6] = {"1/1", "5/6", "2/3", "1/2", "1/3", "1/6"};

  cout << probs[max - 1] << endl;
}

/*

x = list(map(int, input().split()))
# She wins if she gets a number equal to or higher than the highest number they've got

# create probs dict depending on max
probs = {6: '1/6', 5: '1/3', 4: '1/2', 3: '2/3', 2: '5/6', 1: '1/1'}

print(probs[max(x)])

*/
