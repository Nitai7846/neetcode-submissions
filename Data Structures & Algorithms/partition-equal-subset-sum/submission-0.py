class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)
        cache = {}

        def dfs(i, target):
            if target == 0:
                return True
            if i >= n or target < 0:
                return False
            if (i, target) in cache:
                return cache[(i, target)]

            # include nums[i] or skip it
            cache[(i, target)] = dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
            return cache[(i, target)]

        return dfs(0, target)
           









            

        


        