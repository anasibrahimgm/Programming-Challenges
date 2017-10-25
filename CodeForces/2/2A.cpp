////////////////////PROBLEM////////////////////////////
/* The winner of the card game popular in Berland "Berlogging" is determined according to the following rules. If at the end of the game there is only one player with the maximum number of points, he is the winner. The situation becomes more difficult if the number of such players is more than one. During each round a player gains or loses a particular number of points. In the course of the game the number of points is registered in the line "name score", where name is a player's name, and score is the number of points gained in this round, which is an integer number. If score is negative, this means that the player has lost in the round. So, if two or more players have the maximum number of points (say, it equals to m) at the end of the game, than wins the one of them who scored at least m points first. Initially each player has 0 points. It's guaranteed that at the end of the game at least one player has a positive number of points.

 Input
 The first line contains an integer number n (1  ≤  n  ≤  1000), n is the number of rounds played. Then follow n lines, containing the information about the rounds in "name score" format in chronological order, where name is a string of lower-case Latin letters with the length from 1 to 32, and score is an integer number between -1000 and 1000, inclusive.

 Output
 Print the name of the winner.
*/

////////////////////////SOLUTION////////////////////////////
/*
first: add scores for every player and get the max number of points
    seperate the name from the score in the input string
    add the input string to inputList to process later
    check if the name exists in the dict.if it does, add the new score value to the old value and if not, add a new name with its score
    after adding the new score to the old one or adding a brand new record, check if the value is greater than the previous maximum value to check who got the maximum number of points first and she/he is the new winner and that's in case we end up with only one person having the max num of points

second: both cases: if one winner or more than one
    check the max Value in the last stage
    compute the occurances of the maxVal in the scoreDict
    if one occurance, that means no need for looping again and the winner is winner

    if not, generate a list of possible winners, the ones who ended up having maxVal
    then create another dict , resultDict from splitting the values in the previously stored inputList
    search for the first name that has a score >= maxVal and still in the winnersList

    the winner must be someone who ended up having the max number of points not just anyone who got it once down the road
*/

#include <iostream>
#include <string>

using namespace std;

int indexOf(string array[],string str, int size) {
  for (int i = 0; i < size; i++) {
    if (array[i] == str)
      return i;
  }

  return -1;// not found
}

int maximum(int array[], int size) {
  int maxVal = array[0];

  for (int j = 1; j < size; j++) {
    if (array[j] > maxVal) {
      maxVal = array[j];
    }
  }

  return maxVal;
}

int main(int argc, char const *argv[]) {
  int n;
  cin >> n;

  string inputListNames[n];
  int inputListScores[n];

  string scoreListNames[n];
  int scoreListScores[n];

  string winner;
  int maxValue, winnerIndex;

  string name;
  int score;
  int scoreListSize = 1, index;

  for (int i = 0; i < n; i++) {
    cin >> name >> score;
    inputListNames[i] = name;
    inputListScores[i] = score;

    if (i == 0) {
      maxValue = score;
      winner = name;
      winnerIndex = 0;
      scoreListNames[0] = name;
      scoreListScores[0] = score;
    }
    else if (i > 0){
      index = indexOf(scoreListNames, name, scoreListSize);

      if (index != -1) {//existing name
        scoreListScores[index] += score;

        if (scoreListScores[index] > maxValue) {
          maxValue = scoreListScores[index];
          winner = name;
          winnerIndex = index;
        }
      }
      else {//new name
        scoreListNames[scoreListSize] = name;
        scoreListScores[scoreListSize] = score;

        if (score > maxValue) {
          maxValue = score;
          winner = name;
          winnerIndex = scoreListSize;
        }

        scoreListSize++;
      }
    }
  }

  int max, maxVal;

  maxVal = maximum(scoreListScores, scoreListSize);

  int maxOccurances = 0;
  string maxOccurancesArray[scoreListSize];

  for (int j = 0; j < scoreListSize; j++) {
    if (scoreListScores[j] == maxVal) {
      maxOccurancesArray[maxOccurances] = scoreListNames[j];
      maxOccurances++;
    }
  }

  if (maxOccurances > 1) {// more than one possible winner
    string resultListNames[maxOccurances];
    int resultListScores[maxOccurances];
    int resultListNames_Size = 0, first= 0;

    for (int i = 0; i < n; i++) {
      if (indexOf(maxOccurancesArray, inputListNames[i],maxOccurances) != -1) {// First check if the inputListNames[i] is a possible winner

        if (first == 0) {// first element
          resultListNames[0] = inputListNames[i];
          resultListScores[0] = inputListScores[i];

          if (resultListScores[0] >= maxVal)
          {
            winner = resultListNames[0];
            break;
          }
          resultListNames_Size++;
        }
        else {
          index = indexOf(resultListNames, inputListNames[i], resultListNames_Size);

          if (index != -1) {// found
            resultListScores[index] += inputListScores[i];

            if (resultListScores[index] >= maxVal) {
              winner = resultListNames[index];
              break;
            }
          }
          else {// not found
            resultListNames[resultListNames_Size] = inputListNames[i];
            resultListScores[resultListNames_Size] = inputListScores[i];

            if (resultListScores[resultListNames_Size] >= maxVal) {
              winner = resultListNames[resultListNames_Size];
              break;
            }
            resultListNames_Size++;
          }
        }

        first++;
      }
    }
  }
  cout << winner << endl;
  return 0;
}
