class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        ans = []
        res = []

        def backtrack(i):

            if i>=n:
                ans.append(res[:])
                return 
            
            res.append(nums[i])
            backtrack(i+1)
            res.pop()
            backtrack(i+1)
        
        backtrack(0)
        return ans 

            
        