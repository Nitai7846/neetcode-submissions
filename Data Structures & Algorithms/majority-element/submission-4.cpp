class Solution {
public:
    int majorityElement(vector<int>& nums) {

        int res = 0;
        int count = 0;

        int n = nums.size();

        for (int i=0; i<n; i++){
            if (count == 0){
                res = nums[i];
            }

            if (nums[i] == res){
                count+=1;
            }
            else{
                count-=1;
            }
        }

        return res; 
        
    }
};