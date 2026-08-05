import sys
sys.setrecursionlimit(100000)
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        dp = {}


        def dfs(i, n, dp):

            if i>=n-1:
                return True 
            
            if nums[i] == 0:
                return False
            
            if i in dp:
                return dp[i]

            for j in range(i+1, i+nums[i]+1):
                ans =  dfs(j, n, dp)
                if ans == True:
                    return True
            
            dp[i] = ans

            return ans 
        
        return dfs(0, n, dp)

            




        