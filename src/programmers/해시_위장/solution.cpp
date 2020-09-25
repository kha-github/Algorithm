#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    unordered_map<string, vector<string>> hash_map;
    
    for (int i = 0; i< clothes.size(); i++)
        hash_map[clothes[i][1]].push_back(clothes[i][0]);
    
    for (auto iter = hash_map.begin(); iter != hash_map.end(); iter++)
        answer *= (iter->second.size()+1);
    
    return answer-1;
}
