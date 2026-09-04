class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj = defaultdict(set)
        inDegree = defaultdict(int)

        for word in words:
            for c in word:
                inDegree[c] = 0 
        
        for i in range(len(words)-1):

            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1) ,len(w2))

            if len(w1)>len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        inDegree[w2[j]] += 1
                    break 


        res = []
        q = deque()
        for c in inDegree:
            if inDegree[c] == 0:
                q.append(c)
        
        while q:

            node = q.popleft()
            res.append(node)

            for neighbor in adj[node]:
                inDegree[neighbor] -=1 
                
                if inDegree[neighbor] == 0:
                    q.append(neighbor)

        if len(res) != len(inDegree):
            return ""
        return "".join(res)
            
        

