class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        n = len(weights)
        low = max(weights)
        high = sum(weights)

        ans = high 

        def feasible(weights, day_weight):

            num_days = 1 
            current_weight = 0 
            for w in weights:
                if current_weight + w > day_weight:
                    num_days += 1 
                    current_weight = w 
                else:
                    current_weight += w 
            
            return num_days <= days


        while low<=high:

            mid = (low+high) // 2
            if feasible(weights, mid):
                ans = min(ans, mid)
                high = mid-1
            else:
                low = mid+1
        
        return ans
            

            
            

            
        