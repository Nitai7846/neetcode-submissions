class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        total_sum = 0 
        for i in range(0, n):
            total_sum += nums[i]
        
        remainder = total_sum % k 
        if remainder == 0:
            side = total_sum // k
        else:
            return False 

        buckets = [0]*k 
        nums.sort(reverse=True)
        if nums[0]>side:
            return False 

        def backtracking(i):
            
            if i == n:
                return True 
            
            for j in range(0, len(buckets)):

                val_sum = buckets[j] + nums[i]
                if val_sum <= side:
                    buckets[j] = val_sum 
                    if backtracking(i+1):
                        return True 
                    buckets[j] -= nums[i]
                    if buckets[j] == 0:
                        break
            
            return False 
        
        return backtracking(0)



        