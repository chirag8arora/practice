# merge sorted list
class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

    def __iter__(self):
        while self:
            yield self
            self = self.next

class ListFactory():
    def gen_list(self, A):
        if not A:
            return None
        dummy_head = ListNode(0)
        node = dummy_head
        for i in A:
            node.next = ListNode(i)
            node = node.next
        return dummy_head.next

class Solution():
    def merge(self, l1, l2):
        dummy_head = ListNode(0)
        node = dummy_head
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        left = l1 if l1 else l2
        node.next = left
        return dummy_head.next

f = ListFactory()
l1 = f.gen_list([1,4,7])
l2 = f.gen_list([2,3,6])
s = Solution()
for i in s.merge(l1, l2):
    print i.val
