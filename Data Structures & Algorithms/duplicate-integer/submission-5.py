class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        n = len(nums)
        freq = {}

        for i in range(0 ,n):

            if nums[i] in freq:
                return True 
            
            freq[nums[i]]  = freq.get(nums[i], 0) + 1
        
        return False