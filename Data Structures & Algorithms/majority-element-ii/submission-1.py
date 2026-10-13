class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        mpp = {}
        ans = []
        n = len(nums)
        for i in range(0, n):
            mpp[nums[i]] = mpp.get(nums[i], 0) + 1 

        
        for key,value in mpp.items():

            if value > n//3:
                ans.append(key)
        
        return ans 


        