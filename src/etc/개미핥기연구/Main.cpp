#pragma warning(disable: 4996)

#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

void DFS(const int check[10][10], int row, int col, int n);

int input_row, input_col;
vector<int> vec;

int main() {

    char map[100] = "";
    vec.push_back(0);

    cin >> input_row >> input_col;
    for (int i = 0; i < input_row; i++) {
        char temp[10];
        cin >> temp;
        strcat(map, temp);
    }

    int check[10][10] = { 0, };

    for (int i = 0; i < input_row; i++)
        for (int k = 0; k < input_col; k++)
            if (map[i * input_col + k] == '*')
                check[i][k] = 1;

    DFS(check, 0, 0, 1);

    int max = *max_element(vec.begin(), vec.end());
    int cnt = 0;

    for (int k = 0; k < (int)vec.size(); k++)
        if (max == vec[k]) cnt++;

    cout << max << " " << cnt << endl;

    return 0;
}

void DFS(const int check[10][10], int row, int col, int n) {

    int new_check[10][10];

    if (row<0 || col<0 || row>=input_row || col>=input_col || check[row][col] == 1)
        return;

    copy(&check[0][0], &check[0][0] + 10 * 10, &new_check[0][0]);
    new_check[row][col] = 1;

    if (vec[0] <= n) {
        if (vec[0] < n)
            vec[0] = n;
        else
            vec.push_back(n);
    }

    DFS(new_check, row - 1, col, n + 1);
    DFS(new_check, row, col - 1, n + 1);
    DFS(new_check, row + 1, col, n + 1);
    DFS(new_check, row, col + 1, n + 1);
}
