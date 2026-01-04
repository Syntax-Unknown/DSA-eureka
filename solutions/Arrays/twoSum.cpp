// Title: Two Sum 
// Category: Arrays 
// Difficulty: Easy 
// Time Complexity: O(n) 
// Space Complexity: O(n) 
// Tags: HashMap, Two-Pointer 
// Source: LeetCode 1

#include<iostream>
#include<vector>
using namespace std;
class Solution
{
    public:
    vector<int> twoSum(vector<int>&nums, int target)
    {
        int i,j;
        bool found=false;
        vector<int> result;
        for (i=0;i<nums.size(); i++)
        {
            for(j=i+1; j<nums.size();j++)
            {
                if(nums[i] + nums[j]==target)
                {
                    found=true;
                    result.push_back(nums[i]);
                    result.push_back(nums[j]);
                    break;
                }
            }
            if(found)
                break;
        }
        return result;
    }
};
int main()
{
    vector<int>nums={2,7,11,4,6};
    int target;
    cin>>target;
    Solution obj;
    vector<int> ans = obj.twoSum(nums,target);
    for(int i=0; i<ans.size();i++)
        cout << ans[i] << " ";
    return 0;
}