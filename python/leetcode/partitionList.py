# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode

    def partition(self, head, x):
        prev_node, node = None, head
        node_wall_left, node_wall_right = None, None

        # todo dealwith last node
        while node:
            if node.val < x and node_wall_right:
                if not node_wall_left:
                    head = node
                else:
                    node_wall_left.next = node
                node_wall_left = node
                prev_node.next = node.next
                node.next = node_wall_right
                node = node.next
                continue
            elif node.val >= x and not node_wall_right:
                node_wall_left = prev_node
                node_wall_right = node
            prev_node = node
            node = node.next
        return head


# 2 l2, r1 1
# 1 4 left 1 right 4 3 2 3=>

if __name__ == '__main__':
    # ll = ListNode(1)
    # ll.next = ListNode(4)
    # ll.next.next = ListNode(3)
    # ll.next.next.next = ListNode(2)
    # ll.next.next.next.next = ListNode(5)
    # ll.next.next.next.next.next = ListNode(2)
    ll = ListNode(2)
    ll.next = ListNode(1)

    s = Solution()
    ll = s.partition(ll, 2)
    while ll:
        print ll.val
        ll = ll.next

