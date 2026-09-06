class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = [[] for _ in range(n+1)]

        for time in times:

            u = time[0]
            v = time[1]
            cost = time[2]

            adj[u].append((v, cost))
        

        dist = [float('inf')] * (n+1)

        dist[k] = 0

        heap = [(0 ,k)]

        while heap:

            d, node = heapq.heappop(heap)

            if d > dist[node]:
                continue 
            
            for neighbor, weight in adj[node]:
                new_dist = d + weight 
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist 
                    heapq.heappush(heap, (new_dist, neighbor))
        
        ans = max(dist[1:])
        return ans if ans != float('inf') else -1 

            




        



        