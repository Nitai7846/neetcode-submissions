class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mapping = {"2":"abc" , "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}


        if not digits:
            return []
        
        ans = []
        subset = []

        def dfs(i):

            if i == len(digits):
                ans.append("".join(subset))
                return 
            
            for char in mapping[digits[i]]:
                subset.append(char)
                dfs(i+1)
                subset.pop()
        
        dfs(0)
        return ans 
                


            

        
        