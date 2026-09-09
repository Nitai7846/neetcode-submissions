class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n = len(nums)
        min_len = float('inf')
        val = 0 
        i,j = 0, 0

        while j<n:

            val += nums[j]

            if val >= target:


                while val >= target and i<=j :
                    
                    min_len = min(min_len, j-i+1)
                    val -= nums[i]
                    i+=1 
                
      

            j+=1 
        
        if min_len != float('inf'):
            return min_len 
        else:
            return 0 

            

