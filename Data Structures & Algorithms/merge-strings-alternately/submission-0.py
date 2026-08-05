class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        m = len(word1)
        n = len(word2)
        ans = ""
        p1, p2 = 0, 0 

        while p1<m and p2<n:

            ans+=word1[p1]
            ans+=word2[p2]
            p1+=1
            p2+=1
        
        while p1<m:
            ans+=word1[p1]
            p1+=1
        while p2<n:
            ans+=word2[p2]
            p2+=1
        
        return ans 
        