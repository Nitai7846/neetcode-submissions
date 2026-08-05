class Solution:

    def reverse(self, s):

        return s == s[::-1]
    

    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        subset = []

        n = len(s)

        def dfs(i, s, subset):

            if i==len(s):
                res.append(subset.copy())
                return 
                
            for j in range(i, n):
                if self.reverse(s[i:j+1]):
                    subset.append(s[i:j+1])
                    dfs(j+1, s, subset)
                    subset.pop()

        dfs(0, s, [])
        return res 
                
        
        
      


            

            





        


        
        