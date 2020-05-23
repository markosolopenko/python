
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        arrA = self.A(headA)
        arrB = self.B(headB)
        if arrA and arrB:
            if arrA == arrB:
                return arrA[0]

            elif len(arrA) > len(arrB):
                arrA = arrA[len(arrA) - len(arrB):]
                for i in range(len(arrA)):
                    if arrA == arrB:
                        break
                    else:
                        arrA.remove(arrA[0])
                        arrB.remove(arrB[0])
                if arrA:
                    return arrA[0]

            elif len(arrB) > len(arrA):
                arrB = arrB[len(arrB) - len(arrA):]
                if arrB == arrA:
                    return arrB[0]
                for i in range(len(arrB)):
                    if arrA == arrB:
                        break
                    else:
                        arrA.remove(arrA[0])
                        arrB.remove(arrB[0])
                if arrB:
                    return arrB[0]
            else:
                for i in range(len(arrB)):
                    if arrA == arrB:
                        break
                    else:
                        arrA.remove(arrA[0])
                        arrB.remove(arrB[0])
                if arrB:
                    return arrB[0]

    def A(self, node):
        arr = []
        while node is not None:
            arr.append(node)
            node = node.next
        return arr

    def B(self, node):
        arr = []
        while node is not None:
            arr.append(node)
            node = node.next
        return arr


if __name__ == '__main__':
    my_class = Solution()
    # print(my_class.getIntersectionNode(headA=, headB=))