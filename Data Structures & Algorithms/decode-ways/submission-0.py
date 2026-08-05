class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        cache = [-1]*len(s)

        def dfs(i):

            if i >= n:
                return 1    

            if s[i] == '0':
                return 0  

            if cache[i] != -1:
                return cache[i]
            

            cache[i] = dfs(i+1) 

            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                cache[i] += dfs(i+2)


            return cache[i]
        
        ans = dfs(0)

        return ans 
     


            
                





        