//EOF 입출력 처리
#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	while (true) {
		int a, b;
		cin >> a >> b;
		if (cin.eof() == true) {
			exit(0);
		}
		cout << a + b << endl;
	}

}
