class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums

        mpp = {}
        for num in nums:
            mpp[num] = mpp.get(num, 0) + 1
        
        cnt0 = mpp.get(0, 0)
        cnt1 = mpp.get(1, 0)
        cnt2 = mpp.get(2, 0)

        for i in range(0, cnt0):
            nums[i] = 0
        for i in range(cnt0, cnt0+cnt1):
            nums[i] = 1
        for i in range(cnt0+cnt1, cnt0+cnt1+cnt2):
            nums[i] = 2 
        
        return nums 
