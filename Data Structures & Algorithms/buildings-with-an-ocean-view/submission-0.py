class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        max_height = 0 
        n = len(heights)
        ans = []

        for i in range(n-1, -1, -1):

            if heights[i] > max_height:
                ans.append(i)
                max_height = heights[i]
        
        l, r = 0, len(ans)-1 

        while l<=r:
            ans[l], ans[r] = ans[r], ans[l]
            l+=1
            r-=1 
        
        return ans


       




        