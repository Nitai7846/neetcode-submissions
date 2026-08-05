class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        dp = {}
        def dfs(i, n,dp):

            if i >=n-1:
                return 0
            
            if i in dp:
                return dp[i]

            ans = float('inf')
            for j in range(i+1, min(n, i+nums[i]+1)):

                ans = min(ans, 1 + dfs(j, n, dp))
            
            dp[i] = ans
            return ans 
        
        return dfs(0, n,dp)





        