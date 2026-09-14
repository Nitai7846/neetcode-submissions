class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)
        ans = []
        res = []

        def dfs(i, value):

            if i>=n:
                return 

            if value == target:
                ans.append(res[:])
                return 
            
            if value > target:
                return 
            
            value += nums[i]
            res.append(nums[i])
            dfs(i, value)
            res.pop()
            value -= nums[i]
            dfs(i+1, value)
        
        dfs(0, 0)
        return ans
            
                
            
            

            
        