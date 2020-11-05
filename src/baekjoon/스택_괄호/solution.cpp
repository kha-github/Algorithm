#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	vector<char> vec;
	int cnt;
	string str;
	cin >> cnt;
	for (int i = 0; i < cnt; i++) {
		cin >> str;
		vec.clear();
		for (int k = 0; k < str.length(); k++) {
			if ((vec.size() == 0) && (str[k] == ')')) {
				cout << "NO" << endl; break;
			}
			else if (vec.size() == 0)
				vec.push_back(str[k]);
			else if (vec.back() == '(' && str[k] == ')')
				vec.pop_back();
			else
				vec.push_back(str[k]);


			if (k == str.length() - 1) {
				if (vec.size() == 0)
					cout << "YES" << endl;
				else
					cout << "NO" << endl;
			}
		}
	}
}
