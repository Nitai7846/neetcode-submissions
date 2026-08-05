class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        
        i,j = 0, 0
        minlen = float("inf")
        n = len(s)
        mpp_t = {}
        for c in range(len(t)):
            mpp_t[t[c]] = mpp_t.get(t[c], 0) + 1

        need = len(mpp_t)
        have = 0
        mpp_s = {}
        while j < n:
            
            mpp_s[s[j]] = mpp_s.get(s[j], 0) + 1
            if s[j] in mpp_t and mpp_s[s[j]] == mpp_t[s[j]]:
                have+=1
                while have>=need:
                    if j-i+1 < minlen:
                        minlen = j-i+1
                        start = i
                    mpp_s[s[i]] -= 1
                    if s[i] in mpp_t and mpp_s[s[i]] < mpp_t[s[i]]:
                        have-=1
                    i+=1
            j+=1 

        return s[start:start + minlen] if minlen != float("inf") else ""
               
                







        