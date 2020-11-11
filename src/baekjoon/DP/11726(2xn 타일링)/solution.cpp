#include <string>
#include <map>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

#define MAXIMUM 1000000
using namespace std;

int funct(int length);
int dptable[1000001];

int main() {
	int number;
	cin >> number;

	cout << funct(number)%10007;

	return 0;
}

int funct(int length) {
	
	if (length < 0) return 0;
	if (length == 0) return 1;
	if (dptable[length] > 0) return dptable[length];

	dptable[length] = funct(length - 1)%10007 + funct(length - 2)%10007;

	return dptable[length];

}
