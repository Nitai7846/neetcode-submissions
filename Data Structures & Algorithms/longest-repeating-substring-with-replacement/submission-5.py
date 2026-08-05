class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        res = 0 

        i, j = 0, 0 

        for j in range(len(s)):

            count[s[j]] = count.get(s[j], 0) + 1

            while (j-i+1) - max(count.values()) > k:

                count[s[i]] -=1 
                i+=1 
            
            res = max(res, j-i+1)

        return res


            



        
       



        