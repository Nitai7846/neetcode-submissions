class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []
        res = []

        def backtracking(i):

            if len(res) == k:
                ans.append(res[:])
                return 
            
            if len(res)>k:
                return 

            for val in range(i, n+1):
                res.append(val)
                backtracking(val+1)
                res.pop()
            
        backtracking(1)
        return ans 


        