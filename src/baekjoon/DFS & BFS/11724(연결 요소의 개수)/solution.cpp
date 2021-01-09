#include <string>
#include <map>
#include <iostream>
#include <algorithm>
#include <vector>
#include<queue>

#define INFINITY 10000

using namespace std;
vector<int> visit;
void BFS(int node, vector<vector<int>> line);
int n, m;
int cnt;


int main() {
	cin >> n >> m;

	vector<vector<int>> line(n, vector<int>(n, 0));

	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		line[a - 1][b - 1] = 1;
		line[b - 1][a - 1] = 1;
	}

	for (int i = 0; i < n; i++) {
		visit.push_back(0);
	}

	for (int j = 0; j < visit.size(); j++) {

		if (visit[j] == 0) {
			BFS(j+1, line);
		}
	}

	cout << cnt;

}

void BFS(int node, vector<vector<int>> line) {
	queue<int> q;
	q.push(node);
	visit[node-1] = 1;
	while (true) {
		int curnode;
		curnode = q.front();
		for (int i = 0; i < n; i++) {
			if (visit[i] != 1 && line[curnode-1][i] == 1) {
				q.push(i+1);
				visit[i] = 1;
			}
		}
		q.pop();
		if (q.empty() == true) {
			cnt++;
			break;			
		}
	}	
}
