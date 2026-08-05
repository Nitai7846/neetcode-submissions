class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)
        new_n = 2 * n
        ans = [0] * new_n
        for i in range(0,n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        
        return ans
        