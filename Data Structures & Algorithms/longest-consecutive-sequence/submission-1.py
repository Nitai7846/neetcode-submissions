class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)
        n = len(nums)
        length = 0 

        for i in range(0, n):

            if nums[i] - 1 not in numset:

                start = nums[i] 
                count = 1
                while start + 1 in numset:
                    count+=1
                    start+=1
                    
                
                length = max(count, length)

        return length
                
        