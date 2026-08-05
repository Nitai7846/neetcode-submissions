class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        mpp = {0:1}
        res, running = 0, 0 

        for i in range(n):

            running = nums[i] + running
            
            if (running-k) in mpp:
                res += mpp[running-k]

            mpp[running]  = mpp.get(running, 0) + 1
        
        return res 







        