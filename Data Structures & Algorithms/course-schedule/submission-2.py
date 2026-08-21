from collections import deque 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = [[] for _ in range(numCourses)]
        inDegree = [0]*numCourses 

        for it in prerequisites:
            u = it[0]
            v = it[1]
            adj[v].append(u)
        
        for i in range(numCourses):
            for j in adj[i]:
                inDegree[j] += 1

        finish = 0 

        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        while q:

            node = q.popleft()
            finish+=1

            for neighbor in adj[node]:
                inDegree[neighbor] -= 1

                if inDegree[neighbor] == 0:
                    q.append(neighbor)
        
        if finish == numCourses:
            return True 
        else:
            return False 

            

            



        
        