class Solution:

    def reverse(self, s):

        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:

        n = len(s)
        ans = []
        subset = []

        def dfs(i):

            if i == n:
                ans.append(subset.copy())
                return 
            
            for j in range(i, n):

                if self.reverse(s[i:j+1]):
                    subset.append(s[i:j+1])
                    dfs(j+1)
                    subset.pop()
        
        dfs(0)
        return ans 
                    

                
                

            
        