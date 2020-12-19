#include <string>
#include <vector>
#include <iostream>

using namespace std;

int factorial(int num);

int main(){

    int number;

    cin >> number;

    cout << factorial(number);

}
int factorial(int num) {
    int value = 1;

    for (int i = num; i > 0; i--) {
        value *= i;
    }

    return value;
}
