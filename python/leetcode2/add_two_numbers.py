# AC Rate: 23.0%
# SOURCE URL: https://oj.leetcode.com/problems/add-two-numbers/
#
# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
