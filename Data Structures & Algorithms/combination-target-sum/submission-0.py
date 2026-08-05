class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        subset = []

        def dfs(i, value):

            if i>=len(nums):
                return 

            if value == target:
                res.append(subset.copy())
                return 

            elif value > target:

                return 

            value += nums[i]

            subset.append(nums[i])
            dfs(i, value)
            subset.pop()
            value -= nums[i]
            dfs(i+1, value)
        
        

        dfs(0,0)
        return res 



        