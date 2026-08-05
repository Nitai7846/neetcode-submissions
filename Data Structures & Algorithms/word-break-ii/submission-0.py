class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        n = len(s)
        cur = []
        res = []
        wordDict = set(wordDict)

        def dfs(i):

            if i == n:
                res.append(" ".join(cur))
                return 
            
            for j in range(i, len(s)):
                w = s[i:j+1]
                if w in wordDict:
                    cur.append(w)
                    dfs(j+1)
                    cur.pop()
        
        dfs(0)
        return res 
            

      
                
        