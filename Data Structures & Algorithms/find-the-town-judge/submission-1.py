class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        incoming = {}
        outgoing = {}
        ans = -1

        for i in range(0, len(trust)):
            outgoing[trust[i][0]] = outgoing.get(trust[i][0], 0) + 1
            incoming[trust[i][1]] = incoming.get(trust[i][1], 0) + 1
        
        for i in range(1, n+1):

            if outgoing.get(i, 0)== 0 and incoming.get(i,0) == n-1:
                ans = i 
                break 
        
        return ans 
        
