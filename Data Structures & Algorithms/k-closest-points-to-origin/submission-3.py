class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        n = len(points)
        minHeap = []

        for i in range(0, n):
            x = points[i][0]
            y = points[i][1]

            dist = -(x**2 + y**2)
            heapq.heappush(minHeap, [dist, x, y])

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        while minHeap:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
        
        return res 
        

        