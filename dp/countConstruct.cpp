#include <bits/stdc++.h>
using namespace std;

int canConstruct(string s, vector<string> s2, unordered_map<string,int> m1){
    if(m1.find(s) != m1.end()){
        return m1[s];
    }
    if(s == ""){
        return 1;
    }
    
    int totalWays = 0;
    
    for(auto i : s2){
        if(s.find(i) == 0){
            string s3 = s.substr(i.size(),s.size());
            // m1[s3] = canConstruct(s3,s2,m1);
            totalWays += 1;
            // if(canConstruct(s3,s2,m1) == 1){
            //     m1[s3] = 1;
            //     return 1;
            // }
        }
    }
    m1[s] = totalWays;
    return totalWays;
}


int main() {
    // Write C++ code here
    std::cout << "Hello world!"<<'\n';
    string s1 = "skateboard";
    vector<string> s2{"a","b","cd","ed","eif","skateboard","skate","board"};
    // string s3;
    unordered_map<string,int> m;
    cout<<canConstruct(s1,s2,m);
    return 0;
}