class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        n = len(nums)
        mpp = {}

        for i in range(0, n):
            mpp[nums[i]] = mpp.get(nums[i], 0) + 1
        
        for i in range(0, n):
            if mpp[nums[i]] > 1:
                return True 
        
        return False 
        