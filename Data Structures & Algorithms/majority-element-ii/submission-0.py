class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums)
        mpp = {}
        ans = []

        for i in range(0, n):
            mpp[nums[i]] = mpp.get(nums[i], 0) + 1
        
        for key, val in mpp.items():
            if val > n/3:
                ans.append(key)
        
        return ans 

        