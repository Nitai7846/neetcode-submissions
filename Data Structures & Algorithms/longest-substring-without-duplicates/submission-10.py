class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        seen = set()
        max_len = 0 

        i, j = 0, 0 

        while j<n:

            if s[j] in seen:
                seen.remove(s[i])
                i+=1
            
            else:
                seen.add(s[j])
                max_len = max(max_len, j-i+1)
                j+=1 
        
        return max_len 
                
                
                






        