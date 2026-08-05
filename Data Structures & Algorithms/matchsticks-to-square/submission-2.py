class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        n = len(matchsticks)
        array_sum = 0
        for i in range(0, n):
            array_sum += matchsticks[i]
        
        if array_sum % 4 == 0:
            side = array_sum // 4
        else:
            return False 
        
        matchsticks.sort(reverse=True)
        if matchsticks[0] > side:
            return False

        buckets = [0]*4

        def backtracking(i):

            if i == n:
                return True 
            
            for k in range(len(buckets)):
                val = matchsticks[i] + buckets[k]
                if val <= side:
                    buckets[k] = val 
                    if backtracking(i+1):
                        return True
                    buckets[k] -= matchsticks[i]

            return False 
        
        return backtracking(0)

                






            
            

            
        
