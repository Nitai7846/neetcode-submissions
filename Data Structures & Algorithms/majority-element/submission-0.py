class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0)+1
        
        max_key = max(freq, key=freq.get)
        return max_key
            

        