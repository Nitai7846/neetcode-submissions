class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        ans = [0]*n 
        stack = []

        for i in range(0,n):

            while stack and (temperatures[stack[-1]] < temperatures[i]):

                index = stack[-1]
                ans[index] = i - index 
                stack.pop()
            
            stack.append(i)

        return ans 
        