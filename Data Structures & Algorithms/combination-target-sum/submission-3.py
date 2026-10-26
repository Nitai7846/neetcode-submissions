class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        subset = []
        n = len(nums)

        def dfs(i, curr_val):

            if i>=n:
                return 
            
            if curr_val > target:
                return 
            
            if curr_val == target:
                res.append(subset[:])
                return 
            
            curr_val += nums[i]
            subset.append(nums[i])
            dfs(i, curr_val)
            subset.pop()
            curr_val-=nums[i]
            dfs(i+1, curr_val)
        
        dfs(0, 0)
        return res

            
            
             







        