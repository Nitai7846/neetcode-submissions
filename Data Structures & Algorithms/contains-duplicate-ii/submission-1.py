class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        if n == 1:
            return False
        
        seen = set()
        window_len = 0
        ans = False

        for i in range(0, n):

            if window_len <= k:
                if nums[i] in seen:
                    return True
                seen.add(nums[i])
                window_len +=1 
            
            if window_len > k:
                seen.remove(nums[i-k])
                window_len -= 1
        
        return ans

            
                





        

            



        