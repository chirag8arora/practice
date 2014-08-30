# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        pass

def main():
    head = ListNode(1)
    ll = head
    for i in range(2, 11):
        ll.next = ListNode(i)
        ll = ll.next

    ll = head
    while ll:
        print ll.val,
        ll = ll.next

if __name__ == '__main__':
    main()
