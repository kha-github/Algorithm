#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <tuple>

using namespace std;

vector<string> solution(vector<string> files) {
    vector<string> answer;
    map<int, tuple<string, string, int>> m;
    for (int i = 0; i < files.size(); i++){
        int k = 0;
        string num_temp = "";
        string head_temp = "";
        do{
            if(isdigit(files[i][k]))
                num_temp += files[i][k];
            else
                head_temp += toupper(files[i][k]);
            
            if (isdigit(files[i][k]) && !isdigit(files[i][k+1]))
                break;               
        }while ((++k)<=files[i].length());
        
        m.insert(std::make_pair(i, std::make_tuple(files[i], head_temp, stoi(num_temp))));
        
    }
    
    int i, j;
    for(i = 1; i < files.size(); i++){
        auto key = m[i];

        for(j = i-1; j >= 0 && ((get<1>(m[j]) > get<1>(key)) || (get<1>(m[j]) == get<1>(key) && get<2>(m[j]) > get<2>(key))) ; j--){
            m[j+1] = m[j];
        }
    m[j+1] = key;
    }
    
    for (int k = 0 ; k<files.size(); k++){
        answer.push_back(get<0>(m[k]));
    }
    
    return answer;
}
