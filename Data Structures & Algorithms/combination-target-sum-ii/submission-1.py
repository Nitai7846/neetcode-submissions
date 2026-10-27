class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        res = []
        subset = []
        n = len(candidates)
        candidates.sort()

        def dfs(i, cur_sum):

            if cur_sum == target:
                res.append(subset[:])
                return 

            if i>=n:
                return 
            
            if cur_sum>target:
                return
            
            cur_sum += candidates[i]
            subset.append(candidates[i])
            dfs(i+1, cur_sum)
            cur_sum -= candidates[i]
            subset.pop()
            while i+1<n and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, cur_sum)

        dfs(0, 0)
        return res 
            

        