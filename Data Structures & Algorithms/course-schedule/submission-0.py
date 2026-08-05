from collections import deque
class Solution:

    def topo(self, numCourses, adj):

        ans = []
        inDegree = [0] * numCourses

        for i in range(numCourses):
            for it in adj[i]:
                inDegree[it] += 1
        
        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            ans.append(node)

            for it in adj[node]:
                inDegree[it] -= 1
                if inDegree[it] == 0:
                    q.append(it)
        
        return ans 


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = [[] for _ in range(numCourses)]

        for it in prerequisites:
            u = it[0]
            v = it[1]

            adj[v].append(u)

        topo_list = self.topo(numCourses, adj)
        if len(topo_list) < numCourses:
            return False
        return True 
        

        