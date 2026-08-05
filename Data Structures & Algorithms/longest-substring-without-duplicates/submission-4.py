class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        i, j = 0, 0
        maxlen = 0

        char_set = set()

        while j<n:

            if s[j] not in char_set:
                char_set.add(s[j])
                maxlen = max(maxlen, j-i+1)
                j+=1
            
            elif s[j] in char_set:
                char_set.remove(s[i])
                i +=1


        return maxlen 
        
         
        