# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        index = -1
        seen = set()
        node = head

        while node is not None:

            if node in seen:
                index = node
                break
            else:
                seen.add(node)
            
            node = node.next
        
        if index!= -1 :
            return True 

        else :
            return False



        