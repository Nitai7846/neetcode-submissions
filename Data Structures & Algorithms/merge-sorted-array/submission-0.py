class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        l , r = m-1, n-1 
        e = m + n -1 

        while l>=0 and r>=0:

            if nums1[l] >= nums2[r]:
                nums1[e] = nums1[l]
                e-=1
                l-=1
            
            elif nums2[r] > nums1[l]:
                nums1[e] = nums2[r]
                e-=1
                r-=1
        
        while r>=0:
            nums1[e] = nums2[r]
            e-=1
            r-=1
        

        