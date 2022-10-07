#include <bits/stdc++.h>
using namespace std;




bool bestSum(int targetSum, vector<int>& arr, vector<int>& result,vector<int>& shortestCombination){
    // result.clear();
    
    if(targetSum == 0) return true;

    if (targetSum < 0) return false;

    // vector<int> shortestCombination(arr.size());

    for(int i : arr){
        int remainder = targetSum - i;
        bool recursion_result = bestSum(remainder,arr,result,shortestCombination);
        // if(result.size() < shortestCombination.size() || shortestCombination.empty()){
        //         shortestCombination = result;
        //         // return true;
        // }
        if(recursion_result){
            result.push_back(i);
            if(result.size() <= shortestCombination.size() || shortestCombination.empty()){
            //     shortestCombination = result;
            // shortestCombination.assign(result.begin(),result.end());
                // copy(result.begin(),result.end(),back_inserter(shortestCombination));
            //     // return true;
            // shortestCombination.clear();
            for(int j : result){
                shortestCombination.push_back(j);
            }
            }
            // return true;
        }
        // if(result.size() < shortestCombination.size() || shortestCombination.empty()){
        //         shortestCombination = result;
        //         // return true;
        // }
    }
    return false;
}


bool howSum(int targetSum, const std::vector<int>& numbers, std::vector<int>& result)
{
    // result.clear();

    if (targetSum == 0) {
        return true;
    }

    if (targetSum < 0) {
        return false;
    }

    for (int num : numbers) {
        int remainder = targetSum - num;
        bool recursion_result = howSum(remainder, numbers, result);
        if (recursion_result) {
            result.push_back(num);
            return true;
        }
    }
    // return false;
}



int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    vector<int> numbers{2,3,5};
    int num = 10;

    vector<int> ans;
	vector<int> tempAns;
    
    // howSum(num,numbers,tempAns);
	bestSum(num,numbers,tempAns,ans);
    for(int i = 0;i<ans.size();i++){
        cout<<ans[i]<<" ";
    }
    cout<<'\n';
    for(int i = 0;i<tempAns.size();i++){
        cout<<tempAns[i]<<" ";
    }
    cout<<'\n';
    cout<<"Hello World!";
    return 0;
}