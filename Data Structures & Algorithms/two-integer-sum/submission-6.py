class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mpp = {}

        for i in range(0, len(nums)):

            difference = target - nums[i]
            if difference in mpp:
                return [mpp[difference], i]
            
            mpp[nums[i]] = i 

    
        