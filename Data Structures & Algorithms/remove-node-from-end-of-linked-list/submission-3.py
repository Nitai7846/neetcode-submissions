# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        temp = head
        prev = None 

        while temp:

            curr = temp.next 
            temp.next = prev 
            prev = temp 
            temp = curr 
        
        counter = 1
        newHead = prev 
        dummyNode = ListNode(-1)
        dummyNode.next = newHead 
        temp_prev = dummyNode

        while newHead:

            if n == counter:
                temp_prev.next = newHead.next 
                break 
                   

            temp_prev = newHead 
            counter+=1
            newHead = newHead.next 
        
        temp = dummyNode.next
        prev = None 

        while temp:

            curr = temp.next 
            temp.next = prev 
            prev = temp 
            temp = curr 

        return prev
        






    

        
        