class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        mapping = {"2":"abc" , "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        ans = []

        def backtrack(i, current):

            if len(current) == len(digits):
                ans.append(current)
                return 
            
            for char in mapping[digits[i]]:
                backtrack(i+1, current+char)
        
        backtrack(0, "")
        return ans


            

            







        
        