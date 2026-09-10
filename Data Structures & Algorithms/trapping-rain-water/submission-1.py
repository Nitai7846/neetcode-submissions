class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        total_water = 0 
        l, r = 0 , n-1
        leftMax, rightMax = height[l], height[r]


        while l<r:

            if leftMax < rightMax:
                l+=1 
                leftMax = max(leftMax, height[l])
                total_water += leftMax - height[l]
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                total_water += rightMax - height[r]
        
        return total_water 
                
            

            


        

        
        