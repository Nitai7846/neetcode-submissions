class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:


        n = len(nums)

        def dfs(i, run_sum):

            if i>=n and run_sum == target:
                return 1 
            
            if i>=n:
                return 0
            
            count = dfs(i+1, run_sum-nums[i]) + dfs(i+1, run_sum + nums[i])

            return count 
        
        return dfs(0, 0)


            

        