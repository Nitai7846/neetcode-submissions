class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]

        def helper(lo, high):

            if high - lo == 1:
                return nums[lo]

            dp = [0] * n
            dp[lo] = nums[lo]
            dp[lo + 1] = max(nums[lo], nums[lo + 1])

            for i in range(lo+2, high):
                dp[i] = max(nums[i]+dp[i-2], dp[i-1])
            
            return dp[high-1]
        
        return max(helper(0,n-1), helper(1,n))

        