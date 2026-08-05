class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        ans = [0 ,0, 0]
        

        for i in range(0, len(triplets)):
            valid = True

            for j in range(0, 3):

                if triplets[i][j] > target[j]:
                    valid = False
                
            if valid:

                ans = [max(ans[0], triplets[i][0]), max(ans[1], triplets[i][1]), max(ans[2], triplets[i][2])]
        
        return ans == target 



                
                

                    
                







        