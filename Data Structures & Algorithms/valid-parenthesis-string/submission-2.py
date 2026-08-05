class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        memo = {}

        def dfs(i, open):
            if open < 0:
                return False
            if i == n:
                return open == 0
            if (i, open) in memo:
                return memo[(i, open)]
            
            if s[i] == '(':
                result = dfs(i+1, open+1)
            elif s[i] == ')':
                result = dfs(i+1, open-1)
            else:
                result = (dfs(i+1, open) or 
                          dfs(i+1, open-1) or 
                          dfs(i+1, open+1))
            
            memo[(i, open)] = result
            return result

        return dfs(0, 0)