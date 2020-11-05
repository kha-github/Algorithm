#include <string>
#include <map>
#include <iostream>
#include <algorithm>
#include <vector>
#include<queue>

using namespace std;
void DFS(int node);
void BFS(int node);

int line[1001][1001] = { 0, };
int visit[1001];
int n, m, first_node;

int main() {
	cin >> n >> m >> first_node;

	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		line[a][b] = 1;
		line[b][a] = 1;
	}

	DFS(first_node);
	cout << endl;

	for (int i = 0; i <= n; i++) 
		visit[i] = 0;

	BFS(first_node);
	cout << endl;

	return 0;
	

}

void DFS(int node) {
	cout << node << " ";
	visit[node] = 1;
	for (int i = 1; i <= n; i++) {
		if (line[node][i] == 1 && visit[i] != 1) {
			DFS(i);
		}
	}
}

void BFS(int node) {
	queue<int> q;
	q.push(node);
	visit[node] = 1;
	while (true) {
		int curnode;
		curnode = q.front();
		cout << curnode << " ";
		for (int i = 1; i <= n; i++) {
			if (line[curnode][i] == 1 && visit[i] != 1) {
				q.push(i);
				visit[i] = 1;
			}
		}
		q.pop();
		if (q.empty() == true)
			break;
	}
	
}
