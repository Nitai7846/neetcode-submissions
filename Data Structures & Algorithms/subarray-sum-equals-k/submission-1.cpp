class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {

        int n = nums.size(); 

        unordered_map<int, int> mpp; 
        mpp[0] = 1;
        int res = 0; 
        int running = 0; 

        for (int i=0; i<n; i++){
            running = running + nums[i]; 
            if (mpp.find(running-k) != mpp.end()){
                res = res + mpp[running-k]; 
            }
            mpp[running]++; 

        }

        return res; 

        
    }
};