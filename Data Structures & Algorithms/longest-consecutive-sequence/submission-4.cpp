class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        unordered_set<int> seen(nums.begin(), nums.end()); 
        int max_len = 0; 

        for (int num:seen){
            if (seen.find(num-1) != seen.end()){
                continue;
            }

            int start = num; 
            int curr_len = 1; 

            while (seen.find(start+1) != seen.end()){
                start++;
                curr_len++;
            }

            max_len = max(max_len, curr_len);
        }

        return max_len;
        
    }
};
