#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(int n, long long left, long long right) {
    vector<int> answer;
    long long num = left / n;
    for(long long i = num; i <= n; i++){
        for(long long j = 1; j <= n; j++){
            if((i-1) * n + j -1>= left ){
                if((i-1)*n + j-1 <= right){
                    if(i==1) answer.push_back(j);
                    else{
                        if(j > i) answer.push_back(j);
                        else answer.push_back(i);
                    }
                }
                else break;
            }
        }
    }
    
    return answer;
}
