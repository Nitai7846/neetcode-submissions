class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []

        def dfs(i, total):
            if total == target:
                ans.append(subset.copy())
                return
            if total > target:
                return

            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(j, total + nums[j])   # j, not j+1 — reuse allowed
                subset.pop()

        dfs(0, 0)
        return ans
        

    

                

                

        