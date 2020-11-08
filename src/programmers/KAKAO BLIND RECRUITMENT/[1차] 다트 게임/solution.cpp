#include <string>
#include <math.h>
#include <vector>

using namespace std;

int solution(string dartResult) {
    int answer = 0;
    vector <int> temp = { 0,0,0 };
    int index = 0;

    for (int i = 0; i < 3; i++, index += 2) {
        if (dartResult[index + 1] > 'A') 
            temp[i] = dartResult[index] - 48;
        else {
            temp[i] = 10; 
            index++;
        }
        temp[i] = pow(temp[i], (dartResult[index + 1] == 'S' ? 1 : (dartResult[index + 1] == 'D' ? 2 : 3)));

        if (dartResult[index + 2] != '*' && dartResult[index + 2] != '#')
            continue;
        if (dartResult[index + 2] == '*') {
            if (i == 0) 
                temp[0] *= 2;
            else { 
                temp[i-1] *= 2; 
                temp[i] *= 2; 
            }
        }
        if (dartResult[index + 2] == '#') 
            temp[i] *= -1;

        index++;
    }
    answer = temp[0] + temp[1] + temp[2];

    return answer;
}
