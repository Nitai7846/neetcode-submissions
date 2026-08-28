import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        n = len(piles)
        right = max(piles)
        left = 1 

        def isFeasible(piles, mid):
            hours = 0 
            for i in range(0, n):
                hours += math.ceil(piles[i]/mid)
            
            if hours <= h:
                return True 
            else:
                return False 


        while left < right:

            mid = (left + right) // 2 
            
            if isFeasible(piles, mid):
                right = mid 
            
            else:
                left = mid + 1
           
            
        return left 





        