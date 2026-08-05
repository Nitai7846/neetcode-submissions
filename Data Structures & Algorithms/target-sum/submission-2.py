class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:


        n = len(nums)
        dp = {}

        def dfs(i, run_sum):

            if i>=n and run_sum == target:
                return 1 
            
            if i>=n:
                return 0
            
            if (i, run_sum) in dp:
                return dp[(i, run_sum)]
            
            count = dfs(i+1, run_sum-nums[i]) + dfs(i+1, run_sum + nums[i])
            dp[(i, run_sum)] = count
            return dp[(i, run_sum)]
        
        return dfs(0, 0)


            

        