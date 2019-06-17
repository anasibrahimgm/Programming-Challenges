/*
Tom is interested in power consumption of his favourite laptop. His laptop has three modes. In normal mode laptop consumes P1 watt per minute. T1 minutes after Tom moved the mouse or touched the keyboard for the last time, a screensaver starts and power consumption changes to P2 watt per minute. Finally, after T2 minutes from the start of the screensaver, laptop switches to the "sleep" mode and consumes P3 watt per minute. If Tom moves the mouse or touches the keyboard when the laptop is in the second or in the third mode, it switches to the first (normal) mode. Tom's work with the laptop can be divided into n time periods [l1, r1], [l2, r2], ..., [ln, rn]. During each interval Tom continuously moves the mouse and presses buttons on the keyboard. Between the periods Tom stays away from the laptop. Find out the total amount of power consumed by the laptop during the period [l1, rn].

Input
The first line contains 6 integer numbers n, P1, P2, P3, T1, T2 (1 ≤ n ≤ 100, 0 ≤ P1, P2, P3 ≤ 100, 1 ≤ T1, T2 ≤ 60). The following n lines contain description of Tom's work. Each i-th of these lines contains two space-separated integers li and ri (0 ≤ li < ri ≤ 1440, ri < li + 1 for i < n), which stand for the start and the end of the i-th period of work.

Output
Output the answer to the problem.
*/


#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  int n, p1, p2, p3, t1, t2;
  cin >> n >> p1 >> p2 >> p3 >> t1 >> t2;

  p2 -= p1;
  p3 -= p1 + p2;

  int e = 0; // e for energy
  int time_periods[2*n];

  cin >> time_periods[0] >> time_periods[1];

  int li, ri, y;
  for (int i = 0; i < n-1; i++) {
    cin >> li >> ri;
    y = li - time_periods[2*i + 1];
    if (y > t1) {
      e += (y - t1) * p2;
      if ((y - t1) > t2)
          e+= (y - t1 - t2) * p3;
    }

    time_periods[2*i + 2] = li;
    time_periods[2*i + 3] = ri;
  }

  e += (time_periods[2*n - 1] - time_periods[0]) * p1;

  cout << e << endl;
}
