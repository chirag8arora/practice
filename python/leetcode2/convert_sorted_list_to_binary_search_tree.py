# AC Rate: 27.2%
# SOURCE URL: https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
#
# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
#


# used too much memory


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def ezhelper(self, array):
        if len(array) == 0:
            return None
        if len(array) == 1:
            return array[0]
        mid = len(array) / 2
        array[mid].left = self.ezhelper(array[:mid])
        array[mid].right = self.ezhelper(array[mid+1:])
        return array[mid]


    def sortedListToBST(self, head):
        l = []
        while head:
            l.append(TreeNode(head.val))
            head = head.next

        return self.ezhelper(l)

        # counter = 0
        # node = head
        # while node:
        #     counter += 1
        #     node = node.next

        # return self.helper(head, 0, counter-1)[0]

    # def helper(self, head, start, end):
    #     if end <= start:
    #         tr = head
    #         if head:
    #             tr = TreeNode(head.val)
    #         return tr, head
    #     mid = start + (end - start) / 2
    #     left_children, last = self.helper(head, start, mid - 1)
    #     if not last:
    #         return left_children, left_children
    #     parent = last.next
    #     last = TreeNode(last.val)
    #     if not parent:
    #         return left_children, last
    #     right_children, last = self.helper(parent.next, mid + 1, end)
    #     parent = TreeNode(parent.val)
    #     parent.left = left_children
    #     parent.right = right_children
    #     return parent, last

def print_t(node, pv = None):
    if node:
        # print (node.__class__)
        print pv, '->', node.val
        if hasattr(node, 'left'):
            print_t(node.left, node.val)
        if hasattr(node, 'right'):
            print_t(node.right, node.val)

def test(head):
    s = Solution()
    print_t(s.sortedListToBST(head))

def test_case1():
    head = ListNode(None)
    node = head
    for i in range(1, 10):
        node.next = ListNode(i)
        node = node.next
    head = head.next
    test(head)

def test_case2():
    head = ListNode(1)
    head.next = ListNode(3)
    test(head)

if __name__ == '__main__':
    test_case1()
    test_case2()

