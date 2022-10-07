#include <bits/stdc++.h>
using namespace std;

bool canConstruct(string s,vector<string> &vec1){
    vector<bool> vec2(s.size()+1, false);
    vec2[0] = true;
    for(int i = 0;i<= s.size();i++){
        if(vec2[i] == true){
        for(int j = 0;j<vec1.size();j++){
            if(s.substr(i,vec1[j].size()) == vec1[j]){
                if(i + vec1[j].size() <= s.size()){
                    vec2[i + vec1[j].size()] = true;
                }
            }
        }
        }
    }
    return vec2[s.size()];
}

int main() {



    std::cout << "Hello world!"<<endl;
    string s = "abcdef";
    vector<string> vec{"ab","ca","ef"};
    cout<<canConstruct(s,vec);
    // cout<<vec[1][1];
    // for(auto i : vec2)cout<<i<<endl;
    // cout<<vec2[n]<<endl;
    return 0;
}