class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        freq = {}
        ans = []
        counter = 0

        for i in range(0, n):

            freq[nums[i]] = freq.get(nums[i], 0) + 1
        
        buckets = [[] for _ in range(n+1)]

        for value, count in freq.items():

            buckets[count].append(value)
        
        for i in range(n, -1, -1):
            for element in buckets[i]:
                ans.append(element)
                counter+=1
            
                if counter == k:
                    return ans 
                
            
            
        