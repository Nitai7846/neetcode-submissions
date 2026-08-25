class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_val = float('-inf') 
        pre_sum = 0 
        n = len(nums)

        for i in range(0, n):

            pre_sum = pre_sum + nums[i]
            max_val = max(max_val, pre_sum)

            if pre_sum < 0:

                pre_sum =  0
            
       
        
        return max_val
            

                

            


        