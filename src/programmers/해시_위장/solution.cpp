#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <string>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    unordered_map<string, vector<string>> hash_map;
    vector<string> type;

    for (int i = 0; i< clothes.size(); i++){
        hash_map[clothes[i][1]].push_back(clothes[i][0]);
        if (find(type.begin(), type.end(), clothes[i][1]) == type.end())
            type.push_back(clothes[i][1]);
    }

    for (int i = 0; i < type.size(); i++)
        answer *= (hash_map[type[i]].size()+1);

    return answer-1;
}
