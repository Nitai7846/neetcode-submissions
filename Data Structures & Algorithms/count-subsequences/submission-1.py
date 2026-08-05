class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        if len(s) < len(t):
            return 0
        
        dp = {}
        def dfs(i, j, s, t, dp):

            if j ==len(t):
                return 1 
            
            if i >= len(s) :
                return 0 
            
            if (i,j) in dp:
                return dp[(i,j)]

            if s[i] == t[j]:

                dp[(i,j)]  = dfs(i+1, j+1, s, t, dp) + dfs(i+1, j, s, t, dp)
                return dp[(i,j)]
            
            if s[i] != t[j]:
                dp[(i, j)] =  dfs(i+1, j, s, t, dp)
                return dp[(i,j)]

        return dfs(0 , 0 , s, t, dp)

        