class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not n:
            return True 
        
        adj = [[] for _ in range(n)]

        for it in edges:
            u = it[0]
            v = it[1]

            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()

        def dfs(node, prev):

            if node in visit:
                return False 
            
            visit.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue 
                if not dfs(nei, node):
                    return False 
            
            return True 

        return dfs(0, -1) and len(visit) == n


        