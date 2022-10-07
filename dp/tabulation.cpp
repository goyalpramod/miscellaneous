#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<long long> vll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int fibo(int n){
    vector<int> arr(n+1,0);
    arr[0] = 0;
    arr[1] = 1;
    for(int i =2;i<=n;i++){
        arr[i] = arr[i-1] + arr[i-2];
    }
    return arr[n];
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n = 50;
    vector<long long> arr(n+1,0);
    arr[0] = 0;
    arr[1] = 1;
    for(int i =2;i<=n;i++){
        arr[i] = arr[i-1] + arr[i-2];
    }
    cout<<arr[n]<<endl;
    cout<<"Hello World!"<<endl;

    // cout<<fibo(n)<<' ';

    return 0;
}