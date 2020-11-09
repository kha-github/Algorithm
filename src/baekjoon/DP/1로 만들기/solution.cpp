#include <string>
#include <map>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

#define MAXIMUM 1000000
using namespace std;


int funct(int number);
int dptable[1000001];

int main() {
	int number;
	cin >> number;

	cout << funct(number);

	return 0;
}

int funct(int number) {
	if (number == 1)
		return 0;

	int& temp = dptable[number];

	if (dptable[number] != 0)
		return dptable[number];

	temp = MAXIMUM;

	if (number % 3 == 0) temp = min(temp, funct(number / 3) + 1);
	if (number % 2 == 0) temp = min(temp, funct(number / 2) + 1);
	temp = min(temp, funct(number - 1) + 1);

	return temp;

}

