# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp 
        if n==1:
            reversed_head = prev.next
        else:
            reversed_head = prev
            curr= prev
            for _ in range(n-2):
                curr=curr.next
            curr.next= curr.next.next
        prev_back = None
        current_back = reversed_head
        while current_back:
            temp = current_back.next
            current_back.next= prev_back
            prev_back= current_back
            current_back=temp
        return prev_back


