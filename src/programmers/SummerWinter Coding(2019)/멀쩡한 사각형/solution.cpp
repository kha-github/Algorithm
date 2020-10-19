#include<iostream>
#include<math.h>

using namespace std;

long long solution(int w,int h) {
    
    if (w < h){
        int temp = h; h = w; w = temp;
    }
    
    long long answer = 0;
    double a;
    long long before_y = 0;
    
    a = (double)h/(double)w;
    
    for (int i = 1; i<=w; i++){
        double y = a*(double)i;
        answer += (long long)(ceil(y)) - before_y;
        before_y = (long long)(floor(y)); 
    }
    
    return (long long)w*h - answer;
}
