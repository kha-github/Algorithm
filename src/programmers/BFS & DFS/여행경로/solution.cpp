#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;
void DFS(vector<vector<int>> check, vector<string> city, int node);
vector<string> answer;
vector<string> airport;
int ticket_size;

vector<string> solution(vector<vector<string>> tickets) {
    
    ticket_size = tickets.size();

    for (int i = 0; i<tickets.size(); i++){
        airport.push_back(tickets[i][0]);
        airport.push_back(tickets[i][1]);
    }
    
    sort(airport.begin(), airport.end());
    
    airport.erase(unique(airport.begin(),airport.end()),airport.end());
    
    vector<vector<int>> visit(airport.size(), vector<int>(airport.size(), 0));
    
    for (int i = 0; i<tickets.size(); i++){
        int source = find(airport.begin(), airport.end(), tickets[i][0]) - airport.begin();
        int dest = find(airport.begin(), airport.end(), tickets[i][1]) - airport.begin();
        
        visit[source][dest]++;
        
    }
    
    vector<string> city;
    
    DFS(visit, city, find(airport.begin(), airport.end(), "ICN") - airport.begin());
    
    return answer;
}

void DFS(vector<vector<int>> check, vector<string> city, int node) {
    
    vector<string> dummy;
    dummy.assign(city.begin(), city.end());
    dummy.push_back(airport[node]);
    
    int remain = 0;
    for (int i = 0; i < airport.size(); i++)
        for (int k = 0; k < airport.size(); k++)
            remain += check[i][k];
    
    if (remain == 0 && answer.size() == 0){
        answer.assign(dummy.begin(), dummy.end());
        return;
    }
    
    vector<vector<int>> new_check;
    
	for (int i = 0; i < airport.size(); i++) {
        
		if (check[node][i] >= 1) {
            new_check.assign(check.begin(), check.end());
            new_check[node][i]--;
			DFS(new_check, dummy, i);
		}
	}
}
