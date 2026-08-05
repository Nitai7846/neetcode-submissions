class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)
        ans = []
        nums.sort()

        for i in range(0, n-3):
            if i>0 and nums[i] == nums[i-1]:
                continue 
            for j in range(i+1, n-2):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                k = j+1
                m = n-1 

                while k<m:
                    val = nums[i] + nums[j] + nums[k] + nums[m]
                    if val == target:
                        ans.append([nums[i], nums[j], nums[k], nums[m]])
                        k+=1
                        m-=1

                        while k<m and nums[k] == nums[k-1]:
                            k+=1
                        while k<m and nums[m] == nums[m+1]:
                            m-=1
                    
                    elif val<target:
                        k+=1
                    else:
                        m-=1
        
        return ans 







        
        