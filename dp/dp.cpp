#include <bits/stdc++.h>
using namespace std;
// Remeber pass the memo by reference 
vector<int> howSum(int num,vector<int> vec,unordered_map<int,vector<int> >& m1){
    if(num == 0){
        // this is true case
    }else if(num < 0){
        // this is false case
    }
    for(auto i : vec){
        int new_num = num - i;
        
    }
    
}

int fibo(int n, vector<int>& m1){
        if(m1[n] != 0){
            return m1[n];
        }
        if(n == 1){
            return 1;
        }
        else if(n == 0){
            return 0;
        }
        
        m1[n] = fibo(n-1, m1) + fibo(n-2,m1);
        return m1[n];
    }
    

// dis gibs wrong output fix it.
// int targetSum(int num, vector<int> &arr,unordered_map<int, int>& m1){
//     // static int remainder;
//     if(m1.find(num) != m1.end()){
//         return m1[num];
//     }
//     if(num == 0) return 1;
//     if(num < 0) return 0;
//     for(auto i : arr){
//         int remainder = num - i;
//         // m1[remainder] = targetSum(remainder, arr, m1);
//         if(targetSum(remainder, arr, m1) == 1){
//             m1[num] = 1;
//             return 1;
//         }
//     }
//     m1[num] = 0;
//     return 0;
// }


// int gridTraveler(int m,int n, unordered_map<string, int> &arr){
//     string s = to_string(m) + "," + to_string(n);
    
//     if(arr[s] == 1){
//         return arr[s];
//     }
//     arr[s] = 1;
//     // arr[make_pair(n,m)] = 1;
    
//     if(m <= 0 || n <= 0){
//         return 0;
//     }
//     // ans += 1;
//     if(m == 1 && n == 1){
//         return 1;
//     }
    
//     arr[s] = gridTraveler(m-1,n,arr) + gridTraveler(m,n-1,arr);
//     return arr[s];
// }

int main(){
    // int a = 5, b = 7
    // unordered_map<string,int> a;
    // string s = to_string(a) + "," + to_string(b);
    cout<<"Hello World"<<endl;
    // int something = gridTraveler(18,18,a); 
    // cout<<s<<endl;
    // cout<<something;
    // vector<int> a;
    // unordered_map<int,int> m1;
    // a.push_back(5);
    // a.push_back(3);
    // a.push_back(2);
    // int b = 11;
    // // for(auto i : a)cout<<i<<endl;
    // cout<<targetSum(b,a,m1);
    
    
    return 0;
}