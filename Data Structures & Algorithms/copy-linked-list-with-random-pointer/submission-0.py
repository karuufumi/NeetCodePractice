"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        d = {}
        ls = Node(0)
        temp = ls
        curr = head
        while curr:
            t = Node(curr.val)
            d[curr] = t
            if temp: temp.next = t
            temp = temp.next
            curr = curr.next
        curr = head
        while curr:
            if curr.random:
                d[curr].random = d[curr.random]
            else:
                d[curr].random = None
            curr = curr.next
        return ls.next
