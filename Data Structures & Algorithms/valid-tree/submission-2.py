class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = [[] for _ in range(n)]
        visit = set()

        for it in edges:
            u = it[0]
            v = it[1]

            adj[u].append(v)
            adj[v].append(u)
        
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
        
        return dfs(0,-1) and n == len(visit)
        