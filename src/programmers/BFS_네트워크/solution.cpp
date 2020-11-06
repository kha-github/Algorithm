#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;
vector<int> visit;
int cnt;
void BFS(int node, vector<vector<int>> line);

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    int node = 0;
    cnt = computers.size();
    for (int i = 0; i<cnt; i++)
        visit.push_back(0);
    while(true){
        BFS(node, computers);
        answer++;
        for (int i = 0; i<cnt; i++){
            if(visit[i] == 0){
                node = i;
                break;
            }
            if(i == cnt-1)
                return answer;
        }
    }

}

void BFS(int node, vector<vector<int>> line) {
	queue<int> q;
	q.push(node);
	visit[node] = 1;
	while (true) {
		int curnode;
		curnode = q.front();
		for (int i = 0; i < cnt; i++) {
			if (line[curnode][i] == 1 && visit[i] != 1 && curnode != i) {
				q.push(i);
				visit[i] = 1;
			}
		}
		q.pop();
		if (q.empty() == true)
			break;
	}
	
}
