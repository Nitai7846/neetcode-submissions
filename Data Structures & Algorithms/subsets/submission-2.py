class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        ans = []
        res = []

        def backtracking(i):

            if i>=n:
                ans.append(res[:])
                return 
            
            res.append(nums[i])
            backtracking(i+1)
            res.pop()
            backtracking(i+1)

        backtracking(0)
        return ans 
        