class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        i,j,maxLen = 0, 0, 0

        hashLen = 256
        hash = [-1]*hashLen 

        while j<n:

            if hash[ord(s[j])] != -1:
                i = max(hash[ord(s[j])] + 1, i)
        
            currLen = j - i + 1
            maxLen = max(currLen, maxLen)

            hash[ord(s[j])] = j 
            j+=1 

        return maxLen         