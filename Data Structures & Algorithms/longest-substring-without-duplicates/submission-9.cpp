class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        int n = s.size(); 

        unordered_set<int> seen; 

        int i = 0; 
        int j = 0; 

        int max_len = 0; 
        int cur_len = 0; 

        while (j<n){

            if (seen.count(s[j])){
                seen.erase(s[i]); 
                i++; 
            }

            else{
                seen.insert(s[j]);
                cur_len = j - i + 1; 
                max_len = max(cur_len, max_len);
                j++;
            }

    

        }

        return max_len; 
        
    }
};
