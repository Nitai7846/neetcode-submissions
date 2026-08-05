class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #your code goes here 

        n = len(s)
        l, r = 0, 0 
        max_len = 0 
        max_freq = 0
        hash = [0] * 26
        

        while r < n:
            
            hash[ord(s[r]) - ord('A')] += 1 
            max_freq = max(hash)

            if (r-l+1) - max_freq > k:
                hash[ord(s[l]) - ord('A')] -= 1 
                l+=1
                
            max_len = max(r-l+1, max_len)
            r+=1
        
        return max_len 
            




           








        

