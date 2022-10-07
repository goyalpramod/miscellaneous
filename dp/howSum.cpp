#include <bits/stdc++.h>
using namespace std;


// #include <chrono>
// using namespace std::chrono;
// auto start = high_resolution_clock::now();
// auto stop = high_resolution_clock::now();
// auto duration = duration_cast<microseconds>(stop - start);
// cout << duration.count() << endl;


typedef long long ll;
typedef vector<long long> vll;
typedef vector<int> vi;
typedef pair<int,int> pi;


bool howSum(int targetSum, const std::vector<int>& numbers, std::vector<int>& result)
{
    result.clear();

    if (targetSum == 0) {
        return true;
    }

    if (targetSum < 0) {
        return false;
    }

    for (int num : numbers) {
        const int remainder = targetSum - num;
        bool recursion_result = howSum(remainder, numbers, result);
        if (recursion_result) {
            result.push_back(num);
            return true;
        }
    }
    return false;
}

bool bestSum(int targetSum, vector<int>& arr, vector<int>& result,vector<int> shortestCombination){
    if(targetSum == 0) return true;

    else if (targetSum < 0) return false;

    // vector<int> shortestCombination(arr.size());

    for(auto i : arr){
        int remainder = targetSum - i;
        if(bestSum(remainder,arr,result,shortestCombination)){
            result.push_back(remainder);
            if(result.size() < shortestCombination.size()){
                shortestCombination = result;
            }
            // return true;
        }
    }
    return false;
}

// vector<int> howSum(int num,vector<int> numbers){
//     if(num == 0){
//         return {};
//     }else if(num < 0){
//         return {-1};
//     }
//     for(int i = 0;i<numbers.size();i++){
//         int remainder = num - numbers[i];
//         vector<int> vec2 = howSum(remainder,numbers);
//         if(vec2[0] != -1){
//             vec2.push_back(numbers[i]);
//             return vec2;
//         }
//     }
// }


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    // vector<int> numbers{2,3,5};
    // int num = 10;

    // vector<int> ans;

    cout<<"Hello World!";

    // ans = howSum(num,numbers);
    // for(int i = 0;i<ans.size();i++)cout<<ans<<'\n';
    
    return 0;
}