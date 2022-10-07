#include <bits/stdc++.h>
using namespace std;



int main() {
    // Write C++ code here
    int n = 3;
    vector<vector<int>> vec( n+1 , vector<int> (n+1,0));
    vec[1][1] = 1;
    for(int i =0;i<n;i++){
        for(int j =0;j<n;j++){
            vec[i][j+1] += vec[i][j];
            vec[i+1][j] += vec[i][j];
        }
    }
    for(int i = 0;i<n;i++){
        vec[i+1][n] += vec[i][n];
        vec[n][i+1] += vec[n][i];
    }
    std::cout << "Hello world!"<<endl;;
    cout<<vec[n][n]<<endl;
    return 0;
}