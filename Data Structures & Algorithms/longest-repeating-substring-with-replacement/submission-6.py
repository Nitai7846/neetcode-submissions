class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0 
        cnt = {}
        i = 0
        n = len(s)

        for j in range(n):

            cnt[s[j]] = cnt.get(s[j], 0) + 1

            while (j-i+1) - max(cnt.values()) > k:

                cnt[s[i]] -=1 
                i+=1

                
            
            res = max(res, j-i+1)
        
        return res 
        