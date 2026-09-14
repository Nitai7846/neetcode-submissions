class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        ans = []
        res = []
        picked = [False]*n

        def dfs(i):

            if len(res) == n:
                ans.append(res[:])
                return 
            
            for i in range(0,n):

                if picked[i] == False:
                    res.append(nums[i])
                    picked[i] = True 
                    dfs(i+1)
                    res.pop()
                    picked[i] = False 
        
        dfs(0)
        return ans 