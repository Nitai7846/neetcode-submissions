class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n = len(nums)
        seen = set(nums)
        max_len = 0 


        for i in range(0, n):

            prev = nums[i] - 1
            if prev in seen:
                continue 
            
            start = nums[i]
            curr_len = 1
            while start+1 in seen:
                curr_len += 1
                start+=1
                
            max_len = max(max_len, curr_len)
            
        return max_len
            



        