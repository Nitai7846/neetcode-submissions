class Solution:

    def findelement(self, arr, x):

        closest = float('inf')
        ind = 0
        for i in range(0, len(arr)):
            new_closest = abs(x - arr[i])
            if new_closest < closest:
                closest = new_closest
                ind = i
            else:
                continue

        return ind 


    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        n = len(arr)
        ind = self.findelement(arr, x)
        ans = []

        if ind == 0:
            return arr[0:k]
        if ind == n-1:
            return arr[n-k:n]
        
        ans.append(arr[ind])
        l,r = ind-1, ind+1 

        while len(ans) < k :

            if abs(x-arr[l]) <= abs(x - arr[r]):
                ans.append(arr[l])
                l-=1
            elif abs(x-arr[l]) >= abs(x-arr[r]):
                ans.append(arr[r])
                r+=1

        return sorted(ans)






        