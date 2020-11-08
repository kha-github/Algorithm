#include <string>
#include <queue>
#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int solution(vector<int> numbers, int target) {
    int answer = 0;
    queue<int> q;
    q.push(0);
    
    for (int i = 0; i < pow(2,numbers.size())-1; i++){
        q.push(q.front() + numbers[(int)(log(i+1)/log(2))]);
        q.push(q.front() - numbers[(int)(log(i+1)/log(2))]);
        q.pop();
    }
    
    int index = q.size();
    
    for (int i = 0; i < index; i++){
        if (q.front()==target) answer++;
        q.pop();
    }
    
    return answer;
}
