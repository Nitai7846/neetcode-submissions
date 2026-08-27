class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        seen = set()
        max_len = 0 
        cur_len = 0 

        i = 0 
        j = 0 

        while j<n:

            if s[j] in seen:
                seen.remove(s[i])
                i+=1 
            
            elif s[j] not in seen:
                seen.add(s[j])
                cur_len = j-i+1
                max_len = max(max_len, cur_len)
                j+=1

        return max_len
           




        