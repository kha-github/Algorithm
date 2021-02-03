#include <string.h>
#include <map>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

#define MAXIMUM 1000000
using namespace std;

int funct(int number);
int dptable[12];

int main() {
	vector<int> vec;

	int count;
	int number;
	cin >> count;
	
	for (int i = 0; i < count; i++) {
		cin >> number;
		vec.push_back(number);
	}

	for (int i = 0; i < count; i++) {
		cout << funct(vec[i]) << endl;
		memset(dptable, 0, 12);
	}

	return 0;
}


int funct(int number) {
	
	if (number < 0) return 0;
	if (number == 0) return 1;
	if (dptable[number] > 0) return dptable[number];

	dptable[number] = funct(number - 1) + funct(number - 2) + funct(number - 3);

	return dptable[number];

}
