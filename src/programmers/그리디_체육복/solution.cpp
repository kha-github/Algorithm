#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int cnt = n - lost.size() + reserve.size();
    
    vector<int>::iterator iter;
    for (int i = 0; i<lost.size(); i++){
        if ((iter = find(reserve.begin(),reserve.end(),lost[i]))!=reserve.end()){
            reserve.erase(iter); lost.erase(lost.begin()+i); i--;}
    }
    
    for (int i = 0; i<lost.size(); i++){
        if ((iter = find(reserve.begin(),reserve.end(),lost[i]+1))!=reserve.end())
            reserve.erase(iter);
        else if ((iter = find(reserve.begin(),reserve.end(),lost[i]-1))!=reserve.end())
            reserve.erase(iter);
    }
    
    return cnt - reserve.size();
}
