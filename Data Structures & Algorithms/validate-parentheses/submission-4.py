class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closeToOpen = {')':'(', '}':'{', ']':'['}
        n = len(s)
        i = 0

        while i<n:

            if s[i] in closeToOpen and stack:
                if stack[-1] == closeToOpen[s[i]]:
                    stack.pop()
                    i+=1
                else:
                    return False
            
            else:
                stack.append(s[i])
                i+=1
        
        if stack:
            return False
        else:
            return True 






        