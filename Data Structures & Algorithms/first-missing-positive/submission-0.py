class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        fp = 1 

        for num in num_set:

            if num <= 0:
                continue 
            
            if fp in num_set:
                fp+=1 
            
            else:
                return fp 
        
        return fp 