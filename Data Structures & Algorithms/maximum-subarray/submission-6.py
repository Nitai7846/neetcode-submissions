class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        curSum = 0 
        ans = float('-inf')

        if n == 1:
            return nums[0]
        

        j = 0
        while j<n:

            curSum += nums[j]
            ans = max(ans, curSum)
                
            if curSum <=0:
                curSum = 0 
            
            j+=1
            
        
        return ans


        


        