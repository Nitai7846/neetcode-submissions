class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        maxHeap = [-num for num in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            first = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)
            
            if first > second:
                diff = first - second
                heapq.heappush(maxHeap, -diff)  # ← Negate here
            elif second > first:
                diff = second - first
                heapq.heappush(maxHeap, -diff)  # ← Negate here
            # else: both equal, don't push (continue works)
        
        if maxHeap:
            return -maxHeap[0]  # ← Negate here
        else:
            return 0