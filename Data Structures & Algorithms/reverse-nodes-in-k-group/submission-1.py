# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse_list(self, head, k):  

        temp = head 
        prev = None
        tail = temp 
        count = 0 

        while temp and count<k:

            curr = temp.next 
            temp.next = prev 
            prev = temp 
            temp = curr
            count+=1
        
        return prev, tail 


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        current = head 
        new_head = None
        prev_tail = None

        while current:

            check = current 
            count = 0 

            while check and count<k:
                check = check.next 
                count+=1
            
            if count<k:
                break 
            
            group_head, group_tail = self.reverse_list(current, k)
            
            if new_head is None:
                new_head = group_head 
            else:
                prev_tail.next = group_head 
            
            group_tail.next = check 

            prev_tail = group_tail 

            current = check 
        
        if new_head is None:
            return head 
        
        return new_head 









        

        

        

        

        

        

        


        