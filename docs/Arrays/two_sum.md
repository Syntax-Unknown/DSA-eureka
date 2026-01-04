    # Two Sum

    **Category:** Arrays  
    **Difficulty:** Easy  
    **Time complexity:** O(n)  
    **Space complexity:** O(n)  
    **Tags:** HashMap, Two-Pointer  
    **Source:** LeetCode 1

    ## Explanation

    **Problem summary:** Brief the problem in your own words.  
    **Approach:** Describe data structures, invariants, and why it works.  
    **Edge cases:** Mention corner cases and constraints.  
    **Proof sketch:** Optional correctness argument.  
    **Complexity reasoning:** Why the stated complexities hold.

    ## Code

    ```cpp
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
    ```

    ## Tests

    ```text
    # Add sample inputs/outputs or a quick driver here
    ```
