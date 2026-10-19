class Solution:
    def validPalindrome(self, s: str) -> bool:

        def checkPalindrome(i, j):
            while i<j:
                if s[i] != s[j]:
                    return False 
                i+=1
                j-=1
            return True 
        
        n = len(s)
        i,j = 0, n-1 

        while i < j:

            if s[i] != s[j]:
                return (checkPalindrome(i + 1, j) or
                        checkPalindrome(i, j - 1))

            i += 1
            j -= 1

        return True


        

        
        