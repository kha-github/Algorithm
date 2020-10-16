#include <string>
#include <vector>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    
    for (int i = 0; i < n; i++) {
        int temp = arr1[i] | arr2[i];
        answer.push_back("");
        for (int k = 0; k < n; k++) {
            int bin = temp % 2;
            if (bin == 1) 
                answer[i] = "#" + answer[i];
            else 
                answer[i] = " " + answer[i];
            temp /= 2;
        }
    }
    
    return answer;
}
