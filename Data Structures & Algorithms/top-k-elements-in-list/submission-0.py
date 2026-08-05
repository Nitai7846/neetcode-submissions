class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        freq = {}

        for i in range(n):

            freq[nums[i]] = freq.get(nums[i], 0) + 1
        
        ans = []
        sorted_freq = sorted(freq.items(), key=lambda k: k[1])

        for val, count in sorted_freq[-k:]:
            ans.append(val)

        return ans 

        
        
        
             

        