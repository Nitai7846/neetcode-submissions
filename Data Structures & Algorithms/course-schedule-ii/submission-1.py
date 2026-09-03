class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = [[] for _ in range(numCourses)]
        inDegree = [0]*numCourses

        for it in prerequisites:
            u = it[0]
            v = it[1]

            adj[v].append(u)
        
        for i in range(numCourses):
            for j in adj[i]:
                inDegree[j] += 1
        
        ans = []

        q = deque()
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                q.append(i)
                ans.append(i)
        
        finish = 0

        while q:
            node = q.popleft()
            finish+=1

            for neighbor in adj[node]:

                inDegree[neighbor] -= 1 

                if inDegree[neighbor] == 0:
                    q.append(neighbor)
                    ans.append(neighbor)

        if finish == numCourses:
            return ans 
        else:
            return []