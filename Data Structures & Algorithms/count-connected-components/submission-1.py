class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for _ in range(n)]
    
        for it in edges:

            u = it[0]
            v = it[1]

            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()

        def dfs(node):
            for nei in adj[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)

        res = 0 
        for node in range(n):
            if node not in visit:
                dfs(node)
                res += 1
        
        return res 
                

                
            