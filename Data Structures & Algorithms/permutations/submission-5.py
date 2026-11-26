class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        ans = []
        subset = []
        visited = [False]*n

        def dfs():

            if len(subset) == n:
                ans.append(subset[:])
                return 
            
            for i in range(0, n):
                if visited[i]:
                    continue
                
                subset.append(nums[i])
                visited[i] = True 
                dfs()
                subset.pop()
                visited[i] = False
        
        dfs()
        return ans










        