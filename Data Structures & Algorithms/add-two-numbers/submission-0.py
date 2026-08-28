# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1 = l1
        cur2 = l2
        carry = 0
        dummy = ListNode()
        current = dummy

        while cur1 or cur2:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            
            curDigit = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            newNode = ListNode(curDigit)
            current.next = newNode 
            current = current.next
            
            if cur1: 
                cur1 = cur1.next 
            if cur2: 
                cur2 = cur2.next

        if (cur1 is None) and (cur2 is None) and carry == 1:
            current.next = ListNode(carry)
         
        return dummy.next 