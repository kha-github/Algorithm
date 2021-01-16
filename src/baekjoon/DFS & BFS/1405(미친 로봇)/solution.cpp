#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

void DFS(const int check[29][29], int row, int col, double temp, int n);

int n, input_east, input_west, input_south, input_north;
double east, west, south, north;
double percent = 0.0;

int main() {

    cin >> n >> input_east >> input_west >> input_south >> input_north;

    east = input_east / 100.0;
    west = input_west / 100.0;
    south = input_south / 100.0;
    north = input_north / 100.0;
  
    int check[29][29] = { 0, };

    DFS(check, 14, 14, 1.0, n);
    cout.precision(10);
    cout << 1 - percent << endl;
}

void DFS(const int check[29][29], int row, int col, double temp, int n) {

    int new_check[29][29];

    if (temp == 0) return;
    if (n < 0) return;
    if (check[row][col] == 1) {
        percent += temp;
        return;
    }

    copy(&check[0][0], &check[0][0] + 29 * 29, &new_check[0][0]);
    new_check[row][col] = 1;

    DFS(new_check, row - 1, col, north * temp, n-1);
    DFS(new_check, row, col-1, west * temp, n-1);
    DFS(new_check, row + 1 , col, south * temp, n-1);
    DFS(new_check, row, col + 1, east * temp, n-1);
    
}
