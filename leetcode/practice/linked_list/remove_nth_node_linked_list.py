class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = 0
        curr = head
        temp = head
        while i < n:
            i += 1
            temp = temp.next
        if not temp:
            head = head.next
            return head
        else:
            while temp.next is not None:
                curr = curr.next
                temp = temp.next

            curr.next = curr.next.next

            return head