class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = {}

        def dfs(i,j,word1, word2):

            if i>=len(word1):
                return len(word2) - j
            
            if j>=len(word2):
                return len(word1) - i
            
            if (i,j) in dp:
                return dp[(i,j)]

            if word1[i] == word2[j]:
                dp[(i,j)] = dfs(i+1, j+1, word1, word2)
                return dp[(i,j)]

            if word1[i] != word2[j]:

                dp[(i,j)] = 1 + min(
                    dfs(i+1, j+1, word1, word2), 
                    dfs(i+1, j, word1, word2),
                    dfs(i, j+1, word1, word2)
                )

                return dp[(i,j)]
        
        return dfs(0,0,word1,word2)
        