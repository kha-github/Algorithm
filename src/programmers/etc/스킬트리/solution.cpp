#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;
    
    int size = skill_trees.size();
    
    for (int i = 0; i < size ; i++){
        string copy_skill = skill;
        answer++;
        
        int len = skill_trees[i].length();
        
        for (int k = 0; k < len; k++){
             if (copy_skill.find(skill_trees[i][0]) != std::string::npos) {

                cout << skill_trees[i][0] << copy_skill[0] << endl;
                if (skill_trees[i][0] == copy_skill[0]) {
                    skill_trees[i].erase(0,1);
                    copy_skill.erase(0, 1);                 
                }
                else {
                    answer--;
                    cout << answer << endl;
                    break;
                }
            }
            else{
                skill_trees[i].erase(0,1);
            }
        }
    }
    return answer;
}
