class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix = [1] * (n+1)
        postfix = [1] * (n+1)
        ans = []


        for i in range(1,n):
            prefix[i] = nums[i-1] * prefix[i-1]
        
        for i in range(n-2,-1,-1):
            postfix[i] = postfix[i+1] * nums[i+1]
        
        for i in range(0,n):
            ans.append(prefix[i] * postfix[i]) 
        
        return ans
            


        
        
            



    