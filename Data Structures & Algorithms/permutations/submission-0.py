class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res = []
        subset = []
        picked = [False] * n 

        def dfs(i, picked, subset):

            if len(subset) >= n:
                res.append(subset.copy())
                return 

            for i in range(0, n):
            
                if picked[i] == False:
                    subset.append(nums[i])
                    picked[i] = True
                    dfs(i, picked, subset)
                    subset.pop()
                    picked[i] = False
        
        dfs(0, picked, [])
        return res 


               










        