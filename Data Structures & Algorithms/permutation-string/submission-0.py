class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n1 = len(s1)
        n2 = len(s2)

        if n1>n2:
            return False 
        
        freq1 = {}
        for char in s1:
            freq1[char] = freq1.get(char,0) + 1
        
        freq2 = {}
        for char in range(0,n1):
            freq2[s2[char]] = freq2.get(s2[char], 0) + 1

        i = 0
        j = n1
        
        while j<n2:

            if freq1 == freq2:
                return True
            
            elif freq1 != freq2:
                freq2[s2[i]] -= 1
                if freq2[s2[i]] == 0:
                    del freq2[s2[i]]
                    
                
                freq2[s2[j]] = freq2.get(s2[j], 0) + 1
            i+=1
            j+=1
        
        return freq1==freq2


            

            



                



            





