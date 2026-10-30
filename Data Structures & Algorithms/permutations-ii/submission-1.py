class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        subset = []
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        

        def dfs(i):
            
            if len(subset) == len(nums):
                res.append(subset[:])
                return 
            
            for n in count:
                if count[n] > 0:
                    subset.append(n)
                    count[n] -= 1
                    dfs(i)
                    subset.pop()
                    count[n] += 1
            
        
        dfs(0)
        return res
                    
                    
                    
                




                

        