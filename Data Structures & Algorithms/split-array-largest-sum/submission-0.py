class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        n = len(nums)
        low = max(nums)
        high = sum(nums)

        ans = high

        def helper(nums, mid):
            count = 1
            local_val = 0 
            for i in range(0, n):
                if local_val + nums[i] > mid:
                    count +=1 
                    local_val = nums[i]
                else:
                    local_val += nums[i]
            
            return count<=k 

        while low<=high:

            mid = (low+high) // 2 
            if helper(nums, mid):
                ans = min(ans, mid)
                high = mid-1 
            else:
                low = mid+1 
        
        return ans 


         

        