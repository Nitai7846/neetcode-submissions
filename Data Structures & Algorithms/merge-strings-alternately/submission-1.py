class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        n1 = len(word1)
        n2 = len(word2)

        i, j = 0, 0 
        res = ""

        while i<n1 and j<n2:

            res+=word1[i]
            i+=1
            res+=word2[j]
            j+=1
        
        while i<n1:
            res+=word1[i]
            i+=1
        
        while j<n2:
            res+=word2[j]
            j+=1

        return res 


        