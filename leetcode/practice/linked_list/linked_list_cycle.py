
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        point1 = point2 = head
        while point2 != None and point2.next != None:
            point1 = point1.next
            point2 = point2.next.next
            if point1 == point2:
                return True
        return False