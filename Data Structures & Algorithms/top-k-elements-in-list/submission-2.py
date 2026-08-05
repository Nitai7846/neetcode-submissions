class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        freq = {}
        ans = []

        for i in range(0, n):
            freq[nums[i]] = freq.get(nums[i], 0) + 1 
        
        buckets = [[] for _ in range(n+1)]

        for element, value in freq.items():
            buckets[value].append(element)
        
        for i in range(n, -1, -1):
            for ele in buckets[i]:
                ans.append(ele)
                if len(ans) == k:
                    return ans 
       

        