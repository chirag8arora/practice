# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @return a ListNode

    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        result = head
        tmp = 0
        while l1 and l2:
            tmp += l1.val + l2.val
            result.next = ListNode(tmp % 10)
            tmp /= 10
            result = result.next
            l1 = l1.next
            l2 = l2.next
        rest = None
        if l1:
            rest = l1
        elif l2:
            rest = l2

        while rest:
            tmp += rest.val
            result.next = ListNode(tmp % 10)
            tmp /= 10
            result = result.next
            rest = rest.next
        if tmp:
            result.next = ListNode(tmp)
        return head.next

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(0)
    l1.next = ListNode(0)
    l1.next.next = ListNode(5)

    l2 = ListNode(0)
    l2.next = ListNode(0)
    l2.next.next = ListNode(5)
    result = s.addTwoNumbers(l1, l2)
    while result:
        print result.val
        result = result.next
