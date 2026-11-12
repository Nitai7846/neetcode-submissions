class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        n1 = len(s)
        n2 = len(t)

        mpp_s = {}
        mpp_t = {}

        for i in range(0, n1):
            mpp_s[s[i]] = mpp_s.get(s[i] , 0) + 1
        
        for i in range(0, n2):
            mpp_t[t[i]] = mpp_t.get(t[i], 0) + 1
        

        if mpp_s != mpp_t:
            return False
        else:
            return True 




        