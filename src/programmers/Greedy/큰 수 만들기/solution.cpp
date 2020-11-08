#include <string>
#include <vector>
#include <stdlib.h>
using namespace std;

string solution(string number, int k) {
    for (int i = 0; i < k; i++){
        
        for (int k = 0; k < number.size() -1; k++){
            
            if (number[k] < number[k+1]){
                number.erase(k, 1); 
                break;
            }
            if (k == number.size() -2 && number[k] >= number[k+1])
                number.erase(k+1, 1);
            
        }
    }
    return number;
}
