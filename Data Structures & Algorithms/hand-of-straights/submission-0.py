class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        n = len(hand)
        ans = True
        if n % groupSize != 0:
            return False

        hand.sort()

        freq = {}

        for card in hand:
            freq[card] = freq.get(card, 0)+1
        
        for i in range(0,n):

            if hand[i] not in freq:
                continue 
            start = hand[i]

            for j in range(0, groupSize):
                val = start+j

                if val in freq:
                    freq[val] -= 1
                    if freq[val] == 0:
                        del freq[val]
                
                else:
                    return False

        return ans      











            

        


        