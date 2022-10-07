
#include <bits/stdc++.h>
using namespace std;


bool canConstruct(string s, vector<string> s2, unordered_map<string,bool> m1){
    if(m1.find(s) != m1.end()){
        return m1[s];
    }
    if(s == ""){
        return true;
    }
    for(auto i : s2){
        if(s.find(i) == 0){
            string s3 = s.substr(i.size(),s.size());
            // m1[s3] = canConstruct(s3,s2,m1);
            if(canConstruct(s3,s2,m1) == true){
                m1[s3] = true;
                return true;
            }
        }
    }
    return false;
}



// bool canConstruct(string s, vector<string> s2){
//     if(s == ""){
//         return true;
//     }
//     for(auto i : s2){
//         if(s.find(i) == 0){
//             string s3 = s.substr(i.size(),s.size());
//             if(canConstruct(s3,s2) == true){
//                 return true;
//             }
//         }
//     }
//     return false;
// }


int main() {
    // Write C++ code here
    std::cout << "Hello world!"<<'\n';
    string s1 = "skateboard";
    vector<string> s2{"a","b","cd","ed","eif"};
    // string s3;
    unordered_map<string,bool> m;
    cout<<canConstruct(s1,s2,m);
    return 0;
}